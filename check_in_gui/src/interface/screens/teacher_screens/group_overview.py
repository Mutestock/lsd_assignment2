from kivy.uix.gridlayout import GridLayout
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


class GroupPanel(GridLayout):
    def __init__(self, **kwargs):
        super(GroupPanel, self).__init__(**kwargs)

    def sync(self, _):
        app = App.get_running_app()
        app.attached_groups = group_client.get_all_groups_by_username(
            app.username
        ).group_names
        self.clear_widgets()
        panel = BoxLayout(orientation="vertical")
        panel.add_widget(Button(text="sync", on_press=self.sync, size_hint_y=None, height=self.height/2))
        grid = GridLayout(cols=1,row_force_default=True, row_default_height=panel.height/2)
        for group_name in app.attached_groups:
            sub_grid = GridLayout(cols=3)
            sub_grid.add_widget(Label(text=group_name))
            sub_grid.add_widget(SelectGroup(group_name=group_name))
            sub_grid.add_widget(DeleteGroup(group_name=group_name))
            grid.add_widget(sub_grid)
        panel.add_widget(grid)
        self.add_widget(panel)
        



class SelectGroup(Button):
    group_name: str
    
    def __init__(self, group_name,**kwargs):
        super(SelectGroup, self).__init__(**kwargs)
        self.group_name = group_name

    def select_group(self):
        app = App.get_running_app()
        app.selected_group_name = self.group_name
        self.parent.parent.parent.parent.parent.parent.parent.parent.current = "specific_group_overview"



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