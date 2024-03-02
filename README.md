# README COMMAND-LINE TOOL

## DESCRIPTION
Currently the program creates a README with a Title, 
a Description and creates a table
with all files you want in it and a brief description of each file.
it allows you to select all files in a directory, all files with a 
specific extension or you can select files to add to the table one
at a time. 
More support and options will be added later.
Making a README can be boring and I wanted to automate some of that process. 

Created a simple terminal program to add a title of the project a description and create a file table. 

| File | Descripton |
| --------- | --------------------- |
| [create_readme.py](main.py) | Creates a README |
| [create_readme.py](global_bash_version/create_readme.py) | For using the program as a bash command 
| [create_readme.sh](global_bash_version/create_readme.sh) | For using the program as a bash command 

### USING GLOBAL BASH VERSION
you can use the .sh file to turn the program into a command
so that you can run this program from anywhere. I have it set up
so that it will automatically detetect the local directory you are in
and pass that to the .sh and .py file. using these global bash versions
allows you to treat this program as a script that enables you to run
this program from anywhere without having to copy and past the main.py
file into your directory any time you want to use it. Obviously
you can change the path in the .sh file to reflect where you are storing
the .py file.


### TO-DO
1. Add more options 
2. Error check.
3. Make more robust.


