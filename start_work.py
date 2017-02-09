import sys
import subprocess

empty_project_name_error = 'Please, fill in project name'
invalid_env_error = 'Invalid enviroment'

try:
    project_name = sys.argv[1]
except:
    print empty_project_name_error

try:
    subprocess.Popen('workon %s' % project_name, shell=True)
except:
    print invalid_env_error