from cmd import Cmd
import os, sys, subprocess

class myPrompt(Cmd):
    prompt = "~" + os.getcwd() + "$ "
    intro = "Welcome to the shell! Type ? to list commands."

    def do_quit(self, key):
        "Exis the shell."
        print("Exiting...")
        return True

    def do_cd(self, s=""):
        "Changes the current working directory.\nUsage: cd <directory>"
        if s:
            try:
                os.chdir(s)
                path = os.getcwd()
                os.environ["PWD"] = os.getcwd()
                prompt.prompt = "~" + path + "$ "
            except:
                print("No such file or directory: " + s + ". 'help cd' for help.")
        else:
            os.getcwd()

    def do_dir(self, s):
        "Lists the contents of the directory.\nUsage: dir <directory>"
        try:
            os.listdir(s)
        except:
            print("No such file or directory: " + s)

    def do_clr(self):
        "Clears the screen."
        os.system('clear')

    def do_environ(self):
        "Prints the environment strings."
        os.environ()

    def do_echo(self, s):
        "Prints a comment on the screen with excess whitespace removed."
        print(' '.join(s.split()) + "\n")

    def do_pause(self):
        "Pauses shell operation until the Enter key is pressed."
        input("Press Enter to continue.")

   

if __name__ == '__main__':
    prompt = myPrompt()
    path = os.getcwd()

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            for line in file.readlines():
                prompt.onecmd(line)

    else:
        prompt.cmdloop()