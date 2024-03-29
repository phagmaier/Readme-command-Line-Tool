#!/usr/bin/env python3
from pathlib import Path

def get_title():
    title = input("What is the title of your project: ")
    return title.upper()

def get_description():
    description  = input("Enter a description of your project: ")
    return description

def option_files():
    choice = input("Do you wish to include a list of files? (y/n): ").upper()
    if choice not in ['Y',"N"]:
        print("Sorry invalid input please try again")
        option_files()
    else:
        if choice == 'Y':
            return True
        return False


def get_all_files(dir, curr_dir):
    return [(str(file.name),str(file.relative_to(curr_dir))) for file in dir.iterdir() if file.is_file()]

def file_extensions(dir, curr_dir, extension):
    matching_files = dir.glob(f'*.{extension}')
    return [(str(file.name),str(file.relative_to(curr_dir))) for file in matching_files]

def a_file(dir ,base_dir):
    files = []
    paths = []
    print("When you are done selecting files in this directory type q")
    while True:
        file_name = input('please enter the file name: ')
        if file_name.lower() == 'q':
            return files,paths
        matching =  dir.glob(file_name)
        for i in matching:
            files.append(str(i.name))
            paths.append(str(i.relative_to(base_dir)))

def make_table(names, paths, description):
    table = "| File | Descripton |\n"
    table += "| --------- | --------------------- |\n"
    for name,path,dec in zip(names,paths,description):
        table += "| [" + name.replace('\n','') + "]" + "(" + path.replace('\n','') + ') | '
        table += dec.replace('\n','') + " |\n"
    return table

def get_descriptions(names):
    descriptions = []
    for i in names:
        print(f"What description of file {i} would you like to give")
        usr = input("Description:")
        descriptions.append(usr)
    return descriptions


def get_files():
    files = []
    paths = []
    og_dir = Path.cwd()
    curr_dir = Path.cwd()
    while True:
        print("You can exit at any time by typing exit") 
        print("Please enter the directory you would like to get")
        print("these files from with respect to your current path")
        dir = input("If the files are in the current dir just hit enter: ")
        if dir:
            if dir.lower() == "exit":
                return files,paths
            curr_dir = parse_dir(dir,curr_dir)
        all = input("Would you like to get all files in this directory? y/n: ").lower()
        if all == 'y':
            all = get_all_files(curr_dir,og_dir)
            for name,path in all:
                files.append(name)
                paths.append(path)
        else:
            print("Would you like to get all files ending in  certain extension?:")
            extension = input("If not type n if yes enter the extension without the .: ")
            if extension.lower() == "n":
                temp_files,temp_paths = a_file(curr_dir,og_dir)
                for i,x in zip(temp_files,temp_paths):
                    files.append(i)
                    paths.append(x)
            else:
                all = file_extensions(curr_dir, og_dir, extension)
                for name, path in all:
                    files.append(name)
                    paths.append(path)
        

        decision = input("If you want more files type something else click enter")
        if not decision:
            return files,paths

def parse_dir(newdir, curr_path):
    newdir = newdir.split('/')
    for i in newdir:
        curr_path = curr_path / i
        if not curr_path.exists():
            print('Not a valid path')
            print("All previous work lost starting over")
            get_files()
    return curr_path


    

def main():
    output = "# "
    output += get_title() + "\n"
    output += "## DESCRIPTION\n"
    output += get_description() + "\n" 
    y_or_n = option_files()
    if y_or_n:
        output += "\n"
        names, paths = get_files()
        descriptions = get_descriptions(names)
        output += make_table(names,paths,descriptions)

    with open("README.md", 'w') as file:
        file.write(output)
    



if __name__ == '__main__':
    main()
