from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from logic.client import user_client


class LoginScreen(Screen):    
    def __init__(self,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)
    
    
class Login(Widget):
    def __init__(self,**kwargs):
        super(Login, self).__init__(**kwargs)
    
    usr = StringProperty()
    pwd = StringProperty()
    banner = StringProperty("Please login")
    
    def login(self):
        if user_client.login(self.usr,self.pwd).login_successful:
            self.banner = "Login success."
            print("login successful!")    
        else:
            self.banner = "Login failed. Check credentials"
        
    def on_usr_change(self, instance):
        self.usr = instance.text
    
    def on_pwd_change(self, instance):
        self.pwd = instance.text
    
    def swap_to_create_user_screen(self):
        self.parent.parent.current="create_user"
        
    def swap_to_about(self):
        self.parent.parent.current="about"
