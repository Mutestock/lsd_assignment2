from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file("interface/screens/teacher_screens/teacher_stats.kv")


class TeacherStatsScreen(Screen):
    pass


class TeacherStats(Widget):
    def __init__(self, **kwargs):
        super(TeacherStats, self).__init__(**kwargs)

    def to_dashboard(self):
        self.parent.parent.current = "teacher_dashboard"
