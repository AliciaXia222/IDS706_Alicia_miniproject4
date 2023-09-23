"""
Test goes here

"""


from main import rows, columns
import pandas as pd

example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-age/congress-terms.csv"


if __name__ == "__main__":

    test_main()


def test_main():
    assert rows == 266
    assert columns == 67
