"""
Insurance plan class. Other classes are derived from this class
"""

class Insurance_plan:
    """
    Base insurance plan class
    """
    def __init__(self, tax_rate, name, premium, deductible, oop_max, hsa_limit, 
                 company_contribution, coinsurance):
        """
        Insurance plan class constructor
        Inputs:
            tax_rate = top marginal tax rate paid by consumer
        """
        self.tax_rate = tax_rate
        self.premium = premium
        self.deductible = deductible
        self.oop_max = oop_max
        self.hsa_limit = hsa_limit
        self.company_contributions = company_contribution
        self.coinsurance = coinsurance
        self.name = name
        
    def calc_annual_cost(self, min_spend=0, max_spend=100000, step_size=10):
        """
        Calculate 1 year of costs 
        Returns:
            cost_list = total cost for 1 year, each index corresponds to spend in spend_list
            spend_list = total spend for 1 year, each index corresponds to cost in cost_list
        """
        # savings
        annual_tax_savings = self.tax_rate * self.hsa_limit
        annual_contributions = self.company_contributions
        
        # costs
        annual_prem = self.premium * 12

        # calculate costs over a range of medical spend amts
        spend_list = list(range(min_spend, max_spend, step_size))
        cost_list = []
        for spend in spend_list:
            if spend < self.deductible:
                annual_spend = spend
            else:
                annual_spend = self.deductible + self.coinsurance * (spend-self.deductible)
                
                # annual spend must be less than out of pocket max
                annual_spend = min(annual_spend, self.oop_max)
            
            # add a cost for each spend
            annual_cost = annual_prem + annual_spend - annual_tax_savings - annual_contributions
            cost_list.append(annual_cost)
            
        return cost_list, spend_list
        
    def plot_costs(self):
        """
        Plot plan cost on y axis versus medical spend on x axis
        """
        pass