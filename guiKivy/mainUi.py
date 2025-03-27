import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):

    def __init__(self, **kwargs):

        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="nothing"))


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
