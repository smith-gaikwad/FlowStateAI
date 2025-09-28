import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
import json

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

def create_kpi_card(title, value_id, color):
    return dbc.Card(
        dbc.CardBody([
            html.H4(title, className="card-title"),
            html.H2("...", className="card-text", id=value_id),
        ]),
        color=color, inverse=True, style={'textAlign': 'center', 'margin': '10px'}
    )

app.layout = dbc.Container([
    html.H1("FlowStateAI - Mumbai Traffic Dashboard 🚦", style={'textAlign': 'center', 'padding': '20px'}),
    dbc.Row([
        dbc.Col(create_kpi_card("Sim Time (s)", "kpi-sim-time", "primary")),
        dbc.Col(create_kpi_card("Avg Wait Time (s)", "kpi-avg-wait-time", "info")),
        dbc.Col(create_kpi_card("Vehicles Passed (per step)", "kpi-cars-passed", "success")),
    ]),
    html.Div([
        html.H3("🚨 Predictive Alerts (GNN-LSTM)", style={'textAlign': 'center', 'paddingTop': '20px'}),
        html.Div(id='bottleneck-alert', style={'textAlign': 'center', 'fontSize': '24px', 'color': '#ff4d4d', 'padding': '10px', 'fontWeight': 'bold'})
    ]),
    html.Div([
        html.H3("System Logs", style={'paddingTop': '20px'}),
        html.Pre(id='system-log', style={'backgroundColor': '#1E1E1E', 'color': '#D4D4D4', 'border': '1px solid #333', 'padding': '10px', 'height': '200px', 'overflowY': 'scroll'})
    ]),
    dcc.Interval(id='interval-component', interval=1000, n_intervals=0)
], fluid=True)

@app.callback(
    [Output('kpi-sim-time', 'children'), Output('kpi-avg-wait-time', 'children'), Output('kpi-cars-passed', 'children'), Output('bottleneck-alert', 'children'), Output('system-log', 'children')],
    Input('interval-component', 'n_intervals')
)
def update_dashboard(n):
    try:
        with open('simulation_data.json', 'r') as f: data = json.load(f)
        with open('system_log.txt', 'r', encoding='utf-8') as f: log_content = "".join(f.readlines()[-20:])
        return (data.get('time', '...'), data.get('avg_wait_time', '...'), data.get('cars_passed', '...'), data.get('bottleneck_alert', 'None'), log_content)
    except (FileNotFoundError, json.JSONDecodeError):
        return "...", "...", "...", "Waiting for data...", "Initializing..."

if __name__ == '__main__':
    app.run(debug=True)