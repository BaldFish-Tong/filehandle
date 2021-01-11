import os

prompt1 = 'Please import the path you want to handle:\n'
prompt2 = 'Please import the string you want replace:\n'
prompt3 = 'Please import the string you want replace to:\n'
prompt_error = 'Path Error! Please import it again!'


def handle_dir(dir_path, tar, res):
    dir_files = os.listdir(dir_path)
    for i_file in dir_files:
        f_path = dir_path + '\\' + i_file
        f_path_n = f_path.replace(tar, res)
        if os.path.isdir(f_path_n):
            handle_dir(f_path_n, tar, res)
        else:
            os.rename(f_path, f_path_n)


def main():
    dir_path = input(prompt1)
    while not os.path.isdir(dir_path):
        dir_path = input(prompt_error)
    tar = input(prompt2)
    res = input(prompt3)
    handle_dir(dir_path, tar, res)


if __name__ == "__main__":
    main()
