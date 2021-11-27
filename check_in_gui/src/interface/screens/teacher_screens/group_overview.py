from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.app import App

from logic.client import group_client


Builder.load_file("interface/screens/teacher_screens/group_overview.kv")


class GroupOverviewScreen(Screen):
    def __init__(self, **kw):
        super(GroupOverviewScreen, self).__init__(**kw)


class GroupPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(GroupPanel, self).__init__(**kwargs)


class SelectGroup(Button):
    group_name: str
    
    def __init__(self, group_name,**kwargs):
        super(SelectGroup, self).__init__(**kwargs)
        self.group_name = group_name

    def select_group(self):
        app = App.get_running_app()
        app.selected_group_name = self.group_name
        self.parent.parent.parent.parent.current = "login"
        


class DeleteGroup(Button):
    group_name: str
    
    def __init__(self, group_name, **kwargs):
        super(DeleteGroup, self).__init__(**kwargs)
        self.group_name = group_name

    def delete_group(self):
        group_client.delete_group(self.group_name)


class GroupOverview(Widget):
    def __init__(self, **kwargs):
        super(GroupOverview, self).__init__(**kwargs)

    def to_dashboard(self):
        self.parent.parent.current = "teacher_dashboard"

    def to_create_group(self):
        self.parent.parent.current = "create_group"

    def sync(self):
        app = App.get_running_app()
        app.attached_groups = group_client.get_all_groups_by_username(
            app.username
        ).group_names
        for group_name in app.attached_groups:
            print(group_name)
            panel = GroupPanel()
            panel.add_widget(Label(text=group_name))
            panel.add_widget(SelectGroup(group_name=group_name))
            panel.add_widget(DeleteGroup(group_name=group_name))
            self.add_widget(panel)
