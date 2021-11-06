from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from interface.screens.login import LoginScreen

Builder.load_file("interface/check_in.kv")

class CheckIn(Widget):
    pass

class CheckInApp(App):
    def build(self):
        return CheckIn()
    

if __name__ == '__main__':
    CheckInApp().run()