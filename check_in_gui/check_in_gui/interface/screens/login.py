from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


Builder.load_file("interface/screens/login.kv")
class LoginScreen(Screen):
    pass

    def buttonClicked(self, btn):
        self.submit_login_button.text = "clicked!"
    
    def login(self):
        print("hello")
        print(self.user_input.text)