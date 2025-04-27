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
from app.user_accounts import UserAccounts
import app.budget_plan as budget
import app.app_plot as plting
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg


Window.size = (1280, 720)

#create an instance of the UserAccount class
global_account = UserAccounts()
global_account_name = str()
global_account_type = str()

class ScreenManagment(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagment, self).__init__(**kwargs)


class MyBoxLayout(BoxLayout, Screen):

    account_name = "Default"
    account_type = "Default"


    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

        #database setup
        #database_table = user_data.UserDataTable()

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


        global global_account

        global_account.username = self.account_name_input.text
        global_account.account_type = self.account_type_input.text
        
        global_account_name = global_account.username
        global_account_type = global_account.account_type

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

        self.dash_graph = Image(source = 'start.png')
        self.graph_update.add_widget(self.dash_graph)
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
        bottom_left_node = BoxLayout(orientation='horizontal')
        bottom_left_node.padding = 10
        bottom_left_node.spacing = 10


        monthly_projection = Button(text = 'Monthly Projections')
        monthly_projection.background_normal = ''
        monthly_projection.background_color = (0.5, 0.2, 1, 0.8)
        monthly_projection.bind(on_press = self.screen_swtich_to)


        saving_target = Button(text = 'Savings Target')
        saving_target.background_normal = ''
        saving_target.background_color = (0.5, 0.2, 1, 0.8)
        saving_target.bind(on_press = self.screen_swtich_to)

        bottom_left_node.add_widget(monthly_projection)
        bottom_left_node.add_widget(saving_target)

        # Right node of Bottom half
        bottom_right_node = BoxLayout(orientation='horizontal')
        bottom_right_node.spacing = 10
        bottom_right_node.padding = 10


        savings_projection = Button(text = 'Savings Projection')
        savings_projection.background_normal = ''
        savings_projection.background_color = (0.5, 0.2, 1, 0.8)
        savings_projection.bind(on_press = self.screen_swtich_to)

        account_settings = Button(text = 'Account Settings')
        account_settings.background_normal = ''
        account_settings.background_color = (0.5, 0.2, 1, 0.8)
        account_settings.bind(on_press = self.screen_swtich_to)

        bottom_right_node.add_widget(savings_projection)
        bottom_right_node.add_widget(account_settings)

        bottom_layout.add_widget(bottom_left_node)
        bottom_layout.add_widget(bottom_right_node)

        self.add_widget(top_layout)
        self.add_widget(bottom_layout)

# ----------------------Button Functions For Dashboard Class-----------------------------------#

    def show_error(self):

        try:
            self.top_right_node.remove_widget(self.warning)

        except Exception as e:
            pass

    
    def dash_plot(self, instance):
        
        global global_account

        print(global_account.username)

        try:    
            self.graph_update.remove_widget(self.dash_graph)
            self.top_left_node.remove_widget(self.graph_update)

        
        except Exception as e:
            print(e)
            pass
        
        finally:
            fig = plot.dashboard_plot(global_account)

            self.graph_update = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
            self.dash_graph = FigureCanvasKivyAgg(fig)
        
            self.graph_update.add_widget(self.dash_graph)

            self.top_left_node.add_widget(self.graph_update)


    def set_income_spend(self, instance):

        yearly = self.yearly_input.text

        monthly = self.monthly_input.text

        global global_account
        curr_user = global_account.username


        try:

            print(yearly)

            if yearly == '':
                raise Exception

            elif monthly == '':
                raise Exception

            yearly = float(yearly)
            monthly = float(monthly)

            update_income = orm_data.update(orm_data.UserData).where(
                orm_data.UserData.username == curr_user).values(yearly_income=yearly)

            update_spending = orm_data.update(orm_data.UserData).where(
                orm_data.UserData.username == curr_user).values(monthly_spending=monthly)

            self.session.execute(update_income)
            self.session.execute(update_spending)

            self.session.commit()
            
    

            global_account.yearly_income = yearly
            global_account.monthly_spending = monthly
            

            self.dash_plot(instance)

        except Exception as e:
            
            print(e)

            self.show_error()

            self.warning = Label(text='Must be a Number & No Empty Fiels')

            self.warning.font_size = 18

            self.warning.color = (1, 0, 0, 1)

            self.top_right_node.add_widget(self.warning)


    def screen_swtich_to (self, instance):

        self.manager.current = instance.text

#--------------------------Feature Screen Template---------------------------#

class FeatureScreen(BoxLayout, Screen):

    def __init__(self, **kwargs):
        super(FeatureScreen, self).__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.padding = 0
        self.spacing = 0
        self.graph_name = 'dashboard.png'
        self.func = budget.monthly_projection 
        self.plot_func = plting.monthly_projection_plot
        self.button_func = self.set_params
        self.display_text = '' 
        self.engine = orm_data.create_engine('sqlite:///user_account_data.db')
        self.Session = orm_data.sessionmaker(bind=self.engine)
        self.session = self.Session()


        self.return_button = Button(text = 'Back to Dashboad')
        self.return_button.background_normal = ''
        self.return_button.background_color = (0.5, 0.2, 1, 0.8)
        self.return_button.size_hint = (1, 0.1)
        self.return_button.padding = 10
        self.return_button.bind(on_press = self.return_to_dash)

        self.graph_container = AnchorLayout(anchor_x = 'center', anchor_y = 'top')
        self.graph = Label(text = 'Input Data in Fields to See a Result')
        self.graph.font_size = 32
        self.graph_container.add_widget(self.graph)


        self.menu_page = BoxLayout(orientation = 'horizontal')
        self.menu_page.padding = 15
        self.menu_page.spacing = 15

        self.left_input = TextInput(multiline=False, halign='center', font_size=18, hint_text='Monthly Spending')
        self.left_input.size_hint = (0.3, 0.2)
        self.menu_page.add_widget(self.left_input)
       

        self.right_input = TextInput(multiline=False, halign='center', font_size=18, hint_text='Saving Goal')
        self.right_input.size_hint = (0.3, 0.2) 
        self.menu_page.add_widget(self.right_input)


        self.submit_button  = Button(text = 'See My Goal')
        self.submit_button.size_hint = (1, 0.2)
        

        self.add_widget(self.return_button)
        self.add_widget(self.graph_container)
        self.add_widget(self.menu_page)
        self.add_widget(self.submit_button)


    def return_to_dash(self, instance):
        self.manager.current = 'dashboard' 


    def update_graph(self, instance):


        try:
            self.graph_container.remove_widget(self.graph)
            
        
        except Exception as e:
            print(e)
            pass

        finally:
            fig = plot.feature_plot(self, global_account)
            self.graph = FigureCanvasKivyAgg(fig)
            self.graph.size_hint = (0.5,1)
            self.graph_container.add_widget(self.graph)
 
    def set_params(self, instance):
        
        global global_account

        self.first_input = float(self.left_input.text)
        self.second_input = float(self.right_input.text)

        self.result = self.func(global_account, self.first_input, self.second_input)

        self.update_graph(instance)
    
    def update_info(self, instance):

        global global_account

        print('in here')
        
        try:
            self.graph_container.remove_widget(self.graph)
        except Exception as e:
            print(e)
            pass
        
        finally:
            self.result = self.func(global_account, int(self.left_input.text), int(self.right_input.text))

            self.display_text += f'{self.result:.2f}'

            self.graph = Label(text = self.display_text)
            self.graph.font_size = 32

            self.graph_container.add_widget(self.graph)
           
    def update_user(self, instance):
        
        try:
            self.graph_container.remove_widget(self.graph)
            
        except Exception as e:
            pass

        finally:
            self.display_text = f'Current Username: {global_account.username}\n Current Account Type: {global_account.account_type}'


            self.graph = Label(text = self.display_text)
            self.graph.font_size = 32
            self.graph_container.add_widget(self.graph)



    def account_settings(self, instance):
        global global_account

        if len(self.left_input.text) > 0:
            

            curr_user = global_account.username

            update_username = orm_data.update(orm_data.UserData).where(orm_data.UserData.username == curr_user).values(username=self.left_input.text)

            self.session.execute(update_username)
            self.session.commit() 

            global_account.change_name(self.left_input.text)
            

        if len(self.right_input.text) > 0:

            curr_user = global_account.username

            update_account_type = orm_data.update(orm_data.UserData).where(orm_data.UserData.username == curr_user).values(account_type=self.right_input.text)

            self.session.execute(update_account_type)
            self.session.commit() 

            global_account.change_account_type(self.right_input.text)

        self.update_user(instance) 


#---------------------------Feature Prediction Screens-------------------------------#

class MonthlyPrediction(FeatureScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.left_input.hint_text = 'Planned Monthly Spending'
        self.right_input.hint_text = 'Goal in Dollars'
        self.func = budget.monthly_projection
        self.plot_func = plting.monthly_projection_plot
        self.button_func = self.set_params
        self.submit_button.bind(on_press = self.button_func)

class SavingTarget(FeatureScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

        self.left_input.hint_text = 'Goal In Dollars'
        self.right_input.hint_text = 'Number of Months'
        self.func = budget.saving_target
        self.button_func = self.update_info
        self.submit_button.bind(on_press = self.button_func)
        
        self.display_text = 'You need to save /per month: $' 

class SavingsProjection(FeatureScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.left_input.hint_text = 'Monthly Spending'

        self.right_input.hint_text =  'Number of Months'
        
        self.func = budget.savings_projection
        
        self.submit_button.bind(on_press = self.update_info)
    

        self.display_text = 'You will save a total of: $' 


class AccountSettings(FeatureScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.graph_container.remove_widget(self.graph)
        
        self.display_text = f'Enter Whichever Field You Would Like to Change\n(Fields Can Be Left Blank)'
        self.graph = Label(text = self.display_text)
        self.graph.font_size = 32

        self.graph_container.add_widget(self.graph)

        self.left_input.hint_text = 'New Account Name'
        self.right_input.hint_text = 'New Account Type'
        self.func = self.account_settings
        self.submit_button.text = 'Change Details'
        self.submit_button.bind(on_press = self.func)

       
        

class MyApp(App):
    def build(self):
        sm = ScreenManagment(transition=FadeTransition())
        sm.add_widget(MyBoxLayout(name='register'))
        sm.add_widget(Dashboard(name='dashboard'))
        sm.add_widget(MonthlyPrediction(name = 'Monthly Projections'))
        sm.add_widget(SavingTarget(name = 'Savings Target'))
        sm.add_widget(SavingsProjection(name = 'Savings Projection'))
        sm.add_widget(AccountSettings(name = 'Account Settings'))
        return sm


if __name__ == '__main__':
    MyApp().run()
