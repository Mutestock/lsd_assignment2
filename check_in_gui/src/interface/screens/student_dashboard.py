from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from models.user import CurrentUser
from kivy.properties import StringProperty


Builder.load_file("interface/screens/student_dashboard.kv")

class StudentDashboardScreen(Screen):
    pass

class StudentDashboard(Widget):
    def __init__(self, **kwargs):
        super(StudentDashboard, self).__init__(**kwargs)
    
    banner = StringProperty(f"{CurrentUser().get_username()}'s page")
    
    def to_stats(self):
        self.parent.parent.current="student_stats"
    
    def to_check_in(self):
        self.parent.parent.current="submit_check_in"
        
    def logout(self):
        self.parent.parent.current="login"

