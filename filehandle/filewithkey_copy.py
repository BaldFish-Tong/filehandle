import os
from shutil import copy
from random import randint

prompt1 = 'Please input the path you want to handle:\n'
prompt2 = 'Please input the keyword:\n'
prompt3 = "Please input the full target path:\n"
prompt_error = 'Path Error! Please import it again!\n'


def handle_dir(dir_path, key, path_tar):
    dir_files = os.listdir(dir_path)
    for i_file in dir_files:
        f_path_full = dir_path + '\\' + i_file
        if os.path.isdir(f_path_full):
            handle_dir(f_path_full, key, path_tar)
        else:
            if i_file.find(key) != -1:
                f_path_tar = path_tar + '\\' + i_file
                if not os.path.isfile(f_path_tar):
                    copy(f_path_full, f_path_tar)
                else:
                    f_path_tar = path_tar + '\\' + str(randint(1, 1000)) + i_file
                    copy(f_path_full, f_path_tar)


def filewithkey_copy():
    dir_path = input(prompt1)
    while not os.path.isdir(dir_path):
        dir_path = input(prompt_error)
    key = input(prompt2)
    path_tar = input(prompt3)
    if not os.path.exists(path_tar):
        os.mkdir(path_tar)
    handle_dir(dir_path, key, path_tar)

