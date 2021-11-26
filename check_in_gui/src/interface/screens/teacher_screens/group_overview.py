from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder


Builder.load_file("interface/screens/teacher_screens/group_overview.kv")

class GroupOverviewScreen(Screen):
    def __init__(self, **kw):
        super(GroupOverviewScreen, self).__init__(**kw)
        

class GroupOverview(Widget):
    
    def __init__(self, **kwargs):
        super(GroupOverview, self).__init__(**kwargs) 
    
    
    def to_dashboard(self):
        self.parent.parent.current="teacher_dashboard"
        
    def to_create_group(self):
        self.parent.parent.current="create_group"


        