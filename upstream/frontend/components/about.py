import streamlit as st

def about_tab():
    st.markdown(
        """
        <div style="
            background-color: #1E1E1E;
            padding: 30px;
            border-radius: 10px;
            color: #f0f0f0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
        ">
            <h1 style="text-align: center; color: #007BFF; margin-bottom: 10px;">ℹ️ Customer Churn Dashboard</h1>
            <h3 style="color: #f0f0f0;">Overview</h3>
            <p>
                This dashboard is part of the Customer Churn Prediction project using the Telco Customer Churn dataset from Kaggle.
                It provides data-driven insights into customer churn patterns, empowering decision-makers with actionable strategies to improve customer retention.
            </p>
            <h3 style="color: #f0f0f0;">Key Features</h3>
            <ul>
                <li><strong>🔍 Interactive Filtering:</strong> Dynamically refine the data view using filters for contract type, gender, payment method, internet service, and more.</li>
                <li><strong>📈 Rich Visualizations:</strong> Explore a variety of charts including distribution plots, scatter plots with trendlines, box plots, bar charts, sunburst charts, and correlation heatmaps.</li>
                <li><strong>📊 Segment Analysis:</strong> Break down churn rates by various customer segments to identify trends and patterns.</li>
                <li><strong>💡 Insights & Deep Dive:</strong> View key metrics and actionable insights along with detailed deep-dive analyses.</li>
                <li><strong>🔮 Prediction Tool:</strong> Test a predictive model by entering new customer details to receive churn predictions.</li>
                <li><strong>📥 Data Export:</strong> Easily download the filtered dataset for further offline analysis.</li>
            </ul>
            <h3 style="color: #f0f0f0;">How to Use the Dashboard</h3>
            <p>
                Use the sidebar to apply filters and update visualizations across tabs. Navigate through the <strong>🏠 Overview</strong>, <strong>📊 Insights</strong>, and <strong>🔮 Prediction</strong> tabs to explore different aspects of the data and gain actionable insights.
            </p>
            <h3 style="color: #f0f0f0;">Technical Details</h3>
            <p>
                <strong>Backend:</strong> FastAPI<br>
                <strong>Database:</strong> PostgreSQL<br>
                <strong>Frontend:</strong> Streamlit with Plotly visualizations<br>
                <strong>Containerization:</strong> Docker Compose
            </p>
            <h3 style="color: #f0f0f0;">Future Enhancements</h3>
