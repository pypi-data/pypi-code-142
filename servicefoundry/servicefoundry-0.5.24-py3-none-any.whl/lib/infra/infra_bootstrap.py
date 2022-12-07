import base64
import json
import os
import shutil
import tempfile
from shutil import which

import questionary
import yaml

from servicefoundry.lib.clients.git_client import GitClient, GitRepo
from servicefoundry.lib.clients.service_foundry_client import (
    ServiceFoundryServiceClient,
)
from servicefoundry.lib.clients.shell_client import Shell
from servicefoundry.lib.clients.terragrunt_client import Terragrunt
from servicefoundry.lib.config.config_manager import ConfigManager
from servicefoundry.lib.config.dict_questionaire import DictQuestionaire
from servicefoundry.lib.config.infra_config import InfraConfig
from servicefoundry.logger import logger


# TODO define logging level at the class entry point
class Infra:
    __target_repo_config = {
        "url": "",
        "branch": "main",
        "path": "",
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

    __tfy_creds = {
        "token": None,
    }

    def __init__(self, dry_run):
        self.git_client = GitClient()
        self.dry_run = dry_run
        self.kubeconfig_location = None
        self.terragrunt_output_cache = {}
        self.terragrunt_client = Terragrunt()

    def __overwrite_file(self, src, dst):
        if os.path.isdir(dst):
            logger.warning(
                "file to be overwritten is a directory. removing the existing files"
            )
            shutil.rmtree(dst)

        shutil.copy(src, dst)

    def __execute_helm_command(self, args):
        return Shell().execute_shell_command(
            [which("helm"), f"--kubeconfig={self.kubeconfig_location}", *args]
        )

    def __execute_kubectl_apply(self, manifest):
        return Shell().execute_shell_command(
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
        self.terragrunt_client.apply_all(new_env_path)

    def __apply_bootstrapping_config(
        self,
        base_repo: GitRepo,
        target_repo: GitRepo,
        config: InfraConfig,
        processed_config,
        target_repo_config,
        tfy_creds,
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
        private_helm_repo_name = "private-helm-tf-apply"
        private_helm_repo_url = base64.b64decode(
            processed_config["secrets"][2]["data"]["url"]
        )
        # private_helm_repo_password = processed_config["secrets"][2]["data"]["password"]
        private_helm_repo_token = tfy_creds["token"]

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
                    private_helm_repo_token,
                    "--password",
                    private_helm_repo_token,
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
                secret["data"]["username"] = self.__as_b64(private_helm_repo_token)
                secret["data"]["password"] = self.__as_b64(private_helm_repo_token)
            print(self.__execute_kubectl_apply(secret))

        ubermold_manifest = self.__ubermold_manifest

        ubermold_manifest["spec"]["source"]["path"] = os.path.join(
            target_repo_config["path"],
            config.provisioning["provider"],
            "clusters",
            config.provisioning["awsInputs"]["accountName"],
            config.provisioning["awsInputs"]["region"],
            config.provisioning["awsInputs"]["clusterPrefix"],
            "kubernetes",
        )
        ubermold_manifest["spec"]["source"]["repoURL"] = f"https://{target_repo.url}"
        ubermold_manifest["spec"]["source"]["targetRevision"] = target_repo.branch

        print(self.__execute_kubectl_apply(ubermold_manifest))

    def __as_b64(self, data: str) -> str:
        return base64.b64encode(data.encode(encoding="utf-8")).decode(encoding="utf-8")

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

    def __populate_kubeconfig(self, cluster_name, aws_profile, region) -> str:
        self.kubeconfig_location = os.path.join(os.getcwd(), "kubeconfig-test")
        Shell().execute_shell_command(
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
        bootstrap_secrets = self.__bootstrap_secrets
        bootstrap_secrets["docker_image_pull_creds"] = questionary.password(
            "Please enter the base64 encoded secret for pulling truefoundry images:"
        ).ask()
        bootstrap_secrets["tekton_user_api_key"] = questionary.password(
            "Please enter the api key for servicefoundry:"
        ).ask()
        for k, v in self.__bootstrap_secrets.items():
            Shell().execute_shell_command(
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

    def __provision_aws(self):
        ubermold_clones_dir = os.path.join(tempfile.mkdtemp(), "ubermold-clones")
        logger.info(f"Will use {ubermold_clones_dir} for cloning")
        try:

            import pdb

            pdb.set_trace()
            target_repo_config = (
                DictQuestionaire(
                    ConfigManager().get_config(ConfigManager.TARGET_REPO_CONFIG)
                ).ask()
                if ConfigManager().get_config(ConfigManager.TARGET_REPO_CONFIG)
                else DictQuestionaire(self.__target_repo_config).ask()
            )
            ConfigManager().save_config(
                ConfigManager.TARGET_REPO_CONFIG, target_repo_config
            )
            logger.info(f"Values for target repo read: {target_repo_config}")

            config = InfraConfig(self.terragrunt_client)
            config.populate_provisioning_config("aws")
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

            tfy_creds = self.__tfy_creds
            tfy_creds["token"] = questionary.password(
                "Please enter the token for truefoundry repos"
            ).ask()

            base_tf_repo = self.git_client.clone_repo(
                processed_config["baseUbermold"]["url"],
                os.path.join(ubermold_clones_dir, "ubermold"),
                processed_config["baseUbermold"]["branch"],
                username=tfy_creds["token"],
                password=tfy_creds["token"],
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
            config.populate_bootstrapping_config(
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
                self.terragrunt_client.fetch_terragrunt_output(
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
                tfy_creds,
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
