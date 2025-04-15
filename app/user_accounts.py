import budget_plan as bp
from guiKivy import mainUi

# decorator func to log actions of session into log file


def logAppend(func):
    def wrapper(*args, **kwargs):
        with open('log_file.txt', 'w+') as file:
            message = f"Exec: {func}"
            file.write(message)
            result = func(*args, **kwargs)
            return result
    return wrapper


class UserAccounts:

    username: str
    yearly_income: float
    account_type: str
    monthly_spending: float

    def __init__(self, username: str, account_type: str, income: float, monthly_spending: float) -> None:

        # Assign user values to class attributes
        self.username = username
        self.yearly_income = income
        self.account_type = account_type
        self.monthly_spending = monthly_spending
        # initialize log file for current session
        open('log_file.txt', 'w+')

    @logAppend
    def change_name(self, name):
        self.username = name

    @logAppend
    def saving_goal(self):
        goal = 10000
        amount_saved = 1000

        days = bp.saving_goal(self, self.monthly_spending, goal, amount_saved)

        print(days)
