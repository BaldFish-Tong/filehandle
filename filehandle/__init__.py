from .name_change import partname_del
from .filewithkey_del import filewithkey_del
from .filewithkey_copy import filewithkey_copy


def prompt():
    print("Please choose what you want to do:")
    print("1.Change part of files' name")
    print("2.Delete files which contains keywords")
    print("3.Copy files which contains keywords to another dir")
    print("Please input a number of the function witch you want:")
    return int(input())


def default():
    print("Input invalid!Please input again!\n")


def prog_init():
    choice = prompt()
    if choice == 1:
        partname_del()
    elif choice == 2:
        filewithkey_del()
    elif choice == 3:
        filewithkey_copy()
    else:
        default()
        prog_init()
        pass
