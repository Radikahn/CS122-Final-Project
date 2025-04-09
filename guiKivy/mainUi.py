import kivy
from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.bubble import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
from kivy.config import Config


Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'resizable', '1')


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns of the page

        self.cols = 1
        self.rows = 5

        self.add_widget(Label(text='Create an Account'))
        self.add_widget(TextInput(multiline=False))

        self.add_widget(Label(text='Account Type'))
        self.add_widget(TextInput(multiline=False))

        self.add_widget(Button(text="Make Account"))


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
