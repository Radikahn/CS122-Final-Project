import pandas as pd
import matplotlib
from user_accounts import UserAccounts
from budget_plan import saving_goal

user = UserAccounts("Radi", "Spending", 100000, 1200)

user.saving_goal()
