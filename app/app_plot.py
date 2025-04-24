import matplotlib.pyplot as plt
import seaborn as sns


def dashboard_plot(name: str):

    pass


def testing_plot():

    test_line = sns.lineplot(x=[1, 2, 3, 4], y=[5, 6, 7, 8])

    fig = test_line.get_figure()

    fig.savefig('dashboard.png')
