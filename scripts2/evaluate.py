import joblib
import click
from sklearn import metrics
import pandas as pd
from ruamel.yaml import YAML
import mlflow


@click.command()
@click.option("--input_path_data", help="Path")
@click.option("--input_path_label", help="Path")
@click.option("--model_path", help="Path")
def evaluate(input_path_data: str, input_path_label: str, model_path: str):
    """ Function to evaluate model
    :param input_path_data: Path to test data
    :param input_path_label: Path to test labels
    :param model_path: Path to model file
    :param output_path: Path to metrics file
    :return:
    """

    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("logreg classifier")
    mlflow.start_run(run_name="test_logreg")

    yaml = YAML(typ="safe")
    params = yaml.load(open("/home/zalina/xflow/params.yaml", encoding="utf-8"))['model']['params']

    x_test = pd.read_csv(input_path_data)
    y_test = pd.read_csv(input_path_label)
    clf = joblib.load(model_path)
    y_pred = clf.predict(x_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)

    score = dict(
        accuracy=float(accuracy)
    )


    mlflow.log_params(params)
    mlflow.log_metrics(score)


if __name__ == "__main__":
    evaluate()
