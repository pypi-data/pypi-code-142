import base64
import json
import os
import shutil
import subprocess
import tempfile
from shutil import which

import questionary
import yaml

from servicefoundry.lib.clients.git_client import GitClient, GitRepo
from servicefoundry.lib.clients.service_foundry_client import (
    ServiceFoundryServiceClient,
)
from servicefoundry.logger import logger


class InfraConfig:
    # Config needed for the provisioning step where terraform is run
    provisioning = {
        "provider": None,
        "awsInputs": {
            "remoteStateBucket": None,
            "region": "eu-west-1",
            "shortRegion": "euwe1",
            "remoteStateAwsProfile": None,
            "awsProfile": None,
            "accountId": None,
            "accountName": None,
            "clusterPrefix": "tfy-",
            "baseDomain": "truefoundry.com",
            "externalNetworkConfig": {
                "networkVpcId": None,
                "networkPublicSubnetsId": [],
                "networkPrivateSubnetsId": [],
            },
        },
    }
    # Config needed for the boostrapping step where helm apply is run
    bootstrapping = {
        "cluster": {
            "provider": None,
            "name": None,
            "region": None,
            "shortRegion": None,
            "baseDomain": None,
            "account": None,
            "endpoint": None,
        },
        "argoIamRole": None,
        "certificatesIamRole": None,
        "externalDnsIamRole": None,
        "awsComponents": {
            "awsEbsCsiDriverIamRole": None,
            "karpenter": {"iamRole": None, "instanceProfile": None},
        },
        "workloadComponents": {
            "tfyAgent": {
                "tenantName": None,
                "clusterToken": None,
                "controlPlaneUrl": None,
            }
        },
        "targetRepo": {
            "url": None,
            "branch": None,
            "path": None,
            "username": None,
            "password": None,
        },
        "monitoring": {
            "loki": {"bucketName": None, "roleArn": None},
            "prometheus": {"bucketName": None, "roleArn": None},
        },
        "controlPlaneComponents": {
            "controlPlaneUrl": None,
            "mlfoundry": {
                "enabled": False,
                "s3BucketName": None,
            },
            "mlmonitoring": {
                "enabled": False,
            },
            "servicefoundry": {
                "enabled": True,
                "s3BucketName": None,
            },
        },
    }

    def toJSON(self):
        return {"provisioning": self.provisioning, "bootstrapping": self.bootstrapping}


# TODO define logging level at the class entry point
class Infra:

    __target_repo_config = {
        "url": "github.com/truefoundry/ubermold-truefoundry.git",
        "branch": "truefoundry",
        "path": "base-ubermold",
        "username": None,
        "password": None,
    }

    __ubermold_manifest = {
        "apiVersion": "argoproj.io/v1alpha1",
        "kind": "Application",
        "metadata": {"name": "ubermold", "namespace": "argocd"},
        "spec": {
            "destination": {
                "namespace": "argocd",
                "server": "https://kubernetes.default.svc",
            },
            "project": "default",
            "source": {
                "plugin": {
                    "env": [
                        {"name": "RELEASE_NAME", "value": "ubermold"},
                        {"name": "VALUES_FILE", "value": "values.yaml"},
                    ],
                    "name": "secretsfoundry-plugin",
                },
                "path": "<path>",
                "repoURL": "<repo-url>",
                "targetRevision": "<target-revision>",
            },
            "syncPolicy": {
                "automated": {
                    "prune": True,
                },
                "syncOptions": ["CreateNamespace=true"],
            },
        },
    }

    __bootstrap_secrets = {
        "docker_image_pull_creds": None,
        "tekton_user_api_key": None,
    }

    __argo_repo_secrets = {
        "helm_repo_username": None,
        "helm_repo_password": None,
    }

    __base_repo_secrets = {
        "base_repo_username": None,
        "base_repo_password": None,
    }

    def __init__(self, dry_run):
        self.git_client = GitClient()
        self.dry_run = dry_run
        self.kubeconfig_location = None
        self.terragrunt_output_cache = {}

    def __confirm_val(self, v, tree_path, custom_handlers={}):
        if tree_path in custom_handlers:
            if not custom_handlers[tree_path]():
                return

        if v == None:
            v = questionary.text(f"Please Enter {tree_path} : ").ask()
        else:
            v = questionary.text(f"Please Enter {tree_path} : ", default=str(v)).ask()
        return v

    def __confirm_list_val(self, v, tree_path, custom_handlers={}):
        if tree_path in custom_handlers:
            if not custom_handlers[tree_path]():
                return

        temp_v = questionary.text(f"Please Enter {tree_path} : ", default=str(v)).ask()
        temp_v = str(temp_v).replace("'", '"')
        v = json.loads(temp_v)
        return v

    # TODO: add unit test for get_all_values function
    def __get_all_values(self, dicts, tree_path="", custom_handlers={}):
        if tree_path in custom_handlers:
            if not custom_handlers[tree_path]():
                return None
        if tree_path != "":
            tree_path += "."

        for k, v in dicts.items():
            if isinstance(v, dict):
                dicts[k] = self.__get_all_values(v, tree_path + k, custom_handlers)
            elif isinstance(v, list):
                if len(v) != 0 and isinstance(v[0], dict):
                    for i, vi in enumerate(v):
                        self.__get_all_values(
                            vi, tree_path + k + "[" + i + "]", custom_handlers
                        )
                else:
                    dicts[k] = self.__confirm_list_val(
                        v, tree_path + k, custom_handlers
                    )
            else:
                dicts[k] = self.__confirm_val(v, tree_path + k, custom_handlers)
        return dicts

    def __overwrite_file(self, src, dst):
        if os.path.isdir(dst):
            logger.warning(
                "file to be overwritten is a directory. removing the existing files"
            )
            shutil.rmtree(dst)

        shutil.copy(src, dst)

    def __execute_shell_command(self, command, ip=None):
        if self.dry_run:
            return
        logger.debug(f"executing command: {command}")
        try:
            p = subprocess.run(command, stdout=subprocess.PIPE, check=True, input=ip)
            return p.stdout.decode("UTF-8")
        except subprocess.CalledProcessError as err:
            raise Exception(f"failed to execute: {command}, error: {err}")

    def __execute_helm_command(self, args):
        return self.__execute_shell_command(
            [which("helm"), f"--kubeconfig={self.kubeconfig_location}", *args]
        )

    def __execute_kubectl_apply(self, manifest):
        return self.__execute_shell_command(
            [
                which("kubectl"),
                "apply",
                f"--kubeconfig={self.kubeconfig_location}",
                "-f",
                "-",
            ],
            ip=json.dumps(manifest).encode(),
        )

    def __provision_infra(
        self,
        base_repo: GitRepo,
        target_repo: GitRepo,
        config: InfraConfig,
        processed_config,
        target_repo_config,
    ):

        base_tf_config_path = os.path.join(
            base_repo.dir,
            "infra",
            config.provisioning["provider"],
            "clusters",
        )
        target_tf_config_path = os.path.join(
            target_repo.dir,
            target_repo_config["path"],
            config.provisioning["provider"],
            "clusters",
        )
        os.makedirs(target_tf_config_path, exist_ok=True)
        shutil.rmtree(target_tf_config_path)
        shutil.copytree(base_tf_config_path, target_tf_config_path)

        # Dumping values for state bucket
        with open(
            os.path.join(target_tf_config_path, "terragrunt_input.json"), "w"
        ) as terragrunt_input:
            terragrunt_input.write(
                json.dumps(processed_config["provisioning"]["state"])
            )

        # Dumping values for account
        orig_account_path = os.path.join(target_tf_config_path, "account")
        new_account_path = os.path.join(
            target_tf_config_path,
            config.provisioning["awsInputs"]["accountName"],
        )
        shutil.move(orig_account_path, new_account_path)
        with open(os.path.join(new_account_path, "account.json"), "w") as account_input:
            account_input.write(json.dumps(processed_config["provisioning"]["account"]))

        # Dumping values for region
        orig_region_path = os.path.join(new_account_path, "region")
        new_region_path = os.path.join(
            new_account_path,
            config.provisioning["awsInputs"]["region"],
        )
        shutil.move(orig_region_path, new_region_path)
        with open(os.path.join(new_region_path, "region.json"), "w") as region_input:
            region_input.write(json.dumps(processed_config["provisioning"]["region"]))

        # Dumping values for env
        orig_env_path = os.path.join(new_region_path, "cluster-prefix")
        new_env_path = os.path.join(
            new_region_path,
            config.provisioning["awsInputs"]["clusterPrefix"],
        )
        shutil.move(orig_env_path, new_env_path)
        with open(
            os.path.join(new_env_path, "infrastructure", "env_input.json"), "w"
        ) as env_input:
            env_input.write(json.dumps(processed_config["provisioning"]["env"]))

        shutil.rmtree(
            os.path.join(new_env_path, "infrastructure", "cluster-app-ctl-dbs")
        )

        if config.provisioning["awsInputs"]["externalNetworkConfig"]:
            shutil.rmtree(
                os.path.join(new_env_path, "infrastructure", "cluster-iam-certmanager")
            )
            shutil.rmtree(
                os.path.join(new_env_path, "infrastructure", "cluster-iam-external-dns")
            )
            shutil.rmtree(os.path.join(new_env_path, "infrastructure", "dns"))

        if not questionary.confirm(
            "Do you want to continue with infra creation: ", default=True
        ).ask():
            return
        # TODO: Create client for terragrunt. Abstract the shell command execution which can be reused by different dependencies.
        # A terragrunt repo which can cache the outputs for each module. This would reduce the number of output calls
        print(
            self.__execute_shell_command(
                [
                    which("terragrunt"),
                    "run-all",
                    "apply",
                    "--terragrunt-non-interactive",
                    f"--terragrunt-working-dir={new_env_path}",
                ]
            )
        )

    def __apply_bootstrapping_config(
        self,
        base_repo: GitRepo,
        target_repo: GitRepo,
        config: InfraConfig,
        processed_config,
        target_repo_config,
    ):
        base_ubermold_path = os.path.join(
            base_repo.dir,
            "k8s",
        )
        with open(os.path.join(base_ubermold_path, "values.yaml"), "w") as base_values:
            base_values.write(yaml.safe_dump(processed_config["ubermold"]))

        target_ubermold_path = os.path.join(
            target_repo.dir,
            target_repo_config["path"],
            config.provisioning["provider"],
            "clusters",
            config.provisioning["awsInputs"]["accountName"],
            config.provisioning["awsInputs"]["region"],
            config.provisioning["awsInputs"]["clusterPrefix"],
            "kubernetes",
        )
        current_dir = os.getcwd()
        os.chdir(target_repo.dir)
        os.makedirs(target_ubermold_path, exist_ok=True)

        self.__overwrite_file(
            os.path.join(base_ubermold_path, "Chart.yaml"),
            os.path.join(target_ubermold_path, "Chart.yaml"),
        )
        shutil.copytree(
            os.path.join(base_ubermold_path, "templates"),
            os.path.join(target_ubermold_path, "templates"),
        )
        self.__overwrite_file(
            os.path.join(base_ubermold_path, "values.yaml"),
            os.path.join(target_ubermold_path, "values.yaml"),
        )
        target_repo.commit_all_changes(None)
        os.chdir(current_dir)

        # ARGOCD
        # Adding the private repo
        argo_repo_secrets = self.__argo_repo_secrets
        self.__get_all_values(argo_repo_secrets)
        private_helm_repo_name = "private-helm-tf-apply"
        private_helm_repo_url = base64.b64decode(
            processed_config["secrets"][2]["data"]["url"]
        )
        # private_helm_repo_password = processed_config["secrets"][2]["data"]["password"]
        private_helm_repo_password = argo_repo_secrets["helm_repo_password"]

        repo_list_json = self.__execute_helm_command(["repo", "list", "-ojson"])
        repo_list = json.loads(repo_list_json)
        for repo in repo_list:
            if repo["name"] == private_helm_repo_name:
                print(f"{private_helm_repo_name} already exists, removing it...")
                print(
                    self.__execute_helm_command(
                        ["repo", "remove", private_helm_repo_name]
                    )
                )
                break

        print(
            self.__execute_helm_command(
                [
                    "repo",
                    "add",
                    private_helm_repo_name,
                    private_helm_repo_url,
                    "--username",
                    private_helm_repo_password,
                    "--password",
                    private_helm_repo_password,
                ]
            )
        )
        print(self.__execute_helm_command(["repo", "update", private_helm_repo_name]))

        # Installing argocd
        repo_server_annotation_key = '"eks\.amazonaws\.com/role-arn"'
        argocd_installation_args = [
            "upgrade",
            "--install",
            "--namespace",
            "argocd",
            "--create-namespace",
            "--set",
            'controller.enableStatefulSet="true"',
            "--set",
            'server.extraArgs="{--insecure}"',
            "--set",
            f'argo-cd.repoServer.serviceAccount.annotations.{repo_server_annotation_key}={config.bootstrapping["argoIamRole"]}',
            "--kubeconfig",
            self.kubeconfig_location,
            "argocd",
            "private-helm-tf-apply/argocd",
        ]
        print(self.__execute_helm_command(argocd_installation_args))
        print(self.__execute_helm_command(["repo", "remove", private_helm_repo_name]))

        # Connecting repos
        secrets = processed_config["secrets"]

        for secret in secrets:
            if secret["metadata"]["name"] == "argocd-private-helm-charts-creds":
                secret["data"]["username"] = self.__as_b64(private_helm_repo_password)
                secret["data"]["password"] = self.__as_b64(private_helm_repo_password)
            print(self.__execute_kubectl_apply(secret))

        ubermold_manifest = self.__ubermold_manifest

        ubermold_manifest["spec"]["source"]["path"] = config.bootstrapping[
            "targetRepo"
        ]["path"]
        ubermold_manifest["spec"]["source"]["repoURL"] = f"https://{target_repo.url}"
        ubermold_manifest["spec"]["source"]["targetRevision"] = target_repo.branch

        print(self.__execute_kubectl_apply(ubermold_manifest))

    def __as_b64(self, data: str) -> str:
        return base64.b64encode(data.encode(encoding="utf-8")).decode(encoding="utf-8")

    def __populate_bootstrapping_config(
        self, config: InfraConfig, target_repo_config, base_terragrunt_dir
    ):
        config.bootstrapping["cluster"]["account"] = config.provisioning["awsInputs"][
            "accountName"
        ]
        config.bootstrapping["cluster"]["provider"] = config.provisioning["provider"]
        config.bootstrapping["cluster"]["name"] = self.__fetch_terragrunt_output(
            os.path.join(base_terragrunt_dir, "cluster"), "cluster_id"
        )
        config.bootstrapping["cluster"]["region"] = config.provisioning["awsInputs"][
            "region"
        ]
        config.bootstrapping["cluster"]["shortRegion"] = config.provisioning[
            "awsInputs"
        ]["shortRegion"]
        config.bootstrapping["cluster"]["baseDomain"] = config.provisioning[
            "awsInputs"
        ]["baseDomain"]
        config.bootstrapping["cluster"]["endpoint"] = self.__fetch_terragrunt_output(
            os.path.join(base_terragrunt_dir, "cluster"), "cluster_endpoint"
        )

        config.bootstrapping["argoIamRole"] = self.__fetch_terragrunt_output(
            os.path.join(base_terragrunt_dir, "cluster-app-argocd"),
            "argocd_iam_role_arn",
        )
        if not config.provisioning["awsInputs"]["externalNetworkConfig"]:
            config.bootstrapping[
                "certificatesIamRole"
            ] = self.__fetch_terragrunt_output(
                os.path.join(base_terragrunt_dir, "cluster-iam-certmanager"),
                "iam_role_arn",
            )
            config.bootstrapping["externalDnsIamRole"] = self.__fetch_terragrunt_output(
                os.path.join(base_terragrunt_dir, "cluster-iam-external-dns"),
                "iam_role_arn",
            )
        else:
            config.bootstrapping["certificatesIamRole"] = ""
            config.bootstrapping["externalDnsIamRole"] = ""
        config.bootstrapping["awsComponents"][
            "awsEbsCsiDriverIamRole"
        ] = self.__fetch_terragrunt_output(
            os.path.join(base_terragrunt_dir, "cluster-iam-csi-ebs"), "iam_role_arn"
        )
        config.bootstrapping["awsComponents"]["karpenter"][
            "iamRole"
        ] = self.__fetch_terragrunt_output(
            os.path.join(base_terragrunt_dir, "cluster-iam-karpenter"), "iam_role_arn"
        )
        config.bootstrapping["awsComponents"]["karpenter"][
            "instanceProfile"
        ] = self.__fetch_terragrunt_output(
            os.path.join(base_terragrunt_dir, "cluster-iam-karpenter"),
            "iam_instance_profile_id",
        )
        install_workload = questionary.confirm(
            "Do you want to install workload components as well?", default=False
        ).ask()
        if install_workload:
            config.bootstrapping["workloadComponents"]["tfyAgent"][
                "tenantName"
            ] = questionary.text("Tenant name").ask()
            config.bootstrapping["workloadComponents"]["tfyAgent"][
                "clusterToken"
            ] = questionary.text("Cluster token").ask()
            config.bootstrapping["workloadComponents"]["tfyAgent"][
                "controlPlaneUrl"
            ] = questionary.text("Control plane url").ask()
        else:
            config.bootstrapping["workloadComponents"] = None

        install_control_plane = questionary.confirm(
            "Do you want to install control plane components as well?", default=False
        ).ask()
        if install_control_plane:
            config.bootstrapping["controlPlaneComponents"][
                "controlPlaneUrl"
            ] = questionary.text("Control plane url").ask()
            config.bootstrapping["controlPlaneComponents"]["mlfoundry"][
                "enabled"
            ] = questionary.confirm(
                "Do you want to install mlfoundry", default=False
            ).ask()
            if config.bootstrapping["controlPlaneComponents"]["mlfoundry"]["enabled"]:
                config.bootstrapping["controlPlaneComponents"]["mlfoundry"][
                    "s3BucketName"
                ] = self.__fetch_terragrunt_output(
                    os.path.join(base_terragrunt_dir, "truefoundry-aws"),
                    "mlfoundry_bucket_id",
                )
            config.bootstrapping["controlPlaneComponents"]["mlmonitoring"][
                "enabled"
            ] = questionary.confirm(
                "Do you want to install mlmonitoring", default=False
            ).ask()
            config.bootstrapping["controlPlaneComponents"]["servicefoundry"][
                "enabled"
            ] = questionary.confirm(
                "Do you want to install servicefoundry", default=False
            ).ask()
            if config.bootstrapping["controlPlaneComponents"]["servicefoundry"][
                "enabled"
            ]:
                config.bootstrapping["controlPlaneComponents"]["servicefoundry"][
                    "s3BucketName"
                ] = self.__fetch_terragrunt_output(
                    os.path.join(base_terragrunt_dir, "truefoundry-aws"),
                    "svcfoundry_bucket_id",
                )
            else:
                config.bootstrapping["controlPlaneComponents"]["servicefoundry"] = None
        else:
            config.bootstrapping["controlPlaneComponents"] = None

        config.bootstrapping["targetRepo"] = target_repo_config

        install_monitoring = questionary.confirm(
            "Do you want to install monitoring as well?", default=False
        ).ask()
        if install_monitoring:
            config.bootstrapping["monitoring"]["loki"][
                "bucketName"
            ] = self.__fetch_terragrunt_output(
                os.path.join(base_terragrunt_dir, "cluster-app-loki"),
                "loki_bucket_name",
            )
            config.bootstrapping["monitoring"]["loki"][
                "roleArn"
            ] = self.__fetch_terragrunt_output(
                os.path.join(base_terragrunt_dir, "cluster-app-loki"), "iam_role_arn"
            )
            config.bootstrapping["monitoring"]["prometheus"][
                "bucketName"
            ] = self.__fetch_terragrunt_output(
                os.path.join(base_terragrunt_dir, "cluster-app-thanos"),
                "thanos_bucket_name",
            )
            config.bootstrapping["monitoring"]["prometheus"][
                "roleArn"
            ] = self.__fetch_terragrunt_output(
                os.path.join(base_terragrunt_dir, "cluster-app-thanos"), "iam_role_arn"
            )
        else:
            config.bootstrapping["monitoring"] = None

    def __validate_dependencies(self):
        if not which("kubectl"):
            raise Exception("kubectl not found")

        if not which("aws"):
            raise Exception("aws not found")

        if not which("helm"):
            raise Exception("helm not found")

        if not which("git"):
            raise Exception("git not found")

        if not which("terraform"):
            raise Exception("terraform not found")

        if not which("terragrunt"):
            raise Exception("terragrunt not found")

    def __fetch_terragrunt_output(self, dir, path):
        if dir in self.terragrunt_output_cache:
            return self.terragrunt_output_cache[dir][path]["value"]

        current_dir = os.getcwd()
        os.chdir(dir)
        v = self.__execute_shell_command(["terragrunt", "output", "--json"])
        os.chdir(current_dir)

        self.terragrunt_output_cache[dir] = json.loads(v)
        return self.terragrunt_output_cache[dir][path]["value"]

    def __populate_kubeconfig(self, cluster_name, aws_profile, region) -> str:
        self.kubeconfig_location = os.path.join(os.getcwd(), "kubeconfig-test")
        self.__execute_shell_command(
            [
                which("aws"),
                "eks",
                "update-kubeconfig",
                "--name",
                cluster_name,
                "--profile",
                aws_profile,
                "--region",
                region,
                "--kubeconfig",
                self.kubeconfig_location,
            ]
        )

    def __bootstrap_infra_secrets(self, aws_profile, aws_region, processed_config):
        self.__get_all_values(self.__bootstrap_secrets)
        for k, v in self.__bootstrap_secrets.items():
            self.__execute_shell_command(
                [
                    which("aws"),
                    "ssm",
                    "put-parameter",
                    f'--name={processed_config["provisioning"]["bootstrapSecrets"][k]["ssm_path"]}',
                    "--overwrite",
                    f"--value={v}",
                    "--type=SecureString",
                    f"--profile={aws_profile}",
                    f"--region={aws_region}",
                ]
            )

    def __externalConfigHandler(self):
        return questionary.confirm(
            f"Do you want to attach your own network: ", default=False
        ).ask()

    def __provision_aws(self):
        ubermold_clones_dir = os.path.join(tempfile.mkdtemp(), "ubermold-clones")
        logger.info(f"Will use {ubermold_clones_dir} for cloning")
        try:
            config = InfraConfig()
            config.provisioning["provider"] = "aws"
            target_repo_config = self.__get_all_values(self.__target_repo_config)
            logger.info(f"Values for target repo read: {target_repo_config}")

            self.__get_all_values(
                config.provisioning["awsInputs"],
                custom_handlers={"externalNetworkConfig": self.__externalConfigHandler},
            )
            logger.info(
                f'Values for aws inputs read: {config.provisioning["awsInputs"]}'
            )

            config_json = config.toJSON()
            config_json["bootstrapping"] = None
            processed_config = ServiceFoundryServiceClient().process_infra(config_json)[
                "manifest"
            ]
            logger.info(f"Received processed provisioning config: {processed_config}")

            self.__bootstrap_infra_secrets(
                config.provisioning["awsInputs"]["awsProfile"],
                config.provisioning["awsInputs"]["region"],
                processed_config,
            )
            logger.info(f"Created infra secrets in ssm")

            base_repo_secrets = self.__base_repo_secrets
            self.__get_all_values(base_repo_secrets)

            base_tf_repo = self.git_client.clone_repo(
                processed_config["baseUbermold"]["url"],
                os.path.join(ubermold_clones_dir, "ubermold"),
                processed_config["baseUbermold"]["branch"],
                username=base_repo_secrets["base_repo_username"],
                password=base_repo_secrets["base_repo_password"],
            )
            logger.info(f"Cloned base ubermold in {base_tf_repo.dir}")

            target_tf_repo = self.git_client.clone_repo(
                target_repo_config["url"],
                os.path.join(ubermold_clones_dir, "target-ubermold"),
                target_repo_config["branch"],
                username=target_repo_config["username"],
                password=target_repo_config["password"],
            )
            logger.info(f"Cloned target ubermold in {target_tf_repo.dir}")

            self.__provision_infra(
                base_tf_repo,
                target_tf_repo,
                config,
                processed_config,
                target_repo_config,
            )
            logger.info(f"Terragrunt infra provisioning done")

            base_terragrunt_dir = os.path.join(
                target_tf_repo.dir,
                target_repo_config["path"],
                config.provisioning["provider"],
                "clusters",
                config.provisioning["awsInputs"]["accountName"],
                config.provisioning["awsInputs"]["region"],
                config.provisioning["awsInputs"]["clusterPrefix"],
                "infrastructure",
            )
            self.__populate_bootstrapping_config(
                config,
                target_repo_config,
                base_terragrunt_dir,
            )
            logger.info(f"Bootstrapping config populated: {config.bootstrapping}")

            processed_config = ServiceFoundryServiceClient().process_infra(
                config.toJSON()
            )["manifest"]
            logger.info(
                f"Processed bootstrapping config received from sfy: {processed_config}"
            )
            self.__populate_kubeconfig(
                self.__fetch_terragrunt_output(
                    os.path.join(base_terragrunt_dir, "cluster"), "cluster_id"
                ),
                config.provisioning["awsInputs"]["awsProfile"],
                config.provisioning["awsInputs"]["region"],
            )
            logger.info(f"kube config created at: {self.kubeconfig_location}")

            self.__apply_bootstrapping_config(
                base_tf_repo,
                target_tf_repo,
                config,
                processed_config,
                target_repo_config,
            )
            logger.info(f"Cluster bootstrapping done")

        finally:
            if os.path.isdir(ubermold_clones_dir):
                shutil.rmtree(ubermold_clones_dir)
                # pass

    def provision(self):
        self.__validate_dependencies()
        provider = questionary.select(
            "Please select your provider: ", choices=["aws"]
        ).ask()
        if provider == "aws":
            self.__provision_aws()
        else:
            raise Exception(f"{provider} provider is not supported")
