import streamlit as st
from utils import load_data
from components.sidebar import filter_data
from components.metrics import display_summary_metrics, download_filtered_data
from components.plots import (
    plot_churn_distribution, plot_tenure_boxplot, plot_monthly_charges_histogram,
    plot_tenure_vs_charges, plot_payment_method_breakdown, plot_contract_churn,
    plot_sunburst_chart, plot_internet_service_donut, expander_explanation,
    plot_null_values_heatmap, plot_senior_vs_churn, plot_partner_dependents_vs_churn,
    plot_gender_vs_churn, plot_service_usage_vs_churn, plot_paperlessbilling_vs_churn,
    plot_totalcharges_boxplot, plot_scatter_matrix, plot_kmeans_clusters
)
from components.insights import insights_tab
from components.prediction import prediction_form
from components.about import about_tab

# Set page configuration
st.set_page_config(
    page_title="Customer Churn Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("Customer Churn Dashboard")
    st.markdown("""
    Welcome to the **Customer Churn Dashboard**. This interactive tool allows you to explore key insights from the Telco Customer Churn data.
    Use the sidebar to filter data and switch between tabs for an in-depth look at visualizations, insights, predictions, and more.
    """)

    # Load and filter data once
    data = load_data()
    filtered_data = filter_data(data)

    # Create tabs with icons
    tabs = st.tabs(["🏠 Overview", "📊 Insights", "🔮 Prediction", "ℹ️ About"])

    # --- Overview Tab ---
    with tabs[0]:
        st.header("🏠 Overview")
