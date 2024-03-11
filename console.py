#!/usr/bin/python3
""" import modules """
import cmd
import sys
import json
from models.base_model import BaseModel
from models import storage
from models.user  import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


newClasses = [
        "BaseModel",
        "User",
        "Place",
        "Review",
        "City",
        "State",
        "Amenity"
        ]

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
            storage.new(instance)
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
            print("** class name missing **")
        elif len(line_list) >= 1:

            if line_list[0] not in newClasses:
                print("** class doesn't exist ** ")
            else:
                objects =  storage.all()
                obj_id = line_list[0] + "." + str(line_list[1])
                
                if obj_id in objects.keys():
                    del(objects[obj_id])
                    storage.save()
                    
                else:
                    print("** instance id missing **")
                    
        else:
            print("** no instance found **")
            
    def do_all(self, line):
        """ Prints all string representation of all instances
        based or not on the class name"""
        objs_list = []
        objs = storage.all()
        line_list = line.split(" ")
        
        if len(line_list) == 1 and line_list[0] == "":
            for val in objs.values():
                objs_list.append(str(val))
            print(objs_list)
        elif line_list[0] in newClasses:
            for obj in objs.keys():
                if obj.split(".")[0] == line_list[0]:
                    objs_list.append(str(objs[obj]))
                    
        else:
            print("** class doesn't exist **")
              
    def do_update(self, line):
        """
        Updates an instance 
        based on the class name and id by adding or updating attribute
        """
        objs = storage.all()
        line_list = line.split(" ")
        if len(line_list) == 1 and  line_list[0] == "":
            print("** class name missing **")
        elif line_list[0] in newClasses:
            if len(line_list) < 2:
                print("** instane id missing **")
            elif line_list[1] in [name_id.split(".")[1] for name_id in objs.keys()]:
                name_id = line[0] + "." + line[1]
                obj = objs[name_id]
                
                if len(line_list) < 3:
                    print("** attribute name missing **")
                else:
                    if len(line_list) < 4:
                        print("** value missing **")
                    else:
                        try:
                            setattr(obj, line_list[2], eval(line_list[3].strip('"')))
                        except Exception:
                            setattr(obj, line_list[2], line_list[3].strip('"'))
                        storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")
        
        
    def default(self, line):
        """
        default methods
        Args:
            line: args passed
        """
        args = line.split(".")

        if len(args) >= 2:
            if len(args) > 1:
                className = args[0]
            if len(args) == 2:
                method = args[1]

            objects = storage.all()

            if className in newClasses:
                times = 0

                if method == "count()":
                    for key in objects.keys():
                        if className in key:
                            times += 1
                    print(times)

                elif method == "all()":
                    allList = []
                    for key in objects.keys():
                        if className in key:
                            allList.append(str(objects[key]))
                    print(allList)

                elif "show" in method:
                    show_id = method.split("(")[1].strip(")")
                    show_id = show_id.replace('"', '')
                    show_str = className + " " + show_id
                    self.do_show(show_str)

                elif "destroy" in method:
                    destroy_id = method.split("(")[1].strip(")")
                    destroy_id = destroy_id.replace('"', '')
                    destroy_str = className + " " + destroy_id
                    self.do_destroy(destroy_str)

                elif"update" in method:
                    """when dict isn't passed"""
                    if "{" not in method.split("(")[1]:
                        update_id = (
                                method.split("(")[1]
                                .split(", ")[0]
                                .strip(')"')
                                )
                        attr = method.split("(")[1].split(", ")[1].strip(')"')
                        value = method.split("(")[1].split(", ")[2].strip(')"')
                        update_str = (
                                className + " " +
                                update_id + " " +
                                attr + " " + value
                                )
                        self.do_update(update_str)
      
# if __name__ == '__main__':
#      HBNBCommand().cmdloop()   
    
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)
