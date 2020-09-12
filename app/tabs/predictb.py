from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import numpy as np
import pandas as pd



from app import app

category = ['Academia','Admin','Consultant','Engineering', 'Entertainment', 'Executive', 'Finance', 'Government', 'HR', 'IT','Management','Marketing','Operations', 'Other', 'Sales', 'Service', 'Health', 'Law', 'Unemployed']

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict
        Use the controls below to predict the expected tenure. Prediction is based on "Job Category", "Number of Degrees", "Number of Certifications", "Average Salary" and "Historical Tenure". 

    """),

    html.Div(id='prediction-content', style={'fontWeight': 'bold'}),

    html.Div([
        dcc.Markdown('###### Job Category'),
        dcc.Dropdown(
            id='category',
            options=[{'label': type, 'value': type} for type in category],
            value=category[10]
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Number of Degrees'),
        dcc.Slider(
            id='degrees',
            min=1,
            max=5,
            step=1,
            value=3,
            marks={n: str(n) for n in range(1, 5, 1)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Number of Certifications'),
        dcc.Slider(
            id='certifications',
            min=1,
            max=3,
            step=1,
            value=0,
            marks={n: str(n) for n in range(1, 3, 1)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Average Salary'),
        dcc.Slider(
            id='salary',
            min=0,
            max=200000,
            step=10000,
            value=50000,
            marks={n: str(n) for n in range(0, 200000, 10000)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Historical Tenure'),
        dcc.Slider(
            id='months',
            min=0,
            max=1000,
            step=1,
            value=30,
            marks={n: f'{n/1000:.0f}k' for n in range(0, 1000, 1)}
        ),
    ], style=style),


])


@app.callback(
    Output('prediction-content', 'children'),
    [Input('category', 'value'),
     Input('degrees', 'value'),
     Input('certifications', 'value'),
     Input('salary', 'value'),
     Input('months', 'value')])
def predict(category, degrees, certifications, salary, months):

    Co1 = 1
    jobs = 3
    df = pd.DataFrame(
        columns=['Cat1', 'AvgS1', 'M1', 'Co1', 'Cat2', 'AvgS2', 'M2', 'Co2', 'Cat3', 'AvgS3', 'M3', 'Co3', 'Cat4', 'AvgS4', 'M4', 'Co4', 'NumDeg', 'NumCertf', 'numJobs'],
        #data=[[category, degrees, certifications, salary, months]]
        data=[[category, salary, months, Co1, category, salary, months, Co1, category, salary, months, Co1, category, salary, months, Co1, degrees, certifications, jobs]]
    )

    pipeline = load('model/pipelineb.joblib')
    y_pred_log = pipeline.predict(df)
    y_pred = y_pred_log[0]
    exp_months = np.exp(y_pred)
    predict_months = exp_months
    
    results = f'We expect this person to stay employed for:   {predict_months:.2f} months'

    return results
