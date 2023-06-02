import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.io as pio
import plotly.express as px

# Dataset 'Processing'

path_datasets = 'https://raw.githubusercontent.com/Auroki/DV_Project_Examples/main/'
df_towa = pd.read_excel(path_datasets + 'df_towa_geo.xlsx', engine="openpyxl", sheet_name='Sheet1')


# Building our Graphs

# Regional Sales Line Chart

df_sales = df_towa.groupby(['Month', 'Salesman Region'])['Gross Sales'].sum()
df_sales = df_sales.reset_index()

df_regional_sales = df_sales.pivot_table('Gross Sales', ['Month'], 'Salesman Region')
df_regional_sales = df_regional_sales.reset_index()

x_region = df_regional_sales['Month']
y_region = df_regional_sales['North']

x_region_2 = df_regional_sales['Month']
y_region_2 = df_regional_sales['Center']

x_region_3 = df_regional_sales['Month']
y_region_3 = df_regional_sales['South']


data_1 = dict(type='scatter', x=x_region, y=y_region, name='North', line=dict(color='seagreen'))
data_2 = dict(type='scatter', x=x_region_2, y=y_region_2, name='Center', line=dict(color='darkgreen'))
data_3 = dict(type='scatter', x=x_region_3, y=y_region_3, name='South', line=dict(color='olive'))

data_4_3 = [data_1,data_2,data_3]

layout_4_3 = dict(title=dict(
                        text='Regional Sales by Month'
                        ),
                  xaxis=dict(title='Month'),
                  yaxis=dict(title='Gross Sales'),
                  paper_bgcolor = 'white', plot_bgcolor = 'white')

fig_1 = go.Figure(data=data_4_3, layout=layout_4_3)

fig_1.update_layout(title_x=0.5)
fig_1.update_traces(mode='lines')

fig_1.update_xaxes(showgrid=False)
fig_1.update_yaxes(showgrid=False)

############################################

# Regional Sales Pie Chart

df_pie_sales = df_towa.groupby(['Salesman Region'])['Gross Sales'].sum()
df_pie_sales = df_pie_sales.reset_index()

labels_pie = df_pie_sales['Salesman Region']

values_pie = df_pie_sales['Gross Sales']

data_pie = dict(type='pie', labels=labels_pie, values=values_pie)

layout_pie = dict(title=dict(text='Overall Regional Sales Distribution'))

fig_2 = go.Figure(data=[data_pie], layout=layout_pie)
fig_2.update_layout(title_x=0.5)
fig_2.update_traces(marker=dict(colors=['darkgreen', 'seagreen', 'olive']))

############################################

# Regional Sales HeatMap

df_regional_heat = df_towa.groupby(['Molecule', 'Salesman Region'])['Gross Sales'].sum()
df_regional_heat = df_regional_heat.reset_index()
df_regional_heat = df_regional_heat.pivot_table('Gross Sales', ['Salesman Region'], 'Molecule')

x_regional_heat = df_regional_heat.columns
y_regional_heat = df_regional_heat.index

z_regional_heat = df_regional_heat.values

data_regional_heat = dict(type='heatmap', x=x_regional_heat, y=y_regional_heat, z=z_regional_heat, colorscale='blugrn')

layout_regional_heat = dict(title=dict(text='Regional Sales by Product'))

fig_3 = go.Figure(data=[data_regional_heat], layout=layout_regional_heat)

fig_3.update_layout(title_x=0.5)

############################################

# Geo Map

df_geo = df_towa.groupby(['Pharma District', 'Pharma Lat', 'Pharma Long'])['Gross Sales'].sum()
df_geo = df_geo.reset_index()

fig = px.scatter_mapbox(df_geo, lat="Pharma Lat", lon="Pharma Long", hover_name="Pharma District", hover_data=["Pharma District", "Gross Sales"],
                        color="Gross Sales",
                        size="Gross Sales", color_continuous_scale=px.colors.sequential.Blugrn, size_max=40,
                        zoom=5, height=1000, mapbox_style="carto-positron")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

############################################

# National Gross, Net Discount Bar Chart by Month

df_national = df_towa.groupby('Month')[('Gross Sales', 'Discount', 'Net Sales')].sum()
df_national = df_national.reset_index()

x_bar_1 = df_national['Month']
y_bar_1 = df_national['Gross Sales']

x_bar_2 = df_national['Month']
y_bar_2 = df_national['Discount']

x_bar_3 = df_national['Month']
y_bar_3 = df_national['Net Sales']

data_gross = dict(type='bar', x=x_bar_1, y=y_bar_1, name='Gross Sales',
                  marker=dict(color='seagreen'))  # Here uou can change the color of a particular trace
data_disc = dict(type='bar', x=x_bar_2, y=y_bar_2, name='Discounts', marker=dict(color='olive'))
data_net = dict(type='bar', x=x_bar_3, y=y_bar_3, name='Net Sales', marker=dict(color='darkgreen'))

data_4 = [data_gross, data_disc, data_net]

layout_4 = dict(title=dict(text='National Sales Performance'))

fig_4 = go.Figure(data=data_4, layout=layout_4)

fig_4.update_xaxes(showgrid=False)
fig_4.update_yaxes(showgrid=False)
fig_4.update_layout(title_x=0.5)
fig_4.update_layout(plot_bgcolor='White')
fig_4.update_layout(paper_bgcolor='White')

############################################

# National Gross, Net Discount Bar Chart by Product

df_national_1 = df_towa.groupby('Molecule')[('Gross Sales', 'Discount', 'Net Sales')].sum()
df_national_1 = df_national_1.reset_index()

x_bar_4 = df_national_1['Molecule']
y_bar_4 = df_national_1['Gross Sales']

x_bar_5 = df_national_1['Molecule']
y_bar_5 = df_national_1['Discount']

x_bar_6 = df_national_1['Molecule']
y_bar_6 = df_national_1['Net Sales']

data_gross = dict(type='bar', x=x_bar_4, y=y_bar_4, name='Gross Sales',
                  marker=dict(color='seagreen'))  # Here uou can change the color of a particular trace
data_disc = dict(type='bar', x=x_bar_5, y=y_bar_5, name='Discounts', marker=dict(color='olive'))
data_net = dict(type='bar', x=x_bar_6, y=y_bar_6, name='Net Sales', marker=dict(color='darkgreen'))

data_5 = [data_gross, data_disc, data_net]

layout_5 = dict(title=dict(text='National Sales Performance'))

fig_5 = go.Figure(data=data_5, layout=layout_5)

fig_5.update_xaxes(showgrid=False)
fig_5.update_yaxes(showgrid=False)
fig_5.update_layout(title_x=0.5)
fig_5.update_layout(plot_bgcolor='White')
fig_5.update_layout(paper_bgcolor='White')

############################################

# Molecule Units Sold by WholeSaler Bar Chart

df_whs_product = df_towa.groupby(['Molecule', 'WholeSaler'])['Units'].sum()
df_whs_product = df_whs_product.reset_index()
df_whs_product = df_whs_product.pivot_table('Units', ['WholeSaler'], 'Molecule')
product_list = df_whs_product.columns
df_whs_product.index

data_whs_product = [dict(type='bar',
             x=df_whs_product.index,
             y=df_whs_product[product],
             name=product)
                            for product in product_list]

layout_whs_product = dict(title=dict(
                        text='Molecule Units Sold by WholeSaler'
                  ),
                  xaxis=dict(title='WholeSaler'),
                  yaxis=dict(title='Units Sold'))

fig_whs_product = go.Figure(data=data_whs_product, layout=layout_whs_product)
fig_whs_product.update_xaxes(showgrid=False)
fig_whs_product.update_yaxes(showgrid=False)
fig_whs_product.update_layout(plot_bgcolor = 'White')
fig_whs_product.update_layout(paper_bgcolor = 'White')
fig_whs_product.update_layout(title_x=0.5)

############################################

# Molecule Sales by WholeSaler Line Chart

df_whs_series = df_towa.groupby(['Month', 'WholeSaler'])['Gross Sales'].sum()
df_whs_series = df_whs_series.reset_index()
df_whs_series = df_whs_series.pivot_table('Gross Sales', ['Month'], 'WholeSaler')
whs_list = df_whs_series.columns

data_whs_series = [dict(type='scatter',
             x=df_whs_series.index,
             y=df_whs_series[whs],
             name=whs)
                            for whs in whs_list]

layout_whs_series = dict(title=dict(
                        text='Molecule Sales by WholeSaler'
                  ),
                  xaxis=dict(title='WholeSaler'),
                  yaxis=dict(title='Gross Sales'))

fig_whs_series = go.Figure(data=data_whs_series, layout=layout_whs_series)
fig_whs_series.update_xaxes(showgrid=False)
fig_whs_series.update_yaxes(showgrid=False)
fig_whs_series.update_layout(plot_bgcolor = 'White')
fig_whs_series.update_layout(paper_bgcolor = 'White')
fig_whs_series.update_layout(title_x=0.5)
fig_whs_series.update_traces(mode='lines')

############################################

# Molecule Units Sold by Salesman Bar Chart

df_salesman_product = df_towa.groupby(['Molecule', 'Salesman'])['Units'].sum()
df_salesman_product = df_salesman_product.reset_index()
df_salesman_product = df_salesman_product.pivot_table('Units', ['Salesman'], 'Molecule')
product_list_1 = df_salesman_product.columns
df_salesman_product.index

data_salesman_product = [dict(type='bar',
             x=df_salesman_product.index,
             y=df_salesman_product[product],
             name=product)
                            for product in product_list_1]

layout_salesman_product = dict(title=dict(
                        text='Molecule Units Sold by Salesman'
                  ),
                  xaxis=dict(title='Salesman'),
                  yaxis=dict(title='Units Sold'))

fig_salesman_product = go.Figure(data=data_salesman_product, layout=layout_salesman_product)
fig_salesman_product.update_xaxes(showgrid=False)
fig_salesman_product.update_yaxes(showgrid=False)
fig_salesman_product.update_layout(plot_bgcolor = 'White')
fig_salesman_product.update_layout(paper_bgcolor = 'White')
fig_salesman_product.update_layout(title_x=0.5)

############################################

# Gross Sales by Salesman Line Chart

df_salesman_series = df_towa.groupby(['Month', 'Salesman'])['Gross Sales'].sum()
df_salesman_series = df_salesman_series.reset_index()
df_salesman_series = df_salesman_series.pivot_table('Gross Sales', ['Month'], 'Salesman')
salesman_list = df_salesman_series.columns

data_salesman_series = [dict(type='scatter',
             x=df_salesman_series.index,
             y=df_salesman_series[salesman],
             name=salesman)
                            for salesman in salesman_list]

layout_salesman_series = dict(title=dict(
                        text='Gross Sales by Salesman'
                  ),
                  xaxis=dict(title='Salesman'),
                  yaxis=dict(title='Gross Sales'))

fig_salesman_series = go.Figure(data=data_salesman_series, layout=layout_salesman_series)
fig_salesman_series.update_xaxes(showgrid=False)
fig_salesman_series.update_yaxes(showgrid=False)
fig_salesman_series.update_layout(plot_bgcolor = 'White')
fig_salesman_series.update_layout(paper_bgcolor = 'White')
fig_salesman_series.update_layout(title_x=0.5)
fig_salesman_series.update_traces(mode='lines')

############################################

# Molecule Sales by Pharmacies Line Chart

df_pharma_series = df_towa.groupby(['Month', 'Pharmacies'])['Gross Sales'].sum()
df_pharma_series = df_pharma_series.reset_index()
df_pharma_series = df_pharma_series.pivot_table('Gross Sales', ['Month'], 'Pharmacies')
pharma_list = df_pharma_series.columns

data_pharma_series = [dict(type='scatter',
             x=df_pharma_series.index,
             y=df_pharma_series[pharma],
             name=pharma)
                            for pharma in pharma_list]

layout_pharma_series = dict(title=dict(
                        text='Molecule Sales by Pharmacies'
                  ),
                  xaxis=dict(title='Pharmacies'),
                  yaxis=dict(title='Gross Sales'))

fig_pharma_series = go.Figure(data=data_pharma_series, layout=layout_pharma_series)
fig_pharma_series.update_xaxes(showgrid=False)
fig_pharma_series.update_yaxes(showgrid=False)
fig_pharma_series.update_layout(plot_bgcolor = 'White')
fig_pharma_series.update_layout(paper_bgcolor = 'White')
fig_pharma_series.update_layout(title_x=0.5)
fig_pharma_series.update_traces(mode='lines')

############################################

# Gross Sales by Pharma Group Line Chart

df_group_series = df_towa.groupby(['Month', 'Pharma Group'])['Gross Sales'].sum()
df_group_series = df_group_series.reset_index()
df_group_series = df_group_series.pivot_table('Gross Sales', ['Month'], 'Pharma Group')
group_list = df_group_series.columns

data_group_series = [dict(type='scatter',
             x=df_group_series.index,
             y=df_group_series[group],
             name=group)
                            for group in group_list]

layout_group_series = dict(title=dict(
                        text='Gross Sales by Pharma Group'
                  ),
                  xaxis=dict(title='Pharma Group'),
                  yaxis=dict(title='Gross Sales'))

fig_group_series = go.Figure(data=data_group_series, layout=layout_group_series)
fig_group_series.update_xaxes(showgrid=False)
fig_group_series.update_yaxes(showgrid=False)
fig_group_series.update_layout(plot_bgcolor = 'White')
fig_group_series.update_layout(paper_bgcolor = 'White')
fig_group_series.update_layout(title_x=0.5)
fig_group_series.update_traces(mode='lines')

############################################
############################################
############################################
############################################
############################################

# The App itself

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
    html.Div([
        html.H1('TOWA 2021 Sales Dasboard', style={'textAlign': 'center'})
    ], className='title'),
    html.Div([
        html.P('Students:  David Peralta (20221090) | Carlos Nunes (20210997) | Eliane Gotuzzo (20210996)  .',className='paragraph')
    ], className='column_two'),
    html.Div([
    html.H1('National & Regional Presentation', style={"font-size": "25px"})
    ], className='title'),
    html.Div([
        html.Div([
            html.Div([
                dcc.Graph(
                    id='geo-graph',
                    figure=fig
                ),
                html.H3(children='')
            ],
                className='column_two'),
            html.Div([
                dcc.Graph(id='national_sales-graph',
                          figure=fig_4),
            ],
                className='column1'
            )
        ],
            className='row'),
    ]),
    html.Div([
        html.Div([
            html.Div([
                dcc.Graph(
                    id='national_product-graph',
                    figure=fig_5
                ),
                html.H3(children='')
            ],
                className='column_two'),
            html.Div([
                dcc.Graph(id='heatmap-graph',
                          figure=fig_3),
            ],
                className='column1'
            )
        ],
            className='row'),
    ]),
    html.Div([
        html.Div([
            html.Div([
                dcc.Graph(
                    id='regional_line-graph',
                    figure=fig_1
                ),
                html.H3(children='')
            ],
                className='column_two'),
            html.Div([
                dcc.Graph(id='pie-graph',
                          figure=fig_2),
            ],
                className='column1'
            )
        ],
            className='row'),
    ]),
    html.Div([
        html.Div([
            html.Div([
                dcc.Graph(
                    id='wholesaler_product_bar-graph',
                    figure=fig_whs_product
                ),
                html.H3(children='')
            ],
                className='column_two'),
            html.Div([
                dcc.Graph(id='molecule_wholesaler_line-graph',
                          figure=fig_whs_series),
            ],
                className='column1'
            )
        ],
            className='row'),
    ]),
    html.Div([
        html.Div([
            html.Div([
                dcc.Graph(
                    id='salesman_product_bar-graph',
                    figure=fig_salesman_product
                ),
                html.H3(children='')
            ],
                className='column_two'),
            html.Div([
                dcc.Graph(id='molecule_salesman_line-graph',
                          figure=fig_salesman_series),
            ],
                className='column1'
            )
        ],
            className='row'),
    ]),
    html.Div([
        html.Div([
            html.Div([
                dcc.Graph(
                    id='molecule_pharma_line-graph',
                    figure=fig_pharma_series
                ),
                html.H3(children='')
            ],
                className='column_two'),
            html.Div([
                dcc.Graph(id='molecule_group_line-graph',
                          figure=fig_group_series),
            ],
                className='column1'
            )
        ],
            className='row')
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)