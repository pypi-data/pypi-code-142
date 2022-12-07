from azureml.core import Workspace, Environment
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core import Experiment
from azureml.train.estimator import Estimator
import click, os, time, re
from azureml.exceptions._azureml_exception import ProjectSystemException

def get_ssh_keys():
    from cryptography.hazmat.primitives import serialization as crypto_serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.backends import default_backend as crypto_default_backend
    dir_path = os.path.join(os.getcwd(), ".ssh")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    pub_key_file = os.path.join(dir_path, "key.pub")
    pri_key_file = os.path.join(dir_path, "key")
    keys_exist = True
    if not os.path.exists(pub_key_file):
        print("Public SSH key does not exist!")
        keys_exist = False
    if not os.path.exists(pri_key_file):
        print("Private SSH key does not exist!")
        keys_exist = False
    if not keys_exist:
        key = rsa.generate_private_key(
            backend=crypto_default_backend(), public_exponent=65537, key_size=2048
        )
        private_key = key.private_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PrivateFormat.PKCS8,
            crypto_serialization.NoEncryption(),
        )
        public_key = key.public_key().public_bytes(
            crypto_serialization.Encoding.OpenSSH,
            crypto_serialization.PublicFormat.OpenSSH,
        )
        with open(pub_key_file, "wb") as f:
            f.write(public_key)
        with open(pri_key_file, "wb") as f:
            f.write(private_key)
        os.chmod(pri_key_file, 0o600)
    with open(pub_key_file, "r") as f:
        pubkey = f.read()
    return pubkey, pri_key_file

def createOrGetComputeTarget(
    ws, ct_name, vm_name, vm_priority, ssh_key_pub,min_nodes,max_nodes,idle_seconds,username
):
    config = AmlCompute.provisioning_configuration(
        vm_size=vm_name,
        min_nodes=min_nodes,
        max_nodes=max_nodes,
        vm_priority=vm_priority,
        idle_seconds_before_scaledown=idle_seconds,
        admin_username=username,
        admin_user_ssh_key=ssh_key_pub,
        remote_login_port_public_access="Enabled",
    )
    ct = ComputeTarget.create(ws, ct_name, config)
    ct.wait_for_completion(show_output=True)
    return ct

def createOrGetEnvironment(ws, env_name):
    environment_name = env_name
    python_interpreter = "/opt/miniconda/bin/python"
    conda_packages = ["matplotlib","jupyterlab"]
    ### CREATE OR RETRIEVE THE ENVIRONMENT
    if environment_name not in ws.environments:
        env = Environment(name=environment_name)
        env.docker.enabled = True
        env.docker.base_image = None
        env.docker.base_dockerfile = 'FROM mcr.microsoft.com/azureml/openmpi4.1.0-cuda11.1-cudnn8-ubuntu18.04\n RUN conda install -c r -y pip=20.1.1 && \\\n pip install jupyterlab && \\\n pip install nvidia-pyindex && \\\n pip install nvidia-tao'
        env.python.interpreter_path = python_interpreter
        env.python.user_managed_dependencies = True
        env.environment_variables = {"AZUREML_COMPUTE_USE_COMMON_RUNTIME":"false"}
        conda_dep = CondaDependencies()
        for conda_package in conda_packages:
            conda_dep.add_conda_package(conda_package)
        env.python.conda_dependencies = conda_dep
        env.register(workspace=ws)
    else:
        env = ws.environments[environment_name]
    return env

def setup_port_forwarding(run,ct,username):
    jupyter_address = run.get_metrics()["jupyter"]
    headnode_ip = run.get_metrics()["jupyter"].split(":")[0]
    headnode_public_ip = ct.list_nodes()[0]["publicIpAddress"]
    headnode_public_port = ct.list_nodes()[0]["port"]
    print("headnode_public_ip: {}".format(headnode_public_ip))
    print("headnode_public_port: {}".format(headnode_public_port))
    cmd = (
        "ssh -vvv -o StrictHostKeyChecking=no -N"
        f" -i {os.path.expanduser(self.admin_ssh_key)}"
        f" -L 0.0.0.0:{self.jupyter_port}:{headnode_ip}:8888"
    )
    cmd += f" {username}@{headnode_public_ip} -p {headnode_public_port}"
    portforward_proc = subprocess.Popen(
        cmd.split(),
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    #### Starting thread to keep the SSH tunnel open on Windows
    #self.portforward_logg = port_forward_logger(self.portforward_proc)
    #self.portforward_logg.start()

def get_jupyter_link(ws,run,jupyter_port):
    hostname = "localhost"
    location = ws.get_details()["location"]
    token = run.get_metrics()["token"]
    jupyter_url = f"http://{hostname}:{jupyter_port}/?token={token}"
    return jupyter_url

def setUpJupyterLab(ws,ct, env,exp_name,script_params,username,path,tags,jupyter_port):
    exp = Experiment(ws, exp_name)
    estimator = Estimator(path,
        compute_target=ct,
        entry_script="start_jupyter.py",
        environment_definition=env,
        script_params=script_params,
        node_count=1,  ### start only scheduler
        use_docker=True,
    )
    run = exp.submit(estimator, tags=tags)
    print("Waiting for compute cluster's IP")
    while (
        run.get_status() != "Canceled"
        and run.get_status() != "Failed"
        and "jupyter"
        not in run.get_metrics()  # and "scheduler" not in run.get_metrics()
    ):
        print(".", end="")
        time.sleep(5)
    if run.get_status() == "Canceled" or run.get_status() == "Failed":
        print("Failed to start the AzureML Compute Cluster")
        raise Exception("Failed to start the AzureML Compute Cluster.")
    print()
    print("Jupyter session is running...")
    print("\n\n")
    setup_port_forwarding(run,ct,username)
    jupyter_link = get_jupyter_link(ws,run,jupyter_port)
    print("Connections established")
    return run,jupyter_link

