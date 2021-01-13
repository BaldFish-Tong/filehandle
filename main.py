from filehandle.partname_del import partname_del
from filehandle.prompt import print_func
from filehandle.filewithkey_del import filewithkey_del


def default():
    print("Input invalid!Please input again!")


def main():
    choice = print_func()
    if choice == 1:
        partname_del()
    elif choice == 2:
        filewithkey_del()
    else:
        default()
        main()
        pass


if __name__ == "__main__":
    main()
