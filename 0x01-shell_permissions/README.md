this file will describe what each script does

0-iam_betty it changes the user id to betty
1-who_am_i prints user id
2-groups prints all the groups the current user is part of 
3-new_owner  changes the owner of the file hello to betty
4-empty creates an empty file called hello
5-execute adds execute permission to the owner of the file hello
6-multiple_permissions adds execute permission to the owner and the group owner, and read permission to other users, to the file hello
7-everybody adds execution permission to the owner, the group owner and the other users, to the file hello
8-James_Bond sets the permission to the file hello as follows: Owner: no permission at all, Group: no permission at all, Other users: all the permission
9-John_Doe sets the mode of the file hello to this: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
10-mirror_permissions sets the mode of the file hello the same as ollehs mode
11-directories_permissions adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. 
12-directory_permissions creates a directory called dir_holberton with permissions 751 in the working directory
13-change_group changes the group owner to holberton for the file hello
14-change_owner_and_group changes the owner to betty and the group owner to holberton for all the files and directories in the working directory
15-symbolic_link_permissions changes the owner and the group owner of the file _hello to betty and holberton respectively
16-if_only changes the owner of the file hello to betty only if it is owned by the user guillaume

