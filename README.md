# ls-command
Python implementation of ls command.

# Platform
The program works only on Linux. I'm planning to make it work on Windows too.

# Download
To download the project, type `git clone https://github.com/aw0s/ls-command.git` in folder which you want the program to be placed in. You can also download ZIP file and then unpack it.

# Running the program
Type `cd ls-command` and then `python ls.py`. If names of folders and files print, the program is working correctly. If something went wrong, report the bug in `Issues` on the project's Github. Make sure you've installed Python package.

# Usage
You can use the application passing a directory as an argument during executing the program. For example: `python ls.py directory`.

# Flags
So far you can run the program using 2 flags: `-a` and `-l`. `-a` shows directories and files which start with `.`. `-l` shows all parameters of the directory or file. Examples: `python ls.py -a directory`, `python ls.py -la directory`. You can use all of the flags at the same time.
