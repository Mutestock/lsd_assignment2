from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from logic.charts import generate_pie_check_in_percentage
from logic.client import student_client
from utils.config import IMAGES_PATH

Builder.load_file("interface/screens/student_screens/student_stats.kv")

class StudentStatsScreen(Screen):
    pass


class StudentStatsBox(BoxLayout):
    def __init__(self, **kwargs):
        super(StudentStatsBox, self).__init__(**kwargs)
    
    def get_check_in_pie(self, _):
        app = App.get_running_app()
        all_stats = student_client.get_stats(app.username).all_stats
        if len(all_stats)>0:
            generate_pie_check_in_percentage(all_stats)
            self.clear_widgets()
            self.add_widget(Button(text="Check-in Pie", on_press=self.get_check_in_pie))
            box = BoxLayout()
            box.add_widget(Image(source=IMAGES_PATH+"/pie.png"))
            self.add_widget(box)
        
    

class StudentStats(Widget):
    
    def __init__(self, **kwargs):
        super(StudentStats, self).__init__(**kwargs)
        
    def to_dashboard(self):
        self.parent.parent.current = "student_dashboard"
        
        
            
            

