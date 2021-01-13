import os

prompt1 = 'Please import the path you want to handle:\n'
prompt2 = 'Please import the keyword:\n'
prompt_error = 'Path Error! Please import it again!'


def handle_dir(dir_path, key):
    dir_files = os.listdir(dir_path)
    for i_file in dir_files:
        f_path_full = dir_path + '\\' + i_file
        if os.path.isdir(f_path_full):
            handle_dir(f_path_full, key)
        else:
            if i_file.find(key) != -1:
                os.remove(f_path_full)


def filewithkey_del():
    dir_path = input(prompt1)
    while not os.path.isdir(dir_path):
        dir_path = input(prompt_error)
    key = input(prompt2)
    handle_dir(dir_path,key)