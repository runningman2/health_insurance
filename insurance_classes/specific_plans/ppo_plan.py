"""
Classes for specific insurance plans
"""
from insurance_classes import Insurance_plan

class PPO(Insurance_plan):
    """
    PPO insurance plan class
    """
    
    def __init__(self, tax_rate, premium, deductible, oop_max, hcsa_limit, company_contributions, coinsurance):
        """
        Constructor for PPO insurance plan class

        Args:
            tax_rate (float): Top marginal tax rate paid by consumer
            premium (float): Monthly insurance premium
            deductible (float): Annual deductible
            oop_max (float): Annual out of pocket maximum 
            hcsa_limit (float): Annual health care spending account contribution limit
            company_contributions (float): Annual company contribution to spending account
            coinsurance (float): Fraction paid by consumer after deductible met
        """
        
        super().__init__(tax_rate)
        
        self.premium = premium
        self.deductible = deductible
        self.oop_max = oop_max
        self.hcsa_limit = hcsa_limit
        self.company_contributions = company_contributions
        self.coinsurance = coinsurance