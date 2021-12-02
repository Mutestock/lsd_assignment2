from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from logic.client.student_client import code_check_in
from logic.ip_check import get_public_ip
from kivy.app import App

Builder.load_file("interface/screens/student_screens/submit_check_in.kv")


class SubmitCheckInScreen(Screen):
    pass


class SubmitCheckIn(Widget):
    def __init__(self, **kwargs):
        super(SubmitCheckIn, self).__init__(**kwargs)

    banner = StringProperty("Check In")
    check_in_input = StringProperty()

    def to_dashboard(self):
        self.parent.parent.current = "student_dashboard"

    def on_check_in_change(self, instance):
        self.check_in_input = instance.text

    def submit_check_in(self):
        app = App.get_running_app()
        print(app.username)
        checked_in = code_check_in(
            self.check_in_input, get_public_ip(), app.username).checked_in
        print(checked_in)
        if checked_in:
            self.banner = "Success!"
            print("Succesfully checked in")
        else:
            self.banner = "Failure. Check code"
            print("Failed to check in")
