#!/usr/bin/python3
"""
cmd console for the airbnb app
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    class for the cmd stuff
    """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF cmd to exit"""
        print()
        return True
    
    def emptyline(self):
        """empty line"""
        pass
    # help

if __name__ == "__main__":
    HBNBCommand().cmdloop()
