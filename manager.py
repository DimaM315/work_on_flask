from app import manager
from main import *

if __name__ == '__main__':
	manager.run()

#command in cmd of init manager:
#python manager.py db init

#mirgation command:
#python manager.py db migrate
#->->-> add new file in 'migration'-'versions' with function migrate data

#migration execution command:
#python manager.py db upgrade