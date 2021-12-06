 
## Large System Development - Assignment 2

This project is created with Python and Kivy:

https://kivy.org/#home

And a Rust backend written with the GRPC framework Tonic:

https://github.com/hyperium/tonic

The backend is currently hosted here:

167.99.91.81:30303

You can run the backend locally with Rust:

> cargo r

The GUI specifically requires Python 3.9. There's a requirement.txt file for you, which you'll have to use. 

Alternatively use poetry:

https://python-poetry.org/

> cd check_in_gui

> poetry shell

> python src/main.py

If you host the backend locally, you should instead use:

> python src/cli.py devmode

The database runs with postgreSQL, so if you want to use it locally you'll need to run:

> docker-compose up

Screenshots of project inside resources folder.