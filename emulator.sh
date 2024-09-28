#!/usr/bin/python3
from zipfile import ZipFile
import sys

user_name = sys.argv[1]
path_to_arxiv = sys.argv[2]
path_to_script = sys.argv[3]

pwd='/'
pre_pwd='/'

with ZipFile(path_to_arxiv,"a") as zip:
    while True:
        list_of_elements = zip.namelist()
        command = input(user_name + '$ ')
        if command != '':
            if command == 'exit':
                break
                zip.close()
            elif command == 'uname':
                print(user_name)
            elif command.split()[0] == 'mkdir':
                commands = command.split()
                if(len(commands) == 2):
                    if(pwd =='/'):
                        new_folder_name = command.split()[1]+ '/'
                    else:
                        new_folder_name = pwd[1:-1] + '/' + commands[1] + '/'
                    zip.writestr(new_folder_name, '')
            elif command == 'ls' :
                for element in list_of_elements:
                    if(pwd in '/' + element and pwd.count('/') == element.count('/')):
                        if(element.endswith('/')):
                            print('dir: ' + element[len(pwd) - 1: element.rfind('/')])
                        else:
                            print('file: ' + element[len(pwd) - 1:element.rfind('/')])
            elif command.split()[0] == 'cd':
                commands = command.split()
                if(len(commands) == 2):
                    if(commands[1] == '..' and pwd != '/'):
                        pwd = pre_pwd
                        pre_pwd = '/'.join(pwd.split('/')[0:-2]) + '/'
                    elif(commands[1]+'/' in list_of_elements or (len(pwd) > 1 and pwd[1:] + commands[1] + '/' in list_of_elements)):
                        pre_pwd = pwd
                        pwd = pwd + commands[1] +'/'
                    else: 
                        print('error: no such directory')
            elif command == 'pwd':
              if pwd != '/':
                print(pwd[:-1])
              else:
                print('/')
            else: 
                print('error: unknown command')