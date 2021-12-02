from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from logic.client import group_client


Builder.load_file("interface/screens/teacher_screens/specific_group_overview.kv")


class SpecificGroupOverviewScreen(Screen):
    pass

class DetachButton(Button):
    
    usr = StringProperty("")
    
    def __init__(self, usr, **kwargs):
        super(DetachButton, self).__init__(**kwargs)
        self.usr = usr
    
    def detach_student_from_group(self):
        app = App.get_running_app()
        group_client.remove_student_from_group(self.usr, app.selected_group_name)
    

class SubGrid(GridLayout):
    
    usr = StringProperty("")
    
    def __init__(self, usr, **kwargs):
        super(SubGrid, self).__init__(**kwargs)
        self.usr = usr
        self.add_widget(DetachButton(usr=self.usr))
        
    
        

class StudentGrid(GridLayout):
    def __init__(self, **kwargs):
        super(StudentGrid, self).__init__(**kwargs)
        
    def sync(self, instance):
        app = App.get_running_app()
        self.clear_widgets()
        panel = BoxLayout(orientation="vertical")
        grid = GridLayout(cols=1,row_force_default=True, row_default_height=panel.height/2)
        panel.add_widget(Button(text="sync", on_press=self.sync, height=panel.height/6))
        for stud in group_client.get_all_students_by_group_name(app.selected_group_name).studs:
            sub_grid = SubGrid(usr=stud.username)
            grid.add_widget(sub_grid)
            
            
        panel.add_widget(grid)
        self.add_widget(panel)
            
            
            
# List of attached students. 

class SpecificGroupOverview(Widget):
    
    def __init__(self, **kwargs):
        super(SpecificGroupOverview, self).__init__(**kwargs)
    
    def to_attach_student_to_group(self):
        self.parent.parent.current = "add_students_to_group"
        
        
    def to_generate_check_in(self):
        self.parent.parent.current = "generate_check_in"
        
    def delete_group(self):
        app = App.get_running_app()
        msg = group_client.delete_group(app.selected_group_name)
        self.parent.parent.current = "group_overview"
        app.selected_group_name = ""
        
    def to_manage_existing_code(self):
        self.parent.parent.current = "manage_existing_code"
        
    def sync(self):
        self.banner = App.get_running_app().selected_group_name

    def back(self):
        self.parent.parent.current = "group_overview"
