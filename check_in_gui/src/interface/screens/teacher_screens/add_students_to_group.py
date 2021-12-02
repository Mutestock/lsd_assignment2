from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

from logic.client import group_client
from logic.client import student_client


Builder.load_file("interface/screens/teacher_screens/add_students_to_group.kv")


class AddStudentsToGroupScreen(Screen):
    def __init__(self, **kw):
        super(AddStudentsToGroupScreen, self).__init__(**kw)


class AddStudentGrid(GridLayout):
    def __init__(self, **kwargs):
        super(AddStudentGrid, self).__init__(**kwargs)
        
    def sync(self, _):
        self.clear_widgets()
        panel = BoxLayout(orientation="vertical")
        grid = GridLayout(cols=1,row_force_default=True, row_default_height=panel.height/2)
        panel.add_widget(Button(text="sync", on_press=self.sync, height=panel.height/6))
        for stud in student_client.get_all_students().studs:
            sub_grid = GridLayout(cols=2)
            sub_grid.add_widget(Label(text=stud.username))
            sub_grid.add_widget(AddStudentButton(student_name=stud.username))
            grid.add_widget(sub_grid)
        panel.add_widget(grid)
        self.add_widget(panel)


class AddStudentButton(Button):
    student_name: str
    
    def __init__(self, student_name, **kwargs):
        super(AddStudentButton, self).__init__(**kwargs)
        self.student_name = student_name
        
    def add_student(self):
        app = App.get_running_app()
        group_client.add_student_to_group(self.student_name, app.selected_group_name)
        
class AddStudentsToGroup(Widget):
    def __init__(self, **kwargs):
        super(AddStudentsToGroup, self).__init__(**kwargs)

    def back(self):
        self.parent.parent.current = "specific_group_overview"
        
            

