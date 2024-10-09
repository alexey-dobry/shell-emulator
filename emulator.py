import sys
from zipfile import ZipFile
import argparse
class ShellEmulator:
    def __init__(self,user_name ="default",path_to_arxiv="./file_system.zip",path_to_script = ""):
        self.user_name = user_name
        self.path_to_arxiv = path_to_arxiv
        self.path_to_script = path_to_script
        self.virtual_sys_folder = ZipFile(path_to_arxiv, 'a')
        self.cwd = '/'
    def run_script(self,script_path):
        with open(script_path,'r') as script:
            for line in script:
                self.execute_command(line)
    def execute_command(self,command):
        if not command:
            return
        
        commands = command.split()
        cmd = commands[0]
        args = commands[1:]

        if cmd == 'cd':
            self.cd(args)
        elif cmd == 'ls':
            self.ls(args)
        elif cmd == 'exit':
            self.exit()
        elif cmd == 'uname':
            self.uname(args)
        elif cmd == 'mkdir':
            self.mkdir(args)
        elif cmd == 'pwd':
            self.pwd()
        else:
            print(f"{cmd}: unknowd command")
    
    def cd(self,args):
        if not args:
            return
        target = args[0]
        list_of_paths = self.virtual_sys_folder.namelist()
        if target == '/':
            self.cwd = '/'
        elif target == '..':
            if self.cwd == '/':
                return
            else:
                self.cwd = '/'.join(self.cwd.split('/')[:-2]) +'/'
        elif target == '.':
            return
        elif self.cwd[1:] + target + '/' in list_of_paths: #Обработка случая абсолютного пути
            self.cwd += target + '/'
        elif target[1:] + '/' in list_of_paths: #Обработка случая относительного пути
            self.cwd = target + '/'
        else:
            print(f"No such file or directory")
            return

    def ls(self,args):
        list_of_paths = self.virtual_sys_folder.namelist()
        for path in list_of_paths:
            if( self.cwd == '/' + path[0:len(self.cwd) - 1] and self.cwd.count('/') == path.count('/')):
                print(path[len(self.cwd) - 1: path.rfind('/')])
    def exit(self):
        print("Bye!")
        self.virtual_sys_folder.close()
        exit(0)
    def uname(self,args):
        if not args:
            print("Linux")
        elif args[0] == "-a":
            print(f"Linux {self.user_name} 5.15.0-1-generic x86_64 GNU/Linux")
        else:
            print("No such flag")

    def mkdir(self,args):
        folder_name = args[0]
        if(folder_name.count('/') == 0):
            if self.cwd == '/':
                path = folder_name + '/'
            else:
                path = self.cwd[1:] + folder_name + '/'
            self.virtual_sys_folder.writestr(path, '')
        else: 
            print("Name is not allowed")
    def pwd(self):
        print(self.cwd)
    def run(self):
        if(self.path_to_script != None and self.path_to_script[0:2] == "./"):
            self.run_script(self.path_to_script)
        try:
            while True:
                command = input(f"{self.user_name}@{self.cwd}> ")
                self.execute_command(command)
        except KeyboardInterrupt:
            self.exit()

def args_parser():
    parser = argparse.ArgumentParser(description="Эмулятор Shell")
    parser.add_argument("user_name",nargs="?",help="Имя пользователя",default="username")
    parser.add_argument("path_to_arxiv",nargs="?",help="Путь до виртуальной файлово системы",default="./file_system.zip")
    parser.add_argument("path_to_script",nargs="?",default=None)
    return parser.parse_args()

if __name__ == '__main__':
    args=args_parser()
    emulator = ShellEmulator(args.user_name,args.path_to_arxiv,args.path_to_script)
    emulator.run()
