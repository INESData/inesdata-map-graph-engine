# -*- coding: utf-8 -*-

import random
from pandas import DataFrame


def process_incomes(df: DataFrame) -> DataFrame:
    """Process_incomes.

    Args:
        df (DataFrame): input df

    Returns: DataFrame

    """
    df["Incomes"] = df["Incomes"] * 2
    return df


def remove_nulls(df: DataFrame) -> DataFrame:
    """Remove_nulls.

    Args:
        df (DataFrame): input df

    Returns: DataFrame

    """
    df.dropna(subset=["Incomes"], inplace=True)
    return df


def get_mean(df: DataFrame) -> DataFrame:
    """Get_mean.

    Args:
        df (DataFrame): input df

    Returns: DataFrame

    """
    return df["Incomes"].mean()


def get_constant() -> int:
    """Get_constant.

    Returns: constant

    """
    cte = random.randint(0, 9)
    return cte


def normalize(df: DataFrame) -> DataFrame:
    """Normalize.

    Args:
        df (DataFrame): input df

    Returns: DataFrame

    """
    normalized_df = df * get_constant()
    return normalized_df
