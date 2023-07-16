""" 
Purpose: Provide reactive output for the Iris dataset.

- Use inputs from the UI Sidebar to filter the dataset.
- Update reactive outputs in the UI Main Panel.

Matching the IDs in the UI Sidebar and function/output names in the UI Main Panel
to this server code is critical. They are case sensitive and must match exactly.

"""
import pathlib
from shiny import render
import pandas as pd
import seaborn as sns

from util_logger import setup_logger

logger, logname = setup_logger(__name__)


def get_iris_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    path_to_data = (
        pathlib.Path(__file__).parent.joinpath("data").joinpath("iris.xlsx")
    )
    original_df = pd.read_excel(path_to_data)
    total_count = len(original_df)

    @output
    @render.table
    def iris_table():
        return original_df

    @output
    @render.text
    def iris_record_count_string():
        message = f"Showing {total_count} records"
        logger.debug(f"filter message: {message}")
        return message

    @output
    @render.text
    def iris_filter_string():
        input_petal_length_range = input.IRIS_PETAL_LENGTH_RANGE()
        input_petal_width_range = input.IRIS_PETAL_LENGTH_RANGE()        
        length_min = input_petal_length_range[0]
        length_max = input_petal_length_range[1]
        width_min = input_petal_width_range[0]
        width_max = input_petal_width_range[1]
        filter_string = f"Petal length between {length_min} and {length_max}; Petal width between {width_min} and {width_max}"
        return filter_string

    @output
    @render.text
    def iris_filtered_record_count_string():
        logger.debug("Triggered iris_filter_record_count_string")
        df = original_df.copy()
        input_petal_length_range = input.IRIS_PETAL_LENGTH_RANGE()
        input_petal_width_range = input.IRIS_PETAL_LENGTH_RANGE()        
        length_min = input_petal_length_range[0]
        length_max = input_petal_length_range[1]
        width_min = input_petal_width_range[0]
        width_max = input_petal_width_range[1]
        condition1 = df["petal_length_cm"] >= length_min
        condition2 = df["petal_length_cm"] <= length_max
        condition3 = df["petal_width_cm"] >= width_min
        condition4 = df["petal_width_cm"] <= width_max
        filter = condition1 & condition2 & condition3 & condition4
        df = df[filter]
        filtered_records = len(df)
        record_count_string = (
            f"Filter shows {filtered_records} of {total_count} records"
        )
        return record_count_string

    @output
    @render.table
    def iris_filtered_table():
        logger.debug("Triggered iris_filtered_table")
        df = original_df.copy()
        input_petal_length_range = input.IRIS_PETAL_LENGTH_RANGE()
        input_petal_width_range = input.IRIS_PETAL_LENGTH_RANGE()        
        length_min = input_petal_length_range[0]
        length_max = input_petal_length_range[1]
        width_min = input_petal_width_range[0]
        width_max = input_petal_width_range[1]
        condition1 = df["petal_length_cm"] >= length_min
        condition2 = df["petal_length_cm"] <= length_max
        condition3 = df["petal_width_cm"] >= width_min
        condition4 = df["petal_width_cm"] <= width_max
        filter = condition1 & condition2 & condition3 & condition4
        df = df[filter]
        return df

    @output
    @render.text
    def iris_stats():
        """Generate and present summary statistics using pandas describe() method
        and by calling value_counts() on the species column."""

        desc = original_df.describe()
        formatted_desc = desc.applymap("{0:.2f}".format)
        part1 = formatted_desc.to_string()

        # Generate value counts for 'species' column
        value_counts = original_df["species"].value_counts().to_string()
        blank_line = "\n\n"
        part2 = "Value Counts for Species" + blank_line + value_counts
        reply = part1 + blank_line + part2 + blank_line
        return reply

    @output
    @render.plot
    def iris_pairplots():
        """Seaborn pairplot creates a grid of plots -
        each variable shares the
        y-axes across the row and the x-axes across a column.
        Diagonals show the distribution of data for that column.
        Seaborn charts aren't interactive, but they look nice.
        Don't worry about the formatting -
        we'll look at more interactive options in the next module."""

        df = original_df

        # Drop the 'Unnamed' index column
        df = df.drop(columns=["Unnamed: 0"])

        sns.set_theme(style="ticks")
        pairplot_grid = sns.pairplot(df, hue="species")
        return pairplot_grid

    @output
    @render.plot
    def iris_scatterplot1():
        """
        Use Seaborn to make a quick scatterplot.
        Provide a pandas DataFrame and the names of the columns to plot.
        Learn more at https://stackabuse.com/seaborn-scatter-plot-tutorial-and-examples/
        """

        df = original_df.copy()
        input_petal_length_range = input.IRIS_PETAL_LENGTH_RANGE()
        input_petal_width_range = input.IRIS_PETAL_LENGTH_RANGE()        
        length_min = input_petal_length_range[0]
        length_max = input_petal_length_range[1]
        width_min = input_petal_width_range[0]
        width_max = input_petal_width_range[1]
        condition1 = df["petal_length_cm"] >= length_min
        condition2 = df["petal_length_cm"] <= length_max
        condition3 = df["petal_width_cm"] >= width_min
        condition4 = df["petal_width_cm"] <= width_max
        filter = condition1 & condition2 & condition3 & condition4
        df = df[filter]

        plt = sns.scatterplot(
            data=df,
            x="petal_length_cm",
            y="petal_width_cm",
            hue="species",
        )
        return plt

    # return a list of function names for use in reactive outputs
    return [
        iris_table,
        iris_record_count_string,
        iris_stats,
        iris_filtered_table,
        iris_filtered_record_count_string,
        iris_pairplots,
        iris_scatterplot1,
    ]
