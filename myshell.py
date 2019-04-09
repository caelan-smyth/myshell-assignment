from cmd import Cmd
import os, sys

class myshell(Cmd):
    def cd(s):
        try:
            if s:
                os.chdir(s)
            else:
                os.getcwd()
        except:
            print(s + ": No such file or directory")

    def dir(s):
        os.listdir(s)

    def clr():
        os.system('clear')

    def environ():
        os.environ()

    def echo(s):
        print(' '.join(s.split()) + "\n")

    def pause():
        os.system('pause')

def main():
    

if __name__ == '__main__':
    main()