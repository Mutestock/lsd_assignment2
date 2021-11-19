from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, BooleanProperty

Builder.load_file("interface/screens/create_user.kv")

class CreateUserScreen(Screen):
    pass


class UserCreation(Widget):
    def __init__(self,**kwargs):
       super(UserCreation, self).__init__(**kwargs)
    
    usr = StringProperty()
    pwd = StringProperty()
    is_teacher = BooleanProperty(False)
    
    def on_teacher_checkbox_ticked(self):
        self.is_teacher = not self.is_teacher
        print(self.is_teacher)
        print("hi")
        
    
    def on_usr_change(self, instance):
        self.usr = instance.text
    
    def on_pwd_change(self, instance):
        self.pwd = instance.text
    
    def cancel(self):
        pass
        
    def create_user(self):
        pass