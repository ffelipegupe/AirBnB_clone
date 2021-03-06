#!/usr/bin/python3
""" Console module """
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """ Command Line Interpreter module """
    prompt = "(hbnb) "
    __names = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, arg):
        pars = list(map(str, arg.split(".")))
        a = pars[1].split("(")
        if pars[1] == "all()":
            self.do_all(pars[0])
        elif a[0] == "show":
            b = (a[1].split(")"))
            n_id = pars[0]
            n_li = n_id + " " + b[0]
            self.do_show(n_li)
        elif a[0] == "destroy":
            b = (a[1].split(")"))
            n_id = pars[0]
            n_li = n_id + " " + b[0]
            self.do_destroy(n_li)
        elif a[0] == "update":
            b = (a[1].split(")"))
            c = b[0].split(", ")
            n_id = pars[0]
            n_li = n_id + " " + c[0] + " " + c[1] + " " + c[2]
            self.do_update(n_li)
        elif a[0] == "count":
            obj_c = 0
            for obj in storage.all().values():
                if pars[0] == obj.__class__.__name__:
                    obj_c += 1
            print(obj_c)

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Empty line does not execute anything
        """
        pass

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_create(self, arg):
        """Usage: create <class>.
        Creates a new instance of BaseModel and prints the id
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__names:
            print("** class doesn't exist **")
        elif len(args) > 1:
            pass
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <instance id>.
        Prints the string representation of an instance
        """
        args = parse(arg)
        sea = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in sea:
            print("** no instance found **")
        else:
            for object_id in sea.keys():
                a = 0
                if object_id == "{}.{}".format(args[0], args[1]):
                    a = 1
            if a == 1:
                print(sea[object_id])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id>.
        Deletes an instance based on the class name and id
        """
        args = parse(arg)
        sea = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in sea:
            print("** no instance found **")
        else:
            del sea["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all / all <class>.
        Prints all string representation of all instances
        """
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__names:
            print("** class doesn't exist **")
        else:
            nls = []
            sea = storage.all().values()
            for find in sea:
                    if len(args) > 0 and args[0] == find.__class__.__name__:
                        nls.append(find.__str__())
                    elif len(args) == 0:
                        nls.append(find.__str__())
            print(nls)

    def do_update(self, arg):
        """Usage: update <class name> <id> <attribute name>"<attribute value>"
        Updates an instance based on the class name and id
        """
        args = parse(arg)
        sea = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in sea:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            for object_id in sea.keys():
                if object_id == "{}.{}".format(args[0], args[1]):
                    setattr(sea[object_id], args[2], args[3].strip('"'))
        storage.save()


def parse(arg):
    """Function that parse arguments
    """
    return tuple(map(str, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
