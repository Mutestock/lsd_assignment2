from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, BooleanProperty
from logic.client import user_client
from models.user import User

Builder.load_file("interface/screens/create_user.kv")


class CreateUserScreen(Screen):
    pass


class UserCreation(Widget):
    def __init__(self, **kwargs):
        super(UserCreation, self).__init__(**kwargs)

    banner = StringProperty("Create New User (Demo only)")
    usr = StringProperty()
    pwd = StringProperty()
    is_teacher = BooleanProperty(False)

    def on_teacher_checkbox_ticked(self):
        self.is_teacher = not self.is_teacher

    def on_usr_change(self, instance):
        self.usr = instance.text

    def on_pwd_change(self, instance):
        self.pwd = instance.text

    def cancel(self):
        self.parent.parent.current = "login"

    def create_user(self):
        if self.usr and self.pwd:
            msg = user_client.create_user(User(self.usr, self.pwd, self.is_teacher)).msg
            if msg == "Err":
                self.banner = "Some Error Occurred. Check duplicate username"
            else:
                self.banner = f"User {self.usr} created"
                
                
