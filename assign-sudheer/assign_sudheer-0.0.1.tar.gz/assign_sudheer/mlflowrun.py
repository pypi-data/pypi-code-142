import mlflow
import mlflow.sklearn

from ingest_data import data_ingest
from score import score
from train import train

remote_server_uri = "http://localhost:5000"
mlflow.set_tracking_uri(remote_server_uri)
exp_name = "House_Price_Prediction"
mlflow.set_experiment(exp_name)
with mlflow.start_run(
    run_name="House Price Prediction",
) as run:
    data_ingest()
    train()
    score()
