import app.user_accounts
from app.BudgetExceptions import *

#calculates how many months of saving to reach desired savings goal
def monthly_projection(account, monthly_spending, goal):

    monthly_income = account.yearly_income / 12

    dividend = monthly_income - monthly_spending

    if dividend <= 0:
        raise ZeroNegativeError(
            "[ERROR]: The savings dividend per month is either 0 or Negative")

    return goal / dividend

#calculates recommended monthly saving amount and spending budget given inputted goals and income
def saving_target(account, saving_goal, time_goal):
    monthly_income = account.yearly_income / 12

    rec_saving = saving_goal / time_goal

    remainder = monthly_income - rec_saving

    return rec_saving, remainder

#calculates total saved given inputted monthly income and timeframe
def savings_projection(account, monthly_spending, timeframe):
    monthly_income = account.yearly_income / 12

    dividend = monthly_income - monthly_spending

    if dividend <= 0:
        raise ZeroNegativeError(
            "[ERROR]: The savings dividend per month is either 0 or Negative")

    return dividend * timeframe
