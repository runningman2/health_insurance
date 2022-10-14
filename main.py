"""
Main file to run insurance analysis 
"""

import matplotlib.pyplot as plt
from helper_functions.helper_funcs import plot_plans

from insurance_classes import Insurance_plan
from helper_functions import *

# define user inputs
TAX_RATE = 0.32



# create objects for each insurance type
ppo_dict = {'premium': 332, 'deductible': 3300, 'oop_max': 13600, 
            'hsa_limit': 2850, 'company_contribution': 0, 'coinsurance': 0.1}
hdhp_dict = {'premium': 16, 'deductible': 6000, 'oop_max': 20000, 
            'hsa_limit': 7750, 'company_contribution': 1000, 'coinsurance': 0.2}
hdhp_basic_dict = {'premium': 0, 'deductible': 10000, 'oop_max': 26200, 
            'hsa_limit': 7750, 'company_contribution': 1000, 'coinsurance': 0.25}

ppo_object = Insurance_plan(TAX_RATE, 'ppo', **ppo_dict)
hdhp_object = Insurance_plan(TAX_RATE, 'hdhp', **hdhp_dict)
hdhp_basic_object = Insurance_plan(TAX_RATE, 'hdhp_basic', **hdhp_basic_dict)

plot_plans([ppo_object, hdhp_object, hdhp_basic_object], 0, 120000, 10, 'output')