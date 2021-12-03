from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.properties import StringProperty

from logic.client import student_client
from logic.charts import generate_pie_check_in_percentage
from logic.client import student_client
from utils.config import IMAGES_PATH

Builder.load_file("interface/screens/teacher_screens/teacher_stats.kv")


class TeacherStatsScreen(Screen):
    pass


class TeacherStats(Widget):
    def __init__(self, **kwargs):
        super(TeacherStats, self).__init__(**kwargs)

    def to_dashboard(self):
        self.parent.parent.current = "teacher_dashboard"



class PieButton(Button):
    usr = StringProperty("")
    
    def __init__(self, usr, **kwargs):
        super(PieButton, self).__init__(**kwargs)
        self.usr = usr
        
    def bake_pie(self):
        all_stats = student_client.get_stats(self.usr).all_stats
        if len(all_stats)>0:
            generate_pie_check_in_percentage(all_stats)
            box = BoxLayout()
            box.add_widget(Image(source=IMAGES_PATH+"/pie.png"))
            self.parent.parent.parent.parent.parent.parent.parent.add_widget(box)



class StudentGridTeacherStats(GridLayout):
    def __init__(self, **kwargs):
        super(StudentGridTeacherStats, self).__init__(**kwargs)
        
    def sync(self, _):
        self.clear_widgets()
        t_stat_box = BoxLayout(orientation="vertical")
        t_grid = GridLayout(cols=1,row_force_default=True, row_default_height=t_stat_box.height/2)
        t_stat_box.add_widget(Button(text="sync", on_press=self.sync, height=t_stat_box.height/6))
        for stud in student_client.get_all_students().studs:
            print(stud)
            s_grid = GridLayout(cols=1, rows=3)
            s_grid.add_widget(Label(text=stud.username))
            s_grid.add_widget(PieButton(usr=stud.username))
            t_grid.add_widget(s_grid)
            
        t_stat_box.add_widget(t_grid)
        self.add_widget(t_stat_box)
        
        
        
