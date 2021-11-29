from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
import datetime

from logic.client import teacher_client
from logic.ip_check import get_public_ip


Builder.load_file("interface/screens/teacher_screens/generate_check_in.kv")


class GenerateCheckInScreen(Screen):
    def __init__(self, **kw):
        super(GenerateCheckInScreen, self).__init__(**kw)


class GenerateCheckIn(Widget):
    def __init__(self, **kwargs):
        super(GenerateCheckIn, self).__init__(**kwargs)

    code_display = StringProperty()

    year_input = StringProperty()
    month_input = StringProperty()
    day_input = StringProperty()
    hour_input = StringProperty()
    minute_input = StringProperty()

    def date_time_values_are_legal(self, parsed_datetime) -> bool:
        return datetime.datetime.now() < parsed_datetime


    def code_gen(self):
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
                code = teacher_client.generate_code_and_start(get_public_ip(), str(parsed_datetime)).code
                self.code_display = f"Code: {code}\nDeadline: {str(parsed_datetime)}"
            else:
                print("Specified date was earlier than now or the values were otherwise illegal")
            
        except Exception as e:
            print(e)
        

    def to_specific_group_overview(self):
        self.parent.parent.current = "login"
        
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
