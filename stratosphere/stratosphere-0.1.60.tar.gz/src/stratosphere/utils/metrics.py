from stratosphere.run import Run
from stratosphere.utils.assertions import assert_df, assert_keys


def eval_metrics(run: Run):
    run.verify(assert_df(name="fields", key="predictions", columns=["y_true", "y_pred"]))

    metrics = {"accuracy": (run.fields["predictions"]["y_true"] == run.fields["predictions"]["y_pred"]).mean()}

    run.fields["metrics"] = metrics
