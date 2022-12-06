import pandas as pd
import plotly.express as px

# Formating
def set_layout_and_display_1y(
    figure_object,
    x_col_name,
    y_col_name,
    title_str,
    y_is_percentage,
    showlegend,
    show_y_axis,
    show_x_axis,
    size_width,
    size_height,
    y_axis_range,
):
    """
    Sets the layout and displays the chart
    """

    # Set the layout
    figure_object.update_layout(
        title=title_str,
        xaxis_title=x_col_name,
        yaxis_title=y_col_name,
        showlegend=showlegend,
        yaxis={"visible": show_y_axis},
        xaxis={"visible": show_x_axis},
        width=size_width,
        height=size_height,
        yaxis_range=y_axis_range,
    )

    # Set the y axis to be percentage
    if y_is_percentage:
        figure_object.update_yaxes(tickformat="%")

    return figure_object


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
        # show_x_axis
        show_x_axis = kwargs["show_x_axis"] if "show_x_axis" in kwargs else True
        # size_width
        size_width = kwargs["size_width"] if "size_width" in kwargs else 1000
        # Size height
        size_height = kwargs["size_height"] if "size_height" in kwargs else 500

        fig = set_layout_and_display_1y(
            figure_object=fig,
            x_col_name=x_title_text,
            y_col_name=y_title_text,
            title_str=title,
            y_is_percentage=y_is_percentage,
            showlegend=showlegend,
            show_y_axis=show_y_axis,
            show_x_axis=show_x_axis,
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
