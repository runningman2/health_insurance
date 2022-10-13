"""
Helper functions
"""

import matplotlib.pyplot as plt

def plot_plans(plan_objs, min_spend, max_spend, step_spend):
    """
    Plot plan cost on y axis versus medical spend on x axis

    Args:
        plan_objs (list): List of plan objects to be plotted.
    """
    
    fig, ax = plt.subplots()
    for plan in plan_objs:
        costs, spend = plan.calc_annual_cost(min_spend, max_spend, step_spend)
        ax.plot(spend, costs, label=plan.name)
        
    ax.set_xlabel('Medical spend')
    ax.set_ylabel('Cost ($)')
    ax.set_title('Medical plan comparison')
    ax.legend()