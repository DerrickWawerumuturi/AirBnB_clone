""" import modules """
import cmd
import sys
import json
from models.base_model import BaseModel
from models import storage
newClasses = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter: """

    prompt = '(hbnb) '
    def emptyline(self):
        """
        wont execute if empty line + ENTER is clicked
        """
        pass
    def do_EOF(self, line):
        """ end of file function"""
        return True
    def do_quit(self, args):
        """ quit command"""
        sys.exit(1)

    def do_help(self, arg: str):
        return super().do_help(arg)
    
    def do_create(self, line):
        """ Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id
        Args:
            args: argument passed
        """
        line_list = line.split(" ")
        if len(line_list) ==  1 and line_list[0] == "":
            print("** class name missing **")
        elif line_list[0] not in newClasses:
            print("** class doesn't exist **")
        else:
            instance = eval(line_list[0] + "()")
            storage.save()
            print(instance.id)

    def do_show(self, line):
        """prints the str representation of an instance
        based on the class name and id
        Args:
            args: arg passed
        """
        line_list = line.split(" ")
        if len(line_list) == 1 and line_list[0] == "":
            print("** class name missing **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        elif len(line_list) >= 1:
            if line_list[0] not in newClasses:
                print("** class doesn't exist **")
            else:
                objects = storage.all()
                obj_id = line_list[0] + "." + str(line_list[1])

                if obj_id in objects:
                    obj = objects[obj_id]
                    print(obj)
                else:
                    print("** no instance found **")
    def do_destroy(self, line):
        """deletes an instance based on the class name and id
        saves the change into the Json file
        Args:
            args: arg passed
        """
        line_list = line.split(" ")
        if len(line_list) ==  1 and line_list[0] == "":
            print()
        
            
        

if __name__ == '__main__':
     HBNBCommand().cmdloop()   
    
