#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


modelos = {'BaseModel': BaseModel,
           'User': User,
           'State': State,
           'City': City,
           'Amenity': Amenity,
           'Place': Place,
           'Review': Review}
comandos = ['quit',
            'EOF',
            'help',
            'create',
            'show',
            'destroy',
            'all',
            'update']


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Ends prompt

        Returns:
            True
        """
        return True

    def do_EOF(self, arg):
        return True

    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)

    def do_emptyline(self, arg):
        pass

    def do_create(self, arg):
        lista = arg.split()
        if len(lista) == 0:
            print('** class name missing **')
        elif lista[0] not in modelos:
            print("** class doesn't exist **")
        else:
            new = modelos[lista[0]]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        lista = arg.split()
        if len(lista) == 0:
            print('** class name missing **')
        elif lista[0] not in modelos:
            print("** class doesn't exist **")
        elif len(lista) == 1:
            print('** instance id missing **')
        else:
            idea  = str(lista[0]) + '.' + str(lista[1])
            if idea not in storage.all():
                print('** not instance found **')
            else:
                print(storage.all()[idea])

    def do_destroy(self, arg):
        lista = arg.split()
        if len(lista) == 0:
            print('** class name missing **')
        elif lista[0] not in modelos:
            print("** class doesn't exist **")
        elif len(lista) == 1:
            print('** instance id missing **')
        else:
            idea  = str(lista[0]) + '.' + str(lista[1])
            if idea not in storage.all():
                print('** not instance found **')
            else:
                tempo = storage.all()
                print(tempo[idea].id)
                del tempo[idea]
                storage.save()

    def do_all(self, arg):
        lista = arg.split()
        if len(lista) == 0:
            print('** class name missing **')
        elif lista[0] not in modelos:
            print("** class doesn't exist **")
        else:
            reto = []
            tempo = storage.all()
            for k in tempo.keys():
                clase = k.split('.')[0]
                if clase == lista[0]:
                    reto.append(str(tempo[k]))
            print(reto)


    def do_update(self, arg):
        lista0 = arg.split('"')
        lista = lista0[0].split()
        if len(lista) == 0:
            print('** class name missing **')
        elif lista[0] not in modelos:
            print("** class doesn't exist **")
        elif len(lista) == 1:
            print('** instance id missing **')
        elif len(lista) == 2:
            print('** attribute name missing **')
        elif len(lista0) == 1:
            print('** value missing **')
        else:
            idea  = str(lista[0]) + '.' + str(lista[1])
            if idea not in storage.all():
                print('** not instance found **')
            else:
                try:
                    tempo = storage.all()
                    setattr(tempo[idea], lista[2], lista0[1])
                    storage.save()
                except Exception:
                    print('** value missing **')

    def default(self, arg):
        punto = arg.split('.')
        pare = punto[1].split('(')
        if not arg:
            self.do_emptyline(self, arg)
        elif pare[0] not in comandos:
            print('** Command does not exist **')
        else:
            stringo = str(pare[0]) + ' ' + str(punto[0])
            if len(pare) == 2:
                for i in range(1, len(pare)):
                    s = pare[i]
                    if i == len(pare) - 1:
                        s = s[:-1]
                    stringo += s
            print(stringo)
            cmd.Cmd.onecmd(self, stringo)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
