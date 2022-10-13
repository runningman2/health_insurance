"""
Helper functions
"""

import matplotlib.pyplot as plt
import plotly.graph_objects as go

def plot_plans(plan_objs, min_spend, max_spend, step_spend):
    """
    Plot plan cost on y axis versus medical spend on x axis

    Args:
        plan_objs (list): List of plan objects to be plotted.
    """
    
    fig, ax = plt.subplots()
    fig2 = go.Figure()
    for plan in plan_objs:
        costs, spend = plan.calc_annual_cost(min_spend, max_spend, step_spend)
        ax.plot(spend, costs, label=plan.name)
        fig2.add_trace(go.Scatter(x=spend, y=costs, name=plan.name, mode='lines'))
        
        
    ax.set_xlabel('Medical spend')
    ax.set_ylabel('Cost ($)')
    ax.set_title('Medical plan comparison')
    ax.legend()
    
    fig2.update_layout(title='Medical plan comparison', xaxis_title='Medical spend',
                       yaxis_title='Cost ($)')
    fig2.show()
    
