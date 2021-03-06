# ls-command
Python implementation of Linux ls command.

## Platform
The app currently works only on Linux.

## Download
To download the project files, type `git clone https://github.com/aw0s/ls-command.git` in folder which you want the program to be placed in. You can also download ZIP file and then unpack it.

## Running the program
Type `cd ls-command` and then `python ls.py`. If names of folders and files have been printed, the app works correctly. If something went wrong, report the bug in `Issues` on the project's Github. Make sure you've installed Python package.  
If You want to use ls app instead of original ls, type `alias ls='python path/to/ls/ls.py'`. To remove alias, type `unalias ls`.

## Usage
You can use the application by passing directory as an argument during executing the program. For example: `python ls.py directory`.

## Flags
So far you can run the program using 6 flags: `-a`, `-A`, `-l`, `-n`, `-o` and `-t`:  
`-a (--all)` shows all the directories and files, also which start with `.` and `..`.  
`-A (--almost_all)` works the same as `-a`, but doesn't display `.` and `..` directories.  
`-l` shows all parameters of the directory or file.  
`-n` works the same as `-l`, but instead of user and group names displays user and group IDs.  
`-o` works the same as `-l`, but doesn't display infomation about group.  
`-t` sorts all files or directories by time in descending order.  
Examples: `python ls.py -a path`, `python ls.py -ltA path`, `python ls.py`. You can use all of the flags at the same time.

## Additional knowledge about ls flags
You can read more about flags and generally about `ls` by typing `man ls` in Linux terminal.
