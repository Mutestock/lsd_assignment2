from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file("interface/screens/submit_check_in.kv")

class SubmitCheckInScreen(Screen):
    pass

class SubmitCheckIn(Widget):
    def __init__(self, **kwargs):
        super(SubmitCheckIn, self).__init__(**kwargs)
    
    def to_dashboard(self):
        self.parent.parent.current="student_dashboard"
        
        

