"""
Insurance plan class. Other classes are derived from this class
"""

class Insurance_plan:
    """
    Base insurance plan class
    """
    def __init__(self, tax_rate=0.35):
        """
        Insurance plan class constructor
        Inputs:
            tax_rate = top marginal tax rate paid by consumer
        """
        self.tax_rate = tax_rate
        
    def calc_annual_cost(self):
        """
        Calculate 1 year of costs 
        """
        pass
        
    def plot_costs(self):
        """
        Plot plan cost on y axis versus medical spend on x axis
        """
        pass