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
    def __init__(self, **kwargs):
        super(SelectGroup, self).__init__(**kwargs)

    def select_group(self):
        App.get_running_app().selected_group_name = self.text
        print(self.text)


class DeleteGroup(Button):
    def __init__(self, **kwargs):
        super(DeleteGroup, self).__init__(**kwargs)

    def delete_group(self):
        group_client.delete_group(App.get_running_app().group_name)


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
            panel.add_widget(Label(text=group_name, background_color=[0.2,0.2,0.2,0.2]))
            panel.add_widget(SelectGroup())
            panel.add_widget(DeleteGroup())
            self.add_widget(panel)
