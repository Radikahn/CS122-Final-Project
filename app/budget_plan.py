import user_accounts
from BudgetExceptions import *


def saving_goal(account, monthly_spending, goal, amount_saved):

    income = account.yearly_income / 12

    dividend = income - monthly_spending

    dividend -= amount_saved  # new divident is amount they are choosing to save per week

    if dividend <= 0:
        raise ZeroNegativeError(
            "[ERROR]: The savings dividend per month is either 0 or Negative")

    return goal / dividend
