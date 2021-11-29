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


class StudentPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(StudentPanel, self).__init__(**kwargs)


class AddStudentButton(Button):
    student_name: str
    
    def __init__(self, student_name, **kwargs):
        super(AddStudentButton, self).__init__(**kwargs)
        self.student_name = student_name
        
        
        
    def add_student(self):
        app = App.get_running_app()
        msg = group_client.add_student_to_group(self.student_name, app.selected_group_name).msg
        print(msg)
        
class AddStudentsToGroup(Widget):
    def __init__(self, **kwargs):
        super(AddStudentsToGroup, self).__init__(**kwargs)

    def back(self):
        self.parent.parent.current = "specific_group_overview"
        
    def sync(self):
        for stud in student_client.get_all_students().studs:
            print(stud.username)
            panel = StudentPanel()
            panel.add_widget(Label(text=stud.username))
            panel.add_widget(AddStudentButton(student_name=stud.username))
            self.add_widget(panel)
            

