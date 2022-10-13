"""
Main file to run insurance analysis 
"""
# from insurance_classes import Insurance_plan
from insurance_classes.specific_plans.ppo_plan import PPO

# define user inputs

# create objects for each insurance type
# ppo_object = PPO(5,6,6,8,9,10)
ppo_object = PPO(0.1,5,6,7,8,9,10)

print(ppo_object.tax_rate)

# calculate costs for each insurance plan over medical spend range

# plot cost vs medical spend