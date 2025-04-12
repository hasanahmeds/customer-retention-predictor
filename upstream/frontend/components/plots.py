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
    fig.update_layout(
        xaxis_title="Tenure (Months)",
        yaxis_title="Monthly Charges ($)",
        title_font=dict(size=18, family="Segoe UI", color="#111111"),
        legend_title="Churn Status",
        hovermode="closest"
    )
    fig.update_traces(
        marker=dict(size=10, symbol="circle"),
        hovertemplate="<b>Tenure:</b> %{x} months<br><b>Monthly Charges:</b> $%{y:.2f}<br><b>Gender:</b> %{customdata[0]}<br><b>Contract:</b> %{customdata[1]}<extra></extra>"
    )
    return fig

def plot_churn_distribution(df):
    churn_counts = df['churn'].value_counts().reset_index()
    churn_counts.columns = ['churn', 'count']
    fig = px.pie(
        churn_counts,
        names='churn',
        values='count',
        title="Churn Distribution",
        hole=0.4,
        template="plotly_white"
    )
    fig.update_traces(textinfo='percent+label')
    return fig

def plot_tenure_boxplot(df):
    fig = px.box(
        df,
        x='churn',
        y='tenure',
        title="Tenure Distribution by Churn",
        template="plotly_white"
    )
    fig.update_layout(
        xaxis_title="Churn",
        yaxis_title="Tenure (Months)",
        title_font=dict(size=18, family="Segoe UI", color="#111111")
    )
