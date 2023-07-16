"""
Purpose: Display outputs for Iris dataset.

Choose the correct ui method for the type of output you want to display.
Provide the exact name of the server function that will provide the output.

"""
from shiny import ui


def get_iris_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Iris: Seaborn Scatter Plot (filtered by Petal Length & Width)"),
            ui.output_plot("iris_scatterplot1"),
            ui.tags.hr(),
            ui.h3("Filtered Iris Table (filtered by Petal Length & Width)"),
            ui.output_text("iris_filtered_record_count_string"),
            ui.output_table("iris_filtered_table"),
            ui.tags.hr(),
            ui.h3("Iris: Seaborn Pair Plots"),
            ui.output_plot("iris_pairplots"),
            ui.tags.hr(),
            ui.h3("Iris Table Summary Statistics"),
            ui.output_text_verbatim("iris_stats"),
            ui.tags.hr(),
            ui.h3("Iris Table"),
            ui.output_text("iris_record_count_string"),
            ui.output_table("iris_table"),
            ui.tags.hr(),
        ),
    )
