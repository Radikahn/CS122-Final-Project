import app.budget_plan as bp
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

   #def __init__(self, username: str, account_type: str, income: float, monthly_spending: float) -> None:

        # Assign user values to class attributes
        #self.username = username
       # self.yearly_income = income
        #self.account_type = account_type
        #self.monthly_spending = monthly_spending
        # initialize log file for current session
        #open('log_file.txt', 'w+')

    def __init__(self):
        open('log_file.txt', 'w+')


    @logAppend
    def change_name(self, name):
        self.username = name

    @logAppend
    def change_account_type(self, account_type):
        self.account_type = account_type

    @logAppend
    def saving_goal(self, goal:float):

        month_projection = bp.monthly_projection(self, self.monthly_spending, goal)

        return f"It will take {month_projection} months to save ${goal}."

    @logAppend
    def time_goal(self, month_goal: int, saving_goal: float):
        
        saving_amount, budget = bp.saving_target(self, saving_goal, month_goal)

        return f"Save: ${saving_amount:.2f} per month to reach your goal in time.Your monthly spending budget is: ${budget:.2f}"

    @logAppend
    def saving_projection(self, time_frame: int):

        amount_saved = bp.savings_projection(self, self.monthly_spending, time_frame)

        return f"Over {time_frame} months, you will have ${amount_saved:.2f} saved up."
