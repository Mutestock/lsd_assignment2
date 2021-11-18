from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty
from logic.client import user_client


class LoginScreen(Screen):
    pass

class Login(Widget):
    usr = StringProperty()
    pwd = StringProperty()
    banner = StringProperty("Please login")
    
    def login(self):
        if user_client.login(self.usr,self.pwd).login_successful:
            print("login successful!")
            
        else:
            self.banner = "Login failed. Check credentials"
        
        
    def on_usr_change(self, instance):
        self.usr = instance.text
    
    def on_pwd_change(self, instance):
        self.pwd = instance.text
    
        
        
        
    