#!/usr/bin/python3
"""command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ console class """
    prompt = '(hbnb)'

    def do_EOF(self, args):
        """ exits console """
        return True

    def do_quit(self, args):
        """ quits program """
        return True

    def emptyline(self):
        """ override cmd emptyline method """
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
