from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty


class LoginScreen(Screen):
    pass

class Login(Widget):
    usr = StringProperty()
    pwd = StringProperty()
    
    def login(self):
        print(self.usr)
        print(self.pwd)
        
    
    def on_usr_change(self, instance):
        self.usr = instance.text
    
    def on_pwd_change(self, instance):
        self.pwd = instance.text
    
        
        
        
    