from typing import List, Union
import pandas as pd


def create_grouped_describe(
    df: pd.DataFrame,
    group_columns: Union[str, List[str]],
    describe_columns: Union[str, List[str]],
    total_group: str = "TotalGroup",
) -> pd.DataFrame:
    """
    Create a summary statistics table

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame to analyze
    group_columns : str or List[str]
        Column(s) to group by
    describe_columns : str or List[str]
        Column(s) to calculate descriptive statistics for

    Returns
    -------
    pd.DataFrame
        A DataFrame containing descriptive statistics for each group and the total.
    """  # noqa: E501

    # Convert string inputs to lists
    if isinstance(group_columns, str):
        group_columns = [group_columns]
    if isinstance(describe_columns, str):
        describe_columns = [describe_columns]

    # Calculate group statistics
    group_stats = df.groupby(group_columns)[describe_columns].describe().T

    # Calculate overall statistics - convert to DataFrame first then stack
    total_stats_df = df[describe_columns].describe()
    total_stats = pd.DataFrame(total_stats_df.stack(), columns=[total_group])

    # Reorder index levels
    total_stats.index = pd.MultiIndex.from_tuples(
        [(col, stat) for stat, col in total_stats.index]
    )
    total_stats = total_stats.sort_index()

    # Set consistent index names
    total_stats.index.set_names(["column", "stat"], inplace=True)
    group_stats.index.set_names(["column", "stat"], inplace=True)

    # Combine group and total statistics
    result = pd.concat([group_stats, total_stats], axis=1)
    result.columns.name = (
        tuple(group_columns) if len(group_columns) > 1 else group_columns[0]
    )

    return result
