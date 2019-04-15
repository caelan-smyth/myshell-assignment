from cmd import Cmd
import os, sys

class myPrompt(Cmd):
    prompt = "~" + os.getcwd() + "$ "
    intro = "Welcome to the shell! Type ? to list commands."

    def do_quit(self, key):
        print("Exiting...\nThank you for using the shell.")
        return True

    def help_quit(self):
        print("Exits the shell.")

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

    def help_cd(self):
        print("Changes the current working directory.\nUsage: cd <directory>\nIf no <directory> argument is passed, reports the current directory.")

    def do_dir(self, s=""):
        if s != "":
            print(os.listdir(s))
        else:
            print(os.listdir(os.getcwd()))

    def help_dir(self):
        print("Lists the contents of <directory>.\nUsage: dir <directory>\nIf no <directory> argument is passed, lists the contents of the current directory.")

    def do_clr(self, args):
        os.system('clear')

    def help_clr(self):
        print("Clears the terminal.\nTakes no arguments.")

    def do_environ(self):
        print(os.environ)

    def help_environ(self):
        print("Prints the environment strings.\nTakes no arguments.")

    def do_echo(self, s=""):
        print(' '.join(s.split()) + "\n")

    def help_echo(self):
        print("Prints a comment in the terminal, followed by a new line.\nUsage: echo <comment>")

    def do_pause(self, args):
        input("Press Enter to continue.")

    def help_pause(self):
        print("Pauses shell operation until the enter key is pressed.")

    def do_help(self, s):            
        os.system("more README")

    def help_help(self):
        print("Displays the user manual.\nhelp <command> displays help for the specified command.")


   

if __name__ == '__main__':
    prompt = myPrompt()
    path = os.getcwd()

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            for line in file.readlines():
                prompt.onecmd(line)

    else:
        prompt.cmdloop()