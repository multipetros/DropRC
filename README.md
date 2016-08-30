# DropRC
Copyright (C) 2013-2016, Petros Kyladitis

## Description
A server-client solution, to __Remote Control a PC via on-line storage sync services.__ 
  

  
For updates and more info see at <http://multipetros.gr/>

## Requirements
This program is developed with Python, so it can be run, under every system which support Python 2.x with the libraries _time, os, re, datetime, ConfigParser_ for both Server-Client, and furthermore _shutil, urllib, Image, ImageGrab_ for the Client.
  
Especially for MS Windows, Server and Client programs are distributed as precompiled standalone executables, which can run, out of the box, without any dependencies.

## Usage
#### Server
- Each time you run the DropRC server, you can specify the time interval between command's list update and the path to your sync folder.
- Of course, you can bypass the setting, and use the last saved options, by pressing 'y' at the initial question.
- After that server is running and waiting for new commands from the client.
#### Client
- Each time you run the DropRC client, you can specify the time interval between command's list update and the path to your sync folder.
- And in this case, you can bypass the setting, and use the last saved options, by pressing 'y' at the initial question.
- After that client is running and listening your commands. At new line, enter '.' to end the input (send commands to server), '?' to see acceptable commands, or 'q' to quit.
- Acceptable commands:
  - `screenshot` 'filename'
  - `download` 'url_to_download' 'path_to_remote_machine'
  - `rm` 'file_to_delete'
  - `rmdir` 'folder_to_delete'
  - `rename` 'file_to_rename' 'new_name'
  - `mkdir` 'folder_to_create'
  - `ls` 'path_to_list'
  - `copy` 'file_to_copy' 'copy_destination'
  
## Change log
#### v1.0
- Initial version
- Supported commands: "screenshot", "download", "rm", "rmdir", "rename", "mkdir", "ls" & "copy"

## License
This program is free software distributed under the GNU GPL 3,
for license details see at _'license.txt'_ file, distributed with
this program, or see at <http://www.gnu.org/licenses/>.

