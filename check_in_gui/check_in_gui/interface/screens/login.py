from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file("interface/screens/login.kv")
class LoginScreen(Screen):
    pass
    #def buttonClicked(self, btn):
    #    self.submit_login_button.text = "clicked!"
    
    

class Login(Widget):
    def login(self):
        print("boop")