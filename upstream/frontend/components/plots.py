import plotly.express as px
import pandas as pd
from sklearn.cluster import KMeans

def plot_monthly_charges_histogram(df):
    fig = px.histogram(
        df,
        x='monthly_charges',
        nbins=30,
        title="Monthly Charges Distribution",
        color='churn',
        marginal="box",
        template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Plotly,
        hover_data={'tenure': True, 'total_charges': True}
    )
    fig.update_layout(
        xaxis_title="Monthly Charges ($)",
        yaxis_title="Number of Customers",
        title_font=dict(size=18, family="Segoe UI", color="#111111"),
        legend_title="Churn Status"
    )
    fig.update_traces(
        hovertemplate="<b>Monthly Charges:</b> %{x:$,.2f}<br><b>Count:</b> %{y}<br><b>Tenure:</b> %{customdata[0]} months<br><b>Total Charges:</b> $%{customdata[1]:,.2f}<extra></extra>"
    )
    return fig

def plot_tenure_vs_charges(df):
    fig = px.scatter(
        df,
        x='tenure',
        y='monthly_charges',
        color='churn',
        trendline="ols",
        title="Relationship Between Tenure and Monthly Charges",
        template="plotly_white",
        opacity=0.7,
        color_discrete_sequence=px.colors.qualitative.Plotly,
        hover_data={'gender': True, 'contract': True}
    )
