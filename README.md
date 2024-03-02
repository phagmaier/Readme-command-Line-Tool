# README COMMAND-LINE TOOL

## DESCRIPTION
Created a simple terminal program to add a title of the project a description and create a file table. Making a README can be boring and wanted to automate some of it and this is what I have for now it's simple and can easily be exapanded. I'm sure better ones exist but I like this as a boilerplate generator. it is also convenient for adding all files in a path to a table with relative links or adding only files  that end in a particular extension in a particular directory.

| File | Descripton |
| --------- | --------------------- |
| [main.py](main.py) | Creates a README |
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


