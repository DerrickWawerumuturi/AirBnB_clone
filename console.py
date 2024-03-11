#!/usr/bin/python3
"""importing relevant modules"""
import cmd
import sys
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models import storage

classesList = [
        "BaseModel",
        "User",
        "Place",
        "Review",
        "City",
        "State",
        "Amenity"
        ]

"""creating our class"""


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def emptyline(self):
        """
        wont execute if empty line + ENTER is clicked
        """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        Args:
            arg: arg passed
        """
        sys.exit(1)

    def do_EOF(self, arg):
        """Handle end of file
        """
        print("")
        return True

    def do_create(self, args):
        """
        creates a new instance of BaseModel, saves
        it (to the JSON file) and prints its id
        Args:
            args: args passed
        """
        args_list = args.split(" ")
        if len(args_list) == 1 and args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in classesList:
            print("** class doesn't exist **")
        else:
            instance = eval(args_list[0] + "()")
            storage.save()
            print(instance.id)

    def do_show(self, args):
        """prints the str representation of an instance
        based on the class name and id
        Args:
            args: arg passed
        """
        args_list = args.split(" ")
        if len(args_list) == 1 and args_list[0] == "":
            print("** class name missing **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif len(args_list) >= 1:
            if args_list[0] not in classesList:
                print("** class doesn't exist **")
            else:
                objects = storage.all()
                obj_id = args_list[0] + "." + str(args_list[1])

                if obj_id in objects:
                    obj = objects[obj_id]
                    print(obj)
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """deletes an instance based on the class name and id
        (saves the change into the Json file
        Args:
            args: arg passed
        """
        args_list = args.split(" ")

        if len(args_list) == 1 and args_list[0] == "":
            print("** class name missing **")
        elif len(args_list) >= 2:
            if args_list[0] not in classesList:
                print("** class doesn't exist **")
            else:
                objects = storage.all()
                obj_id = args_list[0] + "." + str(args_list[1])

                if obj_id in objects.keys():
                    del(objects[obj_id])
                    storage.save()
                else:
                    print("** no instance found **")

        else:
            print("** instance id missing **")

    def do_all(self, args):
        """prints a list of all str representation of all
        instances based or not on the class name
        Args:
            args: arg passed
        """
        objs_list = []
        objs = storage.all()
        args_list = args.split(" ")

        if len(args_list) == 1 and args_list[0] == "":
            for val in objs.values():
                objs_list.append(str(val))
            print(objs_list)

        elif args_list[0] in classesList:
            for obj in objs.keys():
                if obj.split(".")[0] == args_list[0]:
                    objs_list.append(str(objs[obj]))
                print(objs_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """updates an instance bsed on the class name
        and id by adding or updating attr
        Args:
            arg: args passed
        """
        objs = storage.all()
        args = arg.split(" ")
        if len(args) == 1 and args[0] == "":
            print("** class name missing **")
        elif args[0] in classesList:
            if len(args) < 2:
                print("** instane id missing **")
            elif args[1] in [name_id.split(".")[1] for name_id in objs.keys()]:
                name_id = args[0] + "." + args[1]
                obj = objs[name_id]

                if len(args) < 3:
                    print("** attribute name missing **")
                else:
                    if len(args) < 4:
                        print("** value missing **")
                    else:
                        try:
                            setattr(obj, args[2], eval(args[3].strip('"')))
                        except Exception:
                            setattr(obj, args[2], args[3].strip('"'))
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

            if className in classesList:
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()