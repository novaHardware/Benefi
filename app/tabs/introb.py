from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro

Benefi is an elegant solution for companies that are committed to helping employees navigate financial uncertainty. Benefi wants employers attract, retain, and engage employees, by improving their financial wellness. It's Benefi's mission to help Canadians escape consumer debt.  

This web app enables the user to determine an employee's expected tenure taking into account their historical tenure, their role type, their salary, number of degrees, number of certifications.  


""")]
