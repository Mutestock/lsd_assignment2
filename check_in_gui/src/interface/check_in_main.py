from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from interface.screens.login import LoginScreen

Builder.load_file("interface/check_in.kv")

#https://stackoverflow.com/questions/47963198/screen-manager-in-kivy-with-kv-file

class CheckIn(Widget):
    pass

class CheckInApp(App):
    def build(self):
        return CheckIn()
    

if __name__ == '__main__':
    CheckInApp().run()