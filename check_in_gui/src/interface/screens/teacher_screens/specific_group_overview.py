from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.app import App

from logic.client import group_client


Builder.load_file("interface/screens/teacher_screens/specific_group_overview.kv")


class SpecificGroupOverviewScreen(Screen):
    pass


# List of attached students. 

class SpecificGroupOverview(Widget):
    def __init__(self, **kwargs):
        super(SpecificGroupOverview, self).__init__(**kwargs)
    
    banner = StringProperty("")

    def to_attach_student_to_group(self):
        self.parent.parent.current = "teacher_stats"
        
    def to_detach_student_from_group(self):
        app = App.get_current_app()
        group_client.remove_student_from_group(app.username, app.group_name)
        
    def to_generate_check_in(self):
        self.parent.parent.current = "generate_check_in"
        
    def sync(self):
        self.banner = App.get_current_app().selected_group_name

    def back(self):
        self.parent.parent.current = "group_overview"
