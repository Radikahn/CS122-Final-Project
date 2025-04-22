import kivy
from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.bubble import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from data_management import orm_data


class MyBoxLayout(BoxLayout):

    account_name = "Default"
    account_type = "Default"
    engine = orm_data.create_engine('sqlite:///user_account_data.db')
    Session = orm_data.sessionmaker(bind=engine)
    session = Session()



    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.padding = 40
        self.spacing = 40

        self.add_widget(Label(text='Create an Account:', font_size=36))

        # create anchor layout for text box, smaller than boxlayout size
        account_name = AnchorLayout(anchor_x='center', anchor_y='center')

        self.account_name_input = TextInput(
            multiline=False, halign="center", font_size=26, hint_text='Enter a Name For Account')
        self.account_name_input.size_hint = (0.75, 0.90)

        account_name.add_widget(self.account_name_input)

        self.add_widget(account_name)

        self.add_widget(Label(text='Account Type:', font_size=36))

        # anchor layout for second input

        account_type = AnchorLayout(anchor_x='center', anchor_y='center')

        self.account_type_input = TextInput(
            multiline=False, halign="center", font_size=26, hint_text='Enter Account Type')
        self.account_type_input.size_hint = (0.75, 0.90)

        account_type.add_widget(self.account_type_input)

        self.add_widget(account_type)

        # Creating a layout for buttons
        button_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        # make a submit button, make sure it is centered and smaller than boxlayout
        create_button = Button(text="Make Account", font_size=20)

        create_button.size_hint = (0.5, 1)
        create_button.background_normal = ''
        create_button.background_color = (0.5, 0.2, 1, 0.8)
        create_button.bind(on_press=self.save_info)

        button_layout.add_widget(create_button)

        self.add_widget(button_layout)

    def save_info(self, instance):
        account_name = self.account_name_input.text

        account_type = self.account_type_input.text

        user_data = orm_data.UserData(
            username=account_name, account_type=account_type)
        
        self.session.add(user_data)

class MyApp(App):
    def build(self):

        return MyBoxLayout()


if __name__ == '__main__':
    MyApp().run()
