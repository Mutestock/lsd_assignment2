from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty


Builder.load_file("interface/screens/login.kv")
class LoginScreen(Screen):
    pass
    #username_input = StringProperty("")
    #password_input = StringProperty("")
    #def buttonClicked(self, btn):
    #    self.submit_login_button.text = "clicked!"
    
    

class Login(Widget):
    username_input = StringProperty("")
    password_input = StringProperty("")
    
    def login(self, username_input, password_input):
        print("boop")
        print(self.username_input)
        print(self.password_input)
        print(username_input)
    
    def on_text(self):
        print("boop")
        
    