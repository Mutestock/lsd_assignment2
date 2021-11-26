from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from models.user import CurrentUser
from kivy.properties import StringProperty


Builder.load_file("interface/screens/teacher_screens/teacher_dashboard.kv")


class TeacherDashboardScreen(Screen):
    pass


class TeacherDashboard(Widget):
    def __init__(self, **kwargs):
        super(TeacherDashboard, self).__init__(**kwargs)

    banner = StringProperty(f"Teacher: {CurrentUser().get_username()}'s page")

    def to_stats(self):
        self.parent.parent.current = "teacher_stats"

    def to_group_overview(self):
        self.parent.parent.current = "group_overview"

    def logout(self):
        self.parent.parent.current = "login"
