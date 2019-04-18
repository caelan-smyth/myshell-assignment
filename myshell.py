from cmd import Cmd
import os, sys, subprocess, threading #modules used to implement the shell

helpfile = os.path.abspath("README") #the help command previously didn't work if the current working directory was changed within the shell, however this will sidestep this problem by reading the file from its absolute path.

class myShell(Cmd):
    prompt = "~" + os.getcwd() + "$ " #this is the prompt for the shell with the current directory included in the prompt.
    intro = "Welcome to myshell! Type ? to list commands." #a simple intro message that informs the user of how to get commands.
    global helpfile

    def default(self, args): #the CMD default function, if overridden, allows for commands not defined by the shell to still be executed by the shell.
        try: #see if the command exists
            subprocess.run(args) #run the command if it exists.
        except: #return an error message if the command does not exist.
            print("Command not found: " + args[0])

    def shell_out(self, args): #a function for IO redirection in the shell's execution
        if ">" in args: #for writing output to a file
            contents = mainCommands(args[:-2])
            print(contents, file = open(args[-1], "w"))
        elif ">>" in args: #for appending output to a file
            contents = mainCommands(args[:-2])
            print(contents, file = open(args[-1], "a"))
        else: #print the file
            contents = mainCommands(args)
            if contents:
                print(contents)

    def do_quit(self, key): #a function for exiting the shell
        print("Exiting...\nThank you for using myshell.")
        return True #the cmd.cmdloop() function continues to loop until a function returns the boolean True. Therefore, this function will exit the shell when it returns True.

    def do_cd(self, s=""): #a function for changing the current working directory
        if s != "": #if there is a directory passed to the command
            try: #see if the directory exists
                os.chdir(s) #change to that directory
                path = os.getcwd() #edit the prompt to contain the path to the new directory
                os.environ["PWD"] = os.getcwd()
                shell.prompt = "~" + path + "$ "
            except: #if the directory doesn't exist, return an error message
                print("No such file or directory: " + s + ". 'help cd' for help.")
        else:
            print(os.getcwd()) #if no directory argument is passed, report the current working directory

    def do_dir(self, s=""): #a function for listing the contents of a directory
        if s != "": #if there is a directory specified,
            print(os.listdir(s)) #calls the os module function to list the contents of the given directory
        else: #otherwise
            print(os.listdir(os.getcwd())) #calls the os module function to list the contents of the current directory

    def do_clr(self, args): #a function for clearing the terminal
        os.system('clear') #calls the os module function to clear the terminal

    def do_environ(self, args): #a function for printing the environment strings
        print(os.environ) #calls the os module function to produce the environment strings

    def do_echo(self, s=""): #a function for echoing a comment onto the terminal
        print(' '.join(s.split()) + "\n") #outputs a comment on the terminal, followed by a new line.

    def do_pause(self, args): #pauses shell input until the enter key is pressed.
        input("Press Enter to continue.")#although the shell will allow you to type other inputs, it will not continue until you press the enter key.

    def do_help(self, s): #opens the manual with the more filter
        os.system("more " + helpfile) #reads from the README manual 25 lines at a time, press the spacebar to read more lines.

if __name__ == '__main__':
    shell = myShell() #commences execution of the shell
    path = os.getcwd() #for displaying the path of the current working directory in the prompt

    if len(sys.argv) > 1: #for input of commands from a batch file.
        with open(sys.argv[1]) as file: #opens the batch file
            for line in file.readlines(): #reads input from the batch file
                shell.onecmd(line) #executes the batch file line by line

    else: #if no input file is provided, starts shell execution as normal
        shell.cmdloop() #loops command input until the shell is passed the quit command.
        shell_in = input().split()
        if shell_in[-1] == "&": #for background processing
            backexec = threading.Thread(target=shell_out, args=[shell_in[:-1]])
            backexec.start()