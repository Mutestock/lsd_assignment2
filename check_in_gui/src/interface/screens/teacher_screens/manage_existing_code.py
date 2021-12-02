from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
import datetime

from logic.client import teacher_client

Builder.load_file("interface/screens/teacher_screens/manage_existing_code.kv")

class ManageExistingCodeScreen(Screen):
    def __init__(self, **kw):
        super(ManageExistingCodeScreen, self).__init__(**kw)
    
    
class ManageExistingCode(Widget):
    def __init__(self, **kwargs):
        super(ManageExistingCode, self).__init__(**kwargs)

    code_display = StringProperty()
    code_input: StringProperty()

    year_input = StringProperty()
    month_input = StringProperty()
    day_input = StringProperty()
    hour_input = StringProperty()
    minute_input = StringProperty()
    

    def date_time_values_are_legal(self, parsed_datetime) -> bool:
        return datetime.datetime.now() < parsed_datetime


    def update_countdown(self):
        parsed_datetime: datetime.DateTime
        try:
            parsed_datetime = datetime.datetime(
                int(self.year_input),
                int(self.month_input),
                int(self.day_input),
                int(self.hour_input),
                int(self.minute_input),
                0,
            )
            if self.date_time_values_are_legal(parsed_datetime):
                    msg = teacher_client.edit_countdown(self.code_input, str(parsed_datetime)).msg
                    self.code_display = f"Code changed"
            else:
                self.code_display = "Specified date was earlier than now or the values were otherwise illegal"
        except Exception as e:
            self.code_display = "Unhandled error. Please contact dev and inform him that he's stupid"
            print(e)
            
    
    def delete_code(self):
        msg = teacher_client.delete_code(self.code_input)
        
    def back(self):
        self.parent.parent.current = "specific_group_overview"
        
    def on_year_input_change(self, input):
        self.year_input = input.text
        
    def on_month_input_change(self, input):
        self.month_input = input.text
        
    def on_day_input_change(self, input):
        self.day_input = input.text
        
    def on_hour_input_change(self, input):
        self.hour_input = input.text
        
    def on_minute_input_change(self, input):
        self.minute_input = input.text
            
    def on_code_change(self, input):
        self.code_input = input.text
    
