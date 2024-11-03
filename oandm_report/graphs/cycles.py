import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

months = pd.date_range(start="2023-01-01", periods=12, freq='M').strftime('%B')  # Monthly labels
warranty_value = 42 * 12  # Total warranty cycles for the year
    # Generate random values for actual cycles and make them cumulative
monthly_cycles = np.random.randint(1, 20, size=12)  # Random monthly cycle values between 1 and 20

def warranty_vs_actual_cycles():
    # Sample data for the last 12 months
    cumulative_cycles = np.cumsum(monthly_cycles)  # Cumulative sum for each month

    # Create the Plotly figure
    fig = go.Figure()

    # Add the warranty line
    fig.add_trace(go.Scatter(
        x=months,
        y=[warranty_value / 12 * (i + 1) for i in range(12)],  # Constant cumulative increase
        mode='lines',
        name="Cumulative Warranty",
        line=dict(color='red', width=2)
    ))

    # Add the actual cumulative cycles line
    fig.add_trace(go.Scatter(
        x=months,
        y=cumulative_cycles,
        mode='lines+markers',
        name="Cumulative Actual Cycles",
        line=dict(color='blue', width=2),
        marker=dict(size=6)
    ))

    # Update layout for better readability
    fig.update_layout(
        title="Cumulative Monthly Cycles with Warranty and Actual Cycles",
        xaxis_title="Month",
        yaxis_title="Cumulative Cycles",
        xaxis=dict(tickangle=45),
        yaxis=dict(range=[0, max(warranty_value, max(cumulative_cycles)) + 10]),  # Ensure full range
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,
            xanchor="center",
            x=0.5
        )
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)

def warrant_vs_actual_cycles_table():
    warranty_cycles = [42] * 12
    data = {
        "Actual Cycles": monthly_cycles[3:9],
        "Warranty": warranty_cycles[3:9]
    }

    df = pd.DataFrame(data).T
    df.columns = months[3:9]
    df.index = ["Actual Cycles", "Warranty"]
    return st.table(df)
