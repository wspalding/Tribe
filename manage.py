import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from config import *

from tribe import create_app, db

manager = Manager(create_app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()