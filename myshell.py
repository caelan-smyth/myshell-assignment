from cmd import Cmd
import os, sys

class myPrompt(Cmd):
    prompt = "~" + os.getcwd() + "$ "
    intro = "Welcome to myshell! Type ? to list commands."

    def do_quit(self, key):
        print("Exiting...\nThank you for using myshell.")
        return True

    def do_cd(self, s=""):
        if s != "":
            try:
                os.chdir(s)
                path = os.getcwd()
                os.environ["PWD"] = os.getcwd()
                prompt.prompt = "~" + path + "$ "
            except:
                print("No such file or directory: " + s + ". 'help cd' for help.")
        else:
            print(os.getcwd())

    def do_dir(self, s=""):
        if s != "":
            print(os.listdir(s))
        else:
            print(os.listdir(os.getcwd()))

    def do_clr(self, args):
        os.system('clear')

    def do_environ(self, args):
        print(os.environ)

    def do_echo(self, s=""):
        print(' '.join(s.split()) + "\n")

    def do_pause(self, args):
        input("Press Enter to continue.")

    def do_help(self, s):            
        os.system("more README")



   

if __name__ == '__main__':
    prompt = myPrompt()
    path = os.getcwd()

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            for line in file.readlines():
                prompt.onecmd(line)

    else:
        prompt.cmdloop()