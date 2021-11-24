from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from interface.screens.login import LoginScreen
from interface.screens.student_dashboard import StudentDashboardScreen
from interface.screens.teacher_dashboard import TeacherDashboardScreen
from interface.screens.create_user import CreateUserScreen
from interface.screens.about import AboutScreen
from interface.screens.submit_check_in import SubmitCheckInScreen
from interface.screens.student_stats import StudentStatsScreen

Builder.load_file("interface/check_in.kv")

#https://stackoverflow.com/questions/47963198/screen-manager-in-kivy-with-kv-file

class CheckIn(Widget):
    pass

class CheckInApp(App):
    def build(self):
        return CheckIn()
    