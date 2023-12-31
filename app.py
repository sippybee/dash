from dash import Dash
import dash_bootstrap_components as dbc 
from layout import create_layout
from data.util import get_data
import os


cwd = os.getcwd()
file_path = (f'{cwd}/data/gas_sale.csv')




data = get_data(file_path)
app = Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])
app.title = 'Gas Prices'
app.layout = create_layout(app, data)
server = app.server


if __name__ == '__main__':
    app.run_server(debug=True)


