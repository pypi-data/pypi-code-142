# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['isolate_controller',
 'isolate_controller.definitions',
 'isolate_controller.scheduler']

package_data = \
{'': ['*']}

install_requires = \
['dill==0.3.5.1',
 'google-cloud-storage>=2.6.0,<3.0.0',
 'grpcio>=1.49',
 'isolate==0.5.0',
 'kubernetes-asyncio>=24.2.2,<25.0.0',
 'kubernetes>=25.3.0,<26.0.0',
 'protobuf',
 'psycopg>=3.1.4,<4.0.0',
 'redis>=4.3.4,<5.0.0',
 'typing-extensions>=4.4.0,<5.0.0']

setup_kwargs = {
    'name': 'isolate-controller',
    'version': '0.0.1a0',
    'description': 'Managed isolated environments for Python',
    'long_description': "# fal-isolate-cloud\n\n## Regenerating gRPC definitions\n\n- Ensure you are on Python 3.9 or higher\n- From the root directory execute the following commands:\n\n```sh\n$ pip install grpcio_tools mypy-protobuf refactor\n$ python tools/regen_grpc.py src/isolate_controller/definitions/controller.proto\n```\n\n## Building the images\n\n- From the root directory\n\n```sh\n$ docker build -f infra/worker/Dockerfile -t isolate-cloud-worker .\n$ docker build -f infra/controller/Dockerfile -t isolate-cloud-controller .\n```\n\n## Testing the server (locally)\n\n- Assuming you built the image `isolate-cloud-worker`, try the following setup:\n\n```sh\n$ docker run --rm -e CONTROLLER_KEY=local_secret -p 50001:50001 isolate-cloud-worker\n$ ISOLATE_TEST_MODE=1 python -m isolate_controller.server\n# CHANGE THE IP FIRST\n$ python test_script.py\n```\n\n## Setting kubectl with the GCP cluster\n\n- Install the GKE plugin if you don't have it\n- Get the clusters list\n\n```sh\n$ gcloud components install gke-gcloud-auth-plugin\n$ gcloud container clusters get-credentials <cluster-name> --zone <your-zone>\n$ kubectl get pods -A\n# should print kube-system pods\n```\n\n## Deploying\n\n### Deploying the worker\n\n```sh\n$ gcloud builds submit --config=infra/worker/cloudbuild.yml .\n```\n\n### Deploying the controller\n\n```sh\n$ export PROJECT_ID=$(gcloud config list --format 'value(core.project)' 2>/dev/null)\n$ gcloud builds submit --config=infra/controller/cloudbuild.yml .\n$ export IMAGE_SHA=$(python tools/update_images.py)\n$ envsubst < infra/controller/controller.yml | kubectl apply -f -\n# Run this just once to expose the service:\n$ kubectl expose deployment fal-isolate-controller --type=LoadBalancer --name=load-balancer\n```\n\n### Connect redis\n\nMake sure to do this when you are setting up the first time\n\nhttps://cloud.google.com/memorystore/docs/redis/connect-redis-instance#connecting-cluster\n\n```sh\n$ gcloud redis instances list --region=us-central1\n# Take note of the HOST value\n$ export REDISHOST_IP=...\n```\n\n```sh\n$ export REDISHOST_IP=...\n$ git clone https://github.com/bowei/k8s-custom-iptables.git\n$ cd k8s-custom-iptables/\n$ TARGETS=${REDISHOST_IP} ./install.sh\n```\n\n```sh\n$ export REDISHOST_IP=...\n$ kubectl create configmap redishost --from-literal=REDISHOST=${REDISHOST_IP}\n```\n\n### Setup NFS cache\n\nMake sure to do this when you are setting up the first time\n\n```sh\n$ gcloud filestore instances list\n# Take note of the IP_ADDRESS\n$ export NFS_SERVER_IP=...\n```\n\n```sh\n$ export NFS_SERVER_IP=...\n$ envsubst < infra/fileserver/nfs-server.yml | kubectl apply -f -\n$ kubectl apply -f infra/fileserver/claim.yml\n```\n\n### Bind Google Service Account to Kubernetes Service Account\n\nMake sure to do this when you are setting up the first time\n\nThis is necessary to [connect Postgres](#connect-postgres)\n\n```sh\n$ kubectl annotate serviceaccount default iam.gke.io/gcp-service-account=gke-service-account@${PROJECT_ID}.iam.gserviceaccount.com\n```\n\n### Connect Postgres\n\nMake sure to do this when you are setting up the first time\n\n```sh\n# xargs to remove extra quotes\n$ cd fal_terraform/environments/<environment>\n$ export SQITCH_PASSWORD=$(terraform output isolate_cloud_sql_user_server_password | xargs)\n$ kubectl create secret generic sqlaccess \\\n    --from-literal=SQL_DBNAME=users \\\n    --from-literal=SQL_USER=gke_service \\\n    --from-literal=SQL_PASSWORD=$SQITCH_PASSWORD\n```\n\n#### Apply Postgres migrations\n\nDownload CLI tool [sqitch](https://sqitch.org/download/)\n\nDownload the [Cloud SQL Auth Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy#install)\n\nRun the `cloud_sql_proxy` binary to connect to the Cloud SQL instance as a local connection:\n\n```sh\n# Notice the PORT is 5433 to differ from the default 5432 of Postgres\n$ ./cloud_sql_proxy -instances=${PROJECT_ID}:us-central1:isolate-cloud=tcp:0.0.0.0:5433\n```\n\nIn another shell, run the migrations\n\n```sh\n# xargs to remove extra quotes\n$ export SQITCH_PASSWORD=$(terraform output isolate_cloud_sql_user_server_password | xargs)\n$ cd fal-isolate-cloud/db\n$ sqitch deploy --verify cloud-proxy\n#   Adding registry tables to cloud-proxy\n#   Deploying changes to cloud-proxy\n#     + create_table_jobs .. ok\n```\n\nAnd close (`CTRL-C`) the close_sql_proxy process.\n",
    'author': 'Features & Labels',
    'author_email': 'hello@fal.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
