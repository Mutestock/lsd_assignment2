from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file("interface/screens/student_stats.kv")

class StudentStatsScreen(Screen):
    pass

class StudentStats(Widget):
    def __init__(self, **kwargs):
        super(StudentStats, self).__init__(**kwargs)
        
    def to_dashboard(self):
        self.parent.parent.current = "student_dashboard"
        
        
        

