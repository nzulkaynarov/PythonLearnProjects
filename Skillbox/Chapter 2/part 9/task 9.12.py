import os

def print_dirs(project):
    print('\nСодержимое каталога', project)
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        print('   ')

project_list = 'Skillbox'

print_dirs(project_list)