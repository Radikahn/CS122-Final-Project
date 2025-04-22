from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)


class RegisterWindow(Screen):
    def __init__(self, **kwargs):
        super(RegisterWindow, self).__init__(**kwargs)
        self.add_widget(
            Label(text='Username', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .7}))
        self.username = TextInput(
            multiline=False, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .7})
        self.add_widget(self.username)
        self.add_widget(
            Label(text='Password', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .5}))
        self.password = TextInput(
            multiline=False, password=True, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .5})
        self.add_widget(self.password)
        self.add_widget(Label(text='E-mail', size_hint=(.45, .1),
                        pos_hint={'x': .05, 'y': .3}))
        self.email = TextInput(
            multiline=False, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .3})
        self.add_widget(self.email)
        self.btn = Button(text='Register', size_hint=(.9, .2),
                          pos_hint={'center_x': .5, 'y': .03})
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.submit)

    def submit(self, instance):
        username = self.username.text
        password = self.password.text
        email = self.email.text

        info = {'Username': username,
                'Password': password,
                'Email': email}
        print(info)


class LoginWindow(Screen):
    def __init__(self, **kwargs):
        super(LoginWindow, self).__init__(**kwargs)
        self.btn2 = Button(text='Go')
        self.add_widget(self.btn2)
        self.btn2.bind(on_press=self.screen_transition)

    def screen_transition(self, *args):
        self.manager.current = 'register'


class Application(App):
    def build(self):
        sm = ScreenManagement(transition=FadeTransition())
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(RegisterWindow(name='register'))
        return sm


if __name__ == "__main__":
    Application().run()
