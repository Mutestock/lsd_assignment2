from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.app import App


Builder.load_file("interface/screens/teacher_screens/group_overview.kv")


class GroupOverviewScreen(Screen):
    
    def __init__(self, **kw):
        super(GroupOverviewScreen, self).__init__(**kw)

# Show controls up top.
# Show all groups below
# Need scrollbar


class GroupButton(Button):
    
    def __init__(self, **kwargs):
        super(GroupButton, self).__init__(**kwargs)
        
    group_name = StringProperty()
    
    def select_group(self):
        app = App.get_running_app()
        app.selected_group_name = self.group_name
        
        



class GroupOverview(Widget):

    def __init__(self, **kwargs):
        super(GroupOverview, self).__init__(**kwargs)

    def to_dashboard(self):
        self.parent.parent.current = "teacher_dashboard"

    def to_create_group(self):
        self.parent.parent.current = "create_group"
        
    def sync(self):
        pass
        #App.get_running_app().attached_groups = 