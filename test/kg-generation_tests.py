# -*- coding: utf-8 -*-import io
import unittest
import unittest.mock

import pandas as pd
from example_cookiecutter.utils.process import (
    get_mean,
    normalize,
    process_incomes,
    remove_nulls,
)

# https://docs.python.org/3/library/unittest.html


class MyTests(unittest.TestCase):
    """MyTest."""

    def test_process_incomes(self):
        """Comprobar operacionesde transformación."""
        df = pd.DataFrame(
            {"Incomes": [10, 10, 20, 20, 10], "Cost": [5, 2, 5, 5, 2]}
        )
        expected_values = [20, 20, 40, 40, 20]
        incomes_df = process_incomes(df)
        self.assertListEqual(list(incomes_df["Incomes"]), expected_values)

    def test_remove_nulls(self):
        """Comprobar nulos."""
        df = pd.DataFrame(
            {"Incomes": [10, 10, 20, None, 10], "Cost": [5, 2, 5, 5, 2]}
        )
        expected_values = [10, 10, 20, 10]
        remove_nulls_df = remove_nulls(df)
        self.assertListEqual(list(remove_nulls_df["Incomes"]), expected_values)

    def test_mean(self):
        """Comprobar media."""
        df = pd.DataFrame(
            {"Incomes": [10, 10, 20, None, 10], "Cost": [5, 2, 5, 5, 2]}
        )
        expected_values = 12.5
        mean_incomes = get_mean(df)
        self.assertEquals(mean_incomes, expected_values)

    def test_normalize_mock(self):
        """Aplicar mocks."""
        df = pd.DataFrame({"Incomes": [10, 10, 20, 10], "Cost": [5, 2, 5, 2]})

        with unittest.mock.patch(
            "example_cookiecutter.utils.process.get_constant"
        ) as constant:
            constant.return_value = 10

            expected_values = [100.0, 100.0, 200.0, 100.0]
            normalized_df = normalize(df)

            self.assertListEqual(
                list(normalized_df["Incomes"]), expected_values
            )


if __name__ == "__main__":
    unittest.main()
