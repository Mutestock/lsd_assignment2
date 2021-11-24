from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder


Builder.load_file("interface/screens/generate_check_in_screen.kv")

class GenerateCheckInScreen(Screen):
    def __init__(self, **kw):
        super(GenerateCheckInScreen, self).__init__(**kw)
        

class GenerateCheckIn(Widget):
    
    def __init__(self, **kwargs):
        super(GenerateCheckIn, self).__init__(**kwargs) 
    
    
    def back(self):
        self.parent.parent.current="login"


        