"""
Test goes here

"""


from main import rows, columns
from main import (
    report_population,
    generate_summary,
)
import pandas as pd

example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-age/congress-terms.csv"


def test_generate_summary_report():
    """Function calling generate_summary() and generate_summary_iris()"""
    generate_summary(example_csv)
    report_population()


if __name__ == "__main__":

    test_main()


def test_main():
    assert rows == 266
    assert columns == 67
