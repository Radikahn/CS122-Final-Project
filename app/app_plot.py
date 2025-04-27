import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def dashplot_function(x, account):
    
    monthly_income = account.yearly_income / 12
    monthly_spending = account.monthly_spending
    
    print(f'the monthly income is: {monthly_income}')

    return x + monthly_income - monthly_spending

def dashboard_plot(account):
    
    x = np.linspace(0, 12, 12)

    y = dashplot_function(x, account)
    
    fig = plt.figure(figsize= (10,8))
    
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(x, y)
    ax.set_title(f"{account.username}'s Income Vs Spending (12 Month Span)")
    ax.set_xlabel("Months")
    ax.set_ylabel("Accumilated Earnings")

    #fig.savefig('dashboard.png')
    
    return fig

def feature_plot (framework, account):

    x = np.linspace(0, int(framework.result), 4 * int(framework.result))

    y = framework.plot_func(x, framework, account)

    
    fig = plt.figure(figsize= (10,10))
    
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(x, y)
    ax.set_title(f"{account.username}'s Income Vs Spending")
    ax.set_xlabel("Months")
    ax.set_ylabel("Accumilated Earnings")
    
    return fig

def monthly_projection_plot(x, framework, account):

    monthly_income = account.yearly_income / 12

    monthly_spending = framework.first_input

    return x + monthly_income - monthly_spending


