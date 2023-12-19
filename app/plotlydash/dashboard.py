"""Instantiate a Dash app."""
import numpy as np
import pandas as pd
import dash
from dash import dash_table
from dash import html, dcc
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
from .data import create_dataframe
from .layout import html_layout
from .. import rf_model
import plotly.io as pio
pio.templates.default = 'seaborn'

colors = [[0.0, '#052F5F'],
          [0.1, '#0B3D8C'],
          [0.2, '#124AB7'],
          [0.3, '#1861D1'],
          [0.4, '#2E75B6'],
          [0.5, '#4B8FCE'],
          [0.6, '#69A6E4'],
          [0.7, '#87BEFA'],
          [0.8, '#A6D6FF'],
          [0.9, '#C4EFFF'],
          [1.0, '#E3F8FF']]
reversed_colors_list = [
    [0.0, '#E3F8FF'],
    [0.1, '#C4EFFF'],
    [0.2, '#A6D6FF'],
    [0.3, '#87BEFA'],
    [0.4, '#69A6E4'],
    [0.5, '#4B8FCE'],
    [0.6, '#2E75B6'],
    [0.7, '#1861D1'],
    [0.8, '#124AB7'],
    [0.9, '#0B3D8C'],
    [1.0, '#052F5F']
]


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/'
    )

    # Load DataFrame
    df = create_dataframe()
    df.columns = df.columns.str.title()
    # Create confusion matrix
    corr = round(df.corr(), 3)
    mask = np.triu(np.ones_like(corr, dtype=bool))
    df_mask = corr.mask(mask)

    z = df_mask.to_numpy()
    x = df_mask.columns.tolist()
    y = df_mask.columns.tolist()

    # colorscale = 'Viridis'  # Replace this with your desired colorscale

    # Create the heatmap trace
    trace = go.Heatmap(z=z, x=x, y=y, colorscale=colors)

    # Create the layout
    layout = go.Layout(

        title_x=0.5,
        xaxis=dict(showgrid=False, zeroline=False, side="bottom"),
        yaxis=dict(showgrid=False, zeroline=False, autorange='reversed'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    # Create the figure
    feature_heatmap_fig = go.Figure(data=[trace], layout=layout)

    # Update the annotations to handle NaN values
    for i in range(len(feature_heatmap_fig.layout.annotations)):
        if feature_heatmap_fig.layout.annotations[i].text == 'nan':
            feature_heatmap_fig.layout.annotations[i].text = ""

    # Create feature importance bar chart
    feature_importance = pd.Series(rf_model.feature_importances_*100,
                                   index=df.columns[:-1]).sort_values(ascending=False)
    feat_importance_fig = px.bar(feature_importance,
                                 labels={'value': 'Importance',
                                         'index': 'Features'},
                                 color=feature_importance.values,  # Set color to the importance values
                                 color_continuous_scale=reversed_colors_list  # Change to blue color scale
                                 )
    feat_importance_fig.layout.update(showlegend=False,
                                      plot_bgcolor='rgba(0,0,0,0)',
                                      paper_bgcolor='rgba(0,0,0,0)')

    # Create age/feature scatter plot
    x_graph = df[df['Class'] == True]['Age'].value_counts().index
    y_graph = df[df['Class'] == True]['Age'].value_counts().values
    age_scatter_fig = go.Figure()
    age_scatter_fig.add_trace(go.Scatter(x=x_graph, y=y_graph,
                                         mode='markers',
                                         name='Diabetes',
                                         # Change marker color to green
                                         marker={"size": 12, "color": 'red'}))
    x_graphb = df[df['Polyuria'] == True]['Age'].value_counts().index
    y_graphb = df[df['Polyuria'] == True]['Age'].value_counts().values
    age_scatter_fig.add_trace(go.Scatter(x=x_graphb, y=y_graphb,
                                         mode='markers',
                                         name='Polyuria',
                                         # Change marker color to green
                                         marker={"size": 12, "color": 'blue'}))
    age_scatter_fig.update_layout(
        xaxis_title="Age",
        yaxis_title="Number of Patients",
        legend_title="Condition",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            html.Br(),
            html.H5(children="Feature Heatmap", className="lh-1"),
            dcc.Graph(figure=feature_heatmap_fig),
            html.Br(),
            html.H5(children="Feature Importance",  className="lh-1"),
            dcc.Graph(figure=feat_importance_fig),
            html.Br(),
            html.H5(children="Age Distribution", className="lh-1"),
            dcc.Graph(figure=age_scatter_fig),
            html.Br(),
            html.H5(children="Raw Data", className="lh-1"),
            html.Br(),
            html.Br(),
            create_data_table(df),
        ],
        id='dash-container'
    )
    return dash_app.server


def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    class_index = df.columns.get_loc("Class")

    # Get the list of column names in the DataFrame
    columns_list = df.columns.tolist()

    # Reorder the columns with "Class" column at the beginning
    reordered_columns = ['Class'] + \
        columns_list[:class_index] + columns_list[class_index+1:]

    # Create a new DataFrame with the reordered columns
    df_table = df[reordered_columns]

    table = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in df_table.columns],
        data=df_table.to_dict('records'),
        style_table={'overflowX': 'scroll'},
        sort_action="native",
        sort_mode='native',
        page_size=10,
    )
    return table
