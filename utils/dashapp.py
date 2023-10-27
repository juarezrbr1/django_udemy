import dash
from dash import dcc, html

import plotly.express as px
import pandas as pd

# Crie um aplicativo Dash
app = dash.Dash(__name__)

# Dados para o gráfico
data = pd.DataFrame({
    'Fruit': ['Apple', 'Banana', 'Cherry', 'Date'],
    'Amount': [15, 25, 10, 5]
})

# Layout do aplicativo
app.layout = html.Div([
    html.H1('Gráfico de Frutas'),
    dcc.Graph(
        figure=px.bar(data, x='Fruit', y='Amount', title='Quantidade de Frutas')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
