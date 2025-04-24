import time
import kivy
from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.bubble import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from sqlalchemy.sql.functions import user
from data_management import orm_data
from data_management import user_data
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.uix.image import Image
import app.app_plot as plot

Window.size = (1280, 720)
global_name = str()


class ScreenManagment(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagment, self).__init__(**kwargs)


class MyBoxLayout(BoxLayout, Screen):

    account_name = "Default"
    account_type = "Default"
    # engine = orm_data.create_engine('sqlite:///user_account_data.db')
    # Session = orm_data.sessionmaker(bind=engine)
    # session = Session()

    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

        # database setup
        # database_table = user_data.UserDataTable()

        # orm setup
        self.engine = orm_data.create_engine('sqlite:///user_account_data.db')
        self.Session = orm_data.sessionmaker(bind=self.engine)
        self.session = self.Session()

        self.orientation = "vertical"

        self.padding = 40
        self.spacing = 40

        self.add_widget(Label(text='Create an Account:', font_size=36))

        # create anchor layout for text box, smaller than boxlayout size
        account_name = AnchorLayout(anchor_x='center', anchor_y='center')

        self.account_name_input = TextInput(
            multiline=False, halign="center", font_size=26, hint_text='Enter a Name For Account')
        self.account_name_input.size_hint = (0.5, 0.7)

        account_name.add_widget(self.account_name_input)

        self.add_widget(account_name)

        self.add_widget(Label(text='Account Type:', font_size=36))

        # anchor layout for second input

        account_type = AnchorLayout(anchor_x='center', anchor_y='center')

        self.account_type_input = TextInput(
            multiline=False, halign="center", font_size=26, hint_text='Enter Account Type')
        self.account_type_input.size_hint = (0.5, 0.7)

        account_type.add_widget(self.account_type_input)

        self.add_widget(account_type)

        # Creating a layout for buttons
        button_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        # make a submit button, make sure it is centered and smaller than boxlayout
        create_button = Button(text="Make Account", font_size=20)

        create_button.size_hint = (0.3, 0.7)
        create_button.background_normal = ''
        create_button.background_color = (0.5, 0.2, 1, 0.8)
        create_button.bind(on_press=self.save_info)

        button_layout.add_widget(create_button)

        self.add_widget(button_layout)

# ----------------------Button Functions MyBoxLayout Class-----------------------------------#

    def save_info(self, instance):
        account_name = self.account_name_input.text

        account_type = self.account_type_input.text

        user_data = orm_data.UserData(
            username=account_name, account_type=account_type)

        self.session.add(user_data)

        self.session.commit()

        global global_name
        global_name = self.account_name_input.text

        self.manager.current = 'dashboard'


class Dashboard (BoxLayout, Screen):

    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

        self.padding = 10
        self.spacing = 10

        self.orientation = 'vertical'

        self.engine = orm_data.create_engine('sqlite:///user_account_data.db')
        self.Session = orm_data.sessionmaker(bind=self.engine)
        self.session = self.Session()


# --------------------------------------------------------------------------------------
        # Upper Half of Screen
        # Make the container for top half
        top_layout = BoxLayout(orientation='horizontal')
        top_layout.padding = 1
        top_layout.spacing = 1

        # Left node of Top Half
        self.top_left_node = BoxLayout(orientation='vertical')
        self.top_left_node.padding = 0.5
        self.top_left_node.spacing = 0.5

        self.graph_update = AnchorLayout(anchor_x='center', anchor_y='center')

        self.graph_button = Button(text='')
        self.graph_button.background_normal = 'dashboard.png'
        self.graph_button.background_down = 'dashboard.png'
        self.graph_button.size_hint = (1, 1)
        self.graph_button.padding = 0
        self.graph_button.bind(on_press=self.dash_plot)

        self.graph_update.add_widget(self.graph_button)

        self.top_left_node.add_widget(self.graph_update)

        # Right node of top half
        self.top_right_node = BoxLayout(orientation='vertical')
        self.top_right_node.padding = 5
        self.top_right_node.spacing = 5

        button_right_layout = AnchorLayout(
            anchor_x='center', anchor_y='center')
        yearly_right = AnchorLayout(anchor_x='center', anchor_y='center')
        monthly_right = AnchorLayout(anchor_x='center', anchor_y='center')

        # Update Button
        update_button = Button(text='Update')
        update_button.size_hint = (0.3, 0.35)
        update_button.background_normal = ''
        update_button.background_color = (0.5, 0.2, 1, 0.8)
        update_button.bind(on_press=self.set_income_spend)

        self.yearly_input = TextInput(
            multiline=False, halign='center', font_size=18, hint_text='Yearly Income')
        self.yearly_input.size_hint = (0.5, 0.5)
        yearly_right.add_widget(self.yearly_input)

        self.monthly_input = TextInput(
            multiline=False, halign='center', font_size=18, hint_text='Monthly Spending')
        self.monthly_input.size_hint = (0.5, 0.5)
        monthly_right.add_widget(self.monthly_input)

        button_right_layout.add_widget(update_button)

        self.top_right_node.add_widget(Label(text='Yearly Income:'))
        self.top_right_node.add_widget(yearly_right)
        self.top_right_node.add_widget(Label(text='Monthly Spending:'))
        self.top_right_node.add_widget(monthly_right)
        self.top_right_node.add_widget(button_right_layout)

        top_layout.add_widget(self.top_left_node)
        top_layout.add_widget(self.top_right_node)


# ------------------------------------------------------------------------------------------#

        # Bottom Half
        bottom_layout = BoxLayout(orientation='horizontal')

        # Left node of Bottom Half
        bottom_left_node = BoxLayout(orientation='vertical')
        bottom_left_node.add_widget(Label(text='Left Node'))

        # Right node of Bottom half
        bottom_right_node = BoxLayout(orientation='vertical')
        bottom_right_node.add_widget(Label(text='Right Node'))

        bottom_layout.add_widget(bottom_left_node)
        bottom_layout.add_widget(bottom_right_node)

        self.add_widget(top_layout)
        self.add_widget(bottom_layout)


# ----------------------Button Functions For Dashboard Class-----------------------------------#

    def set_income_spend(self, instance):

        warning = Label(text='hello')

        try:
            self.top_right_node.remove_widget(warning)
        except Exception as e:
            pass

        global global_name
        curr_user = global_name

        yearly = self.yearly_input.text

        monthly = self.monthly_input.text

        try:

            print(yearly)

            if yearly == '':
                raise Exception

            elif monthly == '':
                raise Exception

            yearly = int(yearly)
            monthly = int(monthly)

            update_income = orm_data.update(orm_data.UserData).where(
                orm_data.UserData.username == curr_user).values(yearly_income=yearly)

            update_spending = orm_data.update(orm_data.UserData).where(
                orm_data.UserData.username == curr_user).values(monthly_spending=monthly)

            self.session.execute(update_income)
            self.session.execute(update_spending)

            self.session.commit()

        except Exception as e:
            warning = Label(text='Must be a Number & No Empty Fiels')

            warning.font_size = 18

            warning.color = (1, 0, 0, 1)

            self.top_right_node.add_widget(warning)

            # self.top_right_node.remove_widget(warning)

    def dash_plot(self, instance):

        plot.testing_plot()

        print("i am here")

        self.graph_button.background_normal = 'dashboard.png'

        self.graph_button.background_down = 'dashboard.png'


class MyApp(App):
    def build(self):
        sm = ScreenManagment(transition=FadeTransition())
        sm.add_widget(MyBoxLayout(name='register'))
        sm.add_widget(Dashboard(name='dashboard'))
        return sm


if __name__ == '__main__':
    MyApp().run()
