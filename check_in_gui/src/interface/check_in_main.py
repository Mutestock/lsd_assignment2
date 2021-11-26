from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, ListProperty

Builder.load_file("interface/check_in.kv")

# https://stackoverflow.com/questions/47963198/screen-manager-in-kivy-with-kv-file


class CheckIn(Widget):
    pass


class CheckInApp(App):
    username = StringProperty()
    is_teacher = BooleanProperty()
    attached_groups = ListProperty()
    selected_group_name = StringProperty()

    def build(self):
        return CheckIn()
