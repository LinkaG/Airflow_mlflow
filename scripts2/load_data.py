from sklearn import datasets
import pandas as pd
import numpy as np
import click


@click.command()
@click.option("--output_path", help="Path")
def load_data(output_path):
    """ Function load init dataset.
    :param output_path: Path to save DataFrame
    :return:
    """
    iris = datasets.load_iris()
    iris_df = pd.DataFrame(
        data=np.c_[iris['data'], iris['target']],
        columns=iris['feature_names'] + ['target']
    )
    iris_df.to_csv(output_path, index=False)


if __name__ == "__main__":
    load_data()
