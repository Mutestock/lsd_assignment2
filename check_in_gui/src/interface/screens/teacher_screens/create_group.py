from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from logic.client.group_client import create_group
from kivy.app import App

Builder.load_file("interface/screens/teacher_screens/create_group.kv")


class CreateGroupScreen(Screen):
    pass


class CreateGroup(Widget):
    def __init__(self, **kwargs):
        super(CreateGroup, self).__init__(**kwargs)

    group_name_input = StringProperty()
    banner = StringProperty("Create group")

    def to_dashboard(self):
        self.parent.parent.current = "group_overview"

    def on_group_name_change(self, instance):
        self.group_name_input = instance.text

    def submit_group_name(self):
        if self.group_name_input == "":
            self.banner = "Group name can't be empty"
        else:
            app = App.get_running_app()
            msg = create_group(self.group_name_input, app.username)
