import click
import os


@click.group()
def manager():
    pass

@manager.command()
def devmode():
    os.environ["CHECK_IN_GUI_DEV_MODE"]="True"
    from interface.check_in_main import CheckInApp
    CheckInApp().run()

manager()