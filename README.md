# README COMMAND-LINE TOOL

## DESCRIPTION
Created a simple terminal program to add a title of the project a description and create a file table. Making a README can be boring and wanted to automate some of it and this is what I have for now it's simple and can easily be exapanded. I'm sure better ones exist but I like this as a boilerplate generator. it is also convenient for adding all files in a path to a table with relative links or adding only files  that end in a particular extension in a particular directory.

| File | Descripton |
| --------- | --------------------- |
| [main.py](main.py) | Creates a README |
| [create_readme.py](global_bash_version/create_readme.py) | Put this is path somewhere with the .sh file of same name and pass the current path to be able to run this from anywhere without this file in your directory
| [create_readme.sh](global_bash_version/create_readme.sh) | Can alias running this bash file passing it your current directory and it will automatically call the python file. convenient if you don't want to always have the file in your directory. 

### USING GLOBAL BASH VERSION

I put both files in my usr/loca/bin and then i created an
allias called create_readme that will run the .sh file. You need
to pass it your current directory in order for the python file
to know what path to use since it is in a different dir than you.
It is nice if you plan on actually using this (which I doubt anyone will besides me)
because you don't need to constantly copy the files into your current directory. 


### TO-DO
1. Add more options 
2. Error check.
3. Make more robust.


