import os
import toml

_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
_ROOT_DIR = os.path.dirname(_ROOT_DIR)

ROOT_DIR = os.path.dirname(_ROOT_DIR)
CONFIG_FILE_PATH = ROOT_DIR + "/config.toml"
RESOURCES_PATH = ROOT_DIR + "/resources"
IMAGES_PATH = RESOURCES_PATH + "/images"
CONFIG = {}

if not os.path.isdir(RESOURCES_PATH):
    os.mkdir(f"{RESOURCES_PATH}/images")

if not os.path.isdir(IMAGES_PATH):
    os.mkdir(IMAGES_PATH)

_content: str = ""

with open(CONFIG_FILE_PATH) as f:
    _content = f.read()

if os.getenv('CHECK_IN_GUI_DEV_MODE'):
    print("********************************")
    print("********************************")
    print("CHECK IN GUI RUNNING IN DEV MODE")
    print("********************************")
    print("********************************")
    CONFIG = toml.loads(_content)["dev"]
else:
    CONFIG = toml.loads(_content)["prod"]
    