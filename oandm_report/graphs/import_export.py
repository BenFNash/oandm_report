import streamlit as st
import plotly.graph_objects as go
import pandas as pd

dates_september = pd.date_range(start="2023-09-01", end="2023-09-30")
import_september = [14 + i % 5 for i in range(len(dates_september))]
export_september = [7 + (i % 3) for i in range(len(dates_september))]
availability = [20 + i % 2 for i in range(len(dates_september))]

# Data for the last 3 months summary
months = ["July", "August", "September"]
total_import = [300, 320, sum(import_september)]  # Example totals
total_export = [180, 200, sum(export_september)]  # Example totals
    
def import_export_bars():
# Sample data for daily data in September and monthly summary for the last 3 months

    # Creating the September daily data chart
    fig_september = go.Figure()

    fig_september.add_trace(go.Bar(
        x=dates_september,
        y=import_september,
        name="Actual Import (Meter)",
        marker_color='indianred'
    ))

    fig_september.add_trace(go.Bar(
        x=dates_september,
        y=export_september,
        name="Export",
        marker_color='lightskyblue'
    ))

    fig_september.update_layout(
        title="Daily Energy Import and Export for September",
        xaxis_title="Date",
        yaxis_title="Energy (kWh)",
        barmode='group',  # Group bars side-by-side
        xaxis_tickformat='%d-%m',  # Show dates in day-month format
        xaxis=dict(tickvals=dates_september[::3], tickangle=45),  # Reduce tick frequency for readability
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,
            xanchor="center",
            x=0.5
        )
    )

    st.plotly_chart(fig_september)

def import_export_summary():
    # Creating the monthly summary bar chart
    fig_summary = go.Figure()

    fig_summary.add_trace(go.Bar(
        x=months,
        y=total_import,
        name="Actual Import (Meter)",
        marker_color='indianred'
    ))

    fig_summary.add_trace(go.Bar(
        x=months,
        y=total_export,
        name="Export",
        marker_color='lightskyblue'
    ))

    fig_summary.update_layout(
        title="Monthly Summary of Energy Import and Export",
        xaxis_title="Month",
        yaxis_title="Total Energy (kWh)",
        barmode='group',  # Group bars side-by-side
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5
        )
    )

    # Display the charts in Streamlit
    st.plotly_chart(fig_summary)


def import_export_bars_with_av():
    # Sample data for daily data in September and monthly summary for the last 3 months

    # Creating the September daily data chart
    fig_september = go.Figure()

    fig_september.add_trace(go.Bar(
        x=dates_september,
        y=import_september,
        name="Actual Import (Meter)",
        marker_color='indianred'
    ))

    fig_september.add_trace(go.Bar(
        x=dates_september,
        y=export_september,
        name="Export",
        marker_color='lightskyblue'
    ))

    # Add the availability line on top
    fig_september.add_trace(go.Scatter(
        x=dates_september,
        y=availability,
        mode='lines',
        name="Availability",
        line=dict(color='green', width=2)
    ))

    fig_september.update_layout(
        title="Daily Energy Import and Export for September",
        xaxis_title="Date",
        yaxis_title="Energy (kWh)",
        barmode='group',  # Group bars side-by-side
        xaxis_tickformat='%d-%m',  # Show dates in day-month format
        xaxis=dict(tickvals=dates_september[::3], tickangle=45),  # Reduce tick frequency for readability
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,
            xanchor="center",
            x=0.5
        )
    )

    st.plotly_chart(fig_september)
