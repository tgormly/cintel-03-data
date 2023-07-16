"""
Purpose: Provide user interaction options for the Iris dataset.

 - Choose checkboxes when the options are independent of each other.
 - Choose radio buttons when a set of options are mutually exclusive.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""

from shiny import ui


def get_penguins_inputs():
    return ui.panel_sidebar(
        ui.h2("Iris Interaction"),
        ui.tags.hr(),
        ui.tags.h3("Petal Length"),        
        ui.input_slider(
            "IRIS_PETAL_LENGTH_RANGE",
            "Petal Length (cm)",
            min=1,
            max=7,
            value=[0, 3],
        ),
        ui.tags.hr(),
        ui.tags.h3("Petal Width"),        
        ui.input_slider(
            "IRIS_PETAL_WIDTH_RANGE",
            "Petal Width (cm)",
            min=0,
            max=3,
            value=[0, 3],
        ),
        ui.tags.hr(),
        ui.tags.h3("Species"),
        ui.input_checkbox("IRIS_SPECIES_Setosa", "Setosa", value=True),
        ui.input_checkbox("IRIS_SPECIES_Versicolor", "Versicolor", value=True),
        ui.input_checkbox("IRIS_SPECIES_Virginica", "Virginica", value=True),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
