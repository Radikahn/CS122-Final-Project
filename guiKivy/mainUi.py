import kivy
from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.bubble import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout


class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.padding = 20
        self.spacing = 40

        self.add_widget(Label(text='Create an Account', font_size=36))
        self.add_widget(TextInput(multiline=False,
                        halign="center", font_size=26))

        self.add_widget(Label(text='Account Type', font_size=36))
        self.add_widget(TextInput(multiline=False,
                        halign="center", font_size=26))

        self.add_widget(Button(text="Make Account"))


class MyApp(App):
    def build(self):

        return MyBoxLayout()


if __name__ == '__main__':
    MyApp().run()
