from cmd import Cmd
import os, sys

class myshell(Cmd):
    prompt = "~" + os.getcwd() + ":" + "~" + "$ "
    starter = "Welcome to the shell! Type ? to list commands."

    def do_quit(self, key):
        print("Exiting...")
        return True

    def help_quit(self):
        print("Exits the shell.")

    def do_cd(s):
        if s:
            try:
                os.chdir(s)
                path = os.getcwd()
                os.environ["PWD"] = os.getcwd()
                shell.prompt = "~" + path + ":" + "~" + "$ "
            except:
                print(s + ": No such file or directory. Do 'help cd' for help.")
        else:
            os.getcwd()

    def help_cd():
        print("Changes the current working directory.\nUsage: cd <directory>")

    def do_dir(s):
        os.listdir(s)

    def help_dir():
        print("Lists the contents of the directory.\nUsage: dir <directory>")

    def do_clr():
        os.system('clear')

    def help_clr():
        print("Clears the screen.")

    def do_environ():
        os.environ()

    def help_environ():
        print("Prints the environment strings.")

    def do_echo(s):
        print(' '.join(s.split()) + "\n")

    def help_echo():
        print("Prints a comment on the screen with excess whitespace stripped and a newline at the end.\nUsage: echo <comment>")

    def do_pause():
        input("Press Enter to continue.")

    def help_pause():
        print("Pauses shell operation until the Enter key is pressed.")

    def do_help():
    

if __name__ == '__main__':
    shell = myShell()
    path = os.getcwd()
    print(sys.argv)

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            for line in file.readlines():
                shell.onecmd(line)

    else:
        shell.cmdloop()