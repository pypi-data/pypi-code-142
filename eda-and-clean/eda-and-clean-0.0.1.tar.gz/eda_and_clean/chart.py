import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Formatting for Plotly

COLORS = {
    "darkgrey": "rgb(189,189,189)",
    "midgrey": "#AFAFAF",
    "lightgrey": "#e6e6e6",
    "black": "#151514",
    "lightblack": "#363632",
    "gold": "#b6972f",
    "white": "#fff",
    "lightgreen": "#5CD198",
    "darkgreen": "#548F72",
    "darkblue": "#007283",
    "red": "#C23939",
}


def get_standard_layout_dict(
    chart_title: str = None,
    xaxis_title: str = None,
    yaxis_title: str = None,
    yaxis2_title: str = None,
) -> dict:
    """
    Returns our standard layout for plotly. Inputs:
    - Chart title
    - X axis title
    - Y axis title

    If one or more of the above arguments is not given, the default behavior is to simply not
    show that title.
    """

    layout_dict = {
        "autosize": True,
        "title": {
            "text": chart_title,
            "xref": "container",
            "yref": "container",
            "y": 1,
            "x": 0.5,
            "pad": {"t": 30, "b": 20},
            "font": {
                "size": 15,
                "family": "Eina, sans-serif",
                "color": COLORS["white"],
            },
        },
        "xaxis": {
            "title": xaxis_title,
            "ticks": "outside",
            "ticklen": 10,
            "showticklabels": True,
            "showline": False,
            "zeroline": False,
            "gridcolor": COLORS["lightblack"],
            "automargin": True,
        },
        "yaxis": {
            "title": yaxis_title,
            "ticks": "outside",
            "ticklen": 10,
            "showticklabels": True,
            "showline": False,
            "zeroline": False,
            "gridcolor": COLORS["lightblack"],
            "automargin": True,
        },
        "font": {"size": 12, "family": "Eina, sans-serif", "color": COLORS["midgrey"]},
        "legend": {"x": 1.07},
        "paper_bgcolor": COLORS["black"],
        "plot_bgcolor": COLORS["black"],
    }

    if yaxis2_title:
        layout_dict.update(
            {
                "yaxis2": {
                    "title": yaxis2_title,
                    "ticks": "outside",
                    "ticklen": 10,
                    "showticklabels": True,
                    "showline": False,
                    "zeroline": False,
                    "gridcolor": COLORS["lightblack"],
                    "anchor": "free",
                    "overlaying": "y",
                    "side": "right",
                    "position": 1.0,
                    "automargin": True,
                }
            }
        )
    return layout_dict


def get_standard_layout(
    chart_title: str = None,
    xaxis_title: str = None,
    yaxis_title: str = None,
    yaxis2_title: str = None,
) -> go.Layout:

    """
    Returns our standard layout for plotly. Inputs:
    - Chart title
    - X axis title
    - Y axis title

    If one or more of the above arguments is not given, the default behavior is to simply not
    show that title.
    """

    return go.Layout(
        get_standard_layout_dict(chart_title, xaxis_title, yaxis_title, yaxis2_title)
    )


layout = get_standard_layout(chart_title="")
layout_yaxis2 = get_standard_layout(chart_title="", yaxis2_title="NA")


def set_layout_and_display(
    figure_object,
    x_col_name: str,
    y_col_name: str,
    title_str: str,
    y_is_percentage: bool,
    showlegend: bool,
    show_y_axis: bool,
    size_width: int,
    size_height: int,
    layout=layout,
    y_axis_range=None,
):

    # Set layout
    figure_object.layout = layout

    # Set y as percentage if required
    if y_is_percentage:
        figure_object.layout.yaxis.tickformat = ",.0%"

    # Set legend position and size
    figure_object = set_legends_and_size_plotly(
        fig=figure_object, size_width=size_width, size_height=size_height
    )

    # Set x and y axis names
    figure_object.update_xaxes(title_text=x_col_name)
    figure_object.update_yaxes(title_text=y_col_name)

    # Add figure title
    figure_object.update_layout(title_text=title_str)

    # Show legend
    figure_object.update_layout(showlegend=showlegend)

    # Show y-axis
    figure_object.update_yaxes(visible=show_y_axis)

    # Set y-axis range
    if y_axis_range is not None:
        figure_object.update_layout(yaxis_range=y_axis_range)

    return figure_object


def set_layout_and_display_2y(
    figure_object,
    x_col_name: str,
    y1_col_name: str,
    y2_col_name: str,
    title_str: str,
    y1_is_percentage: bool,
    y2_is_percentage: bool,
    x_is_int: bool,
    x_is_date: bool,
    are_negative_numbers_possible: bool = False,
    max_abs_value_main_y: float = None,
    max_abs_value_secondary_y: float = None,
    y_bound_multiple: float = 1.1,
    layout=layout_yaxis2,
):

    # Set layout
    figure_object.layout = layout

    # Set y as percentage if required
    if y1_is_percentage:
        figure_object.layout.yaxis.tickformat = ",.0%"
    if y2_is_percentage:
        figure_object.layout.yaxis2.tickformat = ",.0%"

    # Set proper format for x axis
    if x_is_int:
        figure_object.layout.xaxis.tickformat = ",d"
    elif x_is_date:
        figure_object.update_layout(xaxis=dict(tickformat="%m-%Y"))

    # Set legend position and size
    figure_object = set_legends_and_size_plotly(fig=figure_object)

    # Set x and y axis names
    figure_object.update_xaxes(title_text=x_col_name)
    figure_object.update_yaxes(title_text=y1_col_name, secondary_y=False)
    figure_object.update_yaxes(title_text=y2_col_name, secondary_y=True)

    # Add figure title
    figure_object.update_layout(title_text=title_str)

    # Align 0 - This will work as long as there are no negative values
    figure_object.update_yaxes(rangemode="tozero")
    figure_object.update_xaxes(rangemode="tozero")

    # Update y axis range if required
    if are_negative_numbers_possible:

        if max_abs_value_secondary_y is None:
            raise ValueError("Pls provide abs max value for secondary y axis")
        if max_abs_value_main_y is None:
            raise ValueError("Pls provide abs max value for primary y axis")

        figure_object.update_yaxes(
            scaleanchor="y1",
            scaleratio=1,
            constraintoward="bottom",
            secondary_y=False,
            range=[
                max_abs_value_main_y * -y_bound_multiple,
                max_abs_value_main_y * y_bound_multiple,
            ],
        )

        figure_object.update_yaxes(
            scaleanchor="y2",
            scaleratio=1,
            constraintoward="bottom",
            secondary_y=True,
            range=[
                max_abs_value_secondary_y * -y_bound_multiple,
                max_abs_value_secondary_y * y_bound_multiple,
            ],
        )

    # https://community.plotly.com/t/plotly-express-with-xaxis-having-integers-strings/34777/2
    figure_object.update_layout(xaxis_type="category")

    return figure_object


def set_legends_and_size_plotly(fig, size_width: int, size_height: int):
    """ """
    fig.update_layout(legend=dict(orientation="h", y=-0.3, x=0))
    fig.update_layout(autosize=False, width=size_width, height=size_height)
    return fig


## MAIN FUNCTIONS ##


def standard_chart_formatting_1y(func):
    """
    Decorator for adding formatting on top of charts
    """

    def inner(*args, **kwargs):
        fig = func(*args, **kwargs)

        # Lets bypass the decorator if certain conditions are met
        bypass_decorator = False
        for key in ["marginal", "facet_col", "facet_row"]:
            if key in kwargs:
                bypass_decorator = True

        if bypass_decorator:
            return fig

        # x_title_text
        x_title_text = kwargs["x_title_text"] if "x_title_text" in kwargs else None
        # y_title_text
        y_title_text = kwargs["y_title_text"] if "y_title_text" in kwargs else None
        # title
        title = kwargs["title"] if "title" in kwargs else None
        # y_is_percentage
        y_is_percentage = (
            kwargs["y_is_percentage"] if "y_is_percentage" in kwargs else False
        )
        # showlegend
        showlegend = kwargs["showlegend"] if "showlegend" in kwargs else True
        # show_y_axis
        show_y_axis = kwargs["show_y_axis"] if "show_y_axis" in kwargs else True
        # size_width
        size_width = kwargs["size_width"] if "size_width" in kwargs else 1000
        # Size height
        size_height = kwargs["size_height"] if "size_height" in kwargs else 500

        fig = set_layout_and_display(
            figure_object=fig,
            x_col_name=x_title_text,
            y_col_name=y_title_text,
            title_str=title,
            y_is_percentage=y_is_percentage,
            showlegend=showlegend,
            show_y_axis=show_y_axis,
            layout=layout,
            size_width=size_width,
            size_height=size_height,
            y_axis_range=None,
        )
        return fig

    return inner


# Function to create histogram plot using plotly
@standard_chart_formatting_1y
def histogram_plotly(
    df: pd.DataFrame,
    x_col_name: str,
    y_col_name: str,
    nbins: int,
    color: str = None,
    **kwargs,
) -> None:
    """
    color can be used to plot different categories separately - For example same plot for different sex
    """
    fig = px.histogram(df, x=x_col_name, y=y_col_name, color=color, nbins=nbins)

    return fig


@standard_chart_formatting_1y
def line_plotly(
    df: pd.DataFrame,
    x_col_name: str,
    hover_data: list,
    **kwargs,
) -> None:
    """
    Options for marginal include "histogram", "rug"
    """
    fig = px.line(df, x=x_col_name, y="cdf", hover_data=hover_data)
    return fig


@standard_chart_formatting_1y
def plotly_heatmap(
    _df: pd.DataFrame,
    annotation: bool = True,
    show_y_axis: bool = True,
    **kwargs,
) -> None:
    df = _df.copy()
    fig = px.imshow(
        df.round(2),
        color_continuous_scale="RdBu",
        origin="lower",
        text_auto=annotation,
    )
    """
    fig.update_layout(showlegend=False)
    fig.update_yaxes(visible=show_y_axis)
    fig.update_layout(
        autosize=False,
        width=size,
        height=size,
    )
    """
    return fig
