from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

class AboutScreen(Screen):
    def __init__(self, **kw):
        super(AboutScreen, self).__init__(**kw)
        

class About(Widget):
    
    def __init__(self, **kwargs):
        super(About, self).__init__(**kwargs) 
    
    
    def back(self):
        self.parent.parent.current="login"


        