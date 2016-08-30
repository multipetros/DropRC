#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# DropRC Project, Client part
# Copyright (c) 2013-2016, Petros Kyladitis
#
# This program is free software distributed under the GNU GPL 3,
# for license details see at 'license.txt' file, distributed with
# this project, or see at <http://www.gnu.org/licenses/>.

import time
import os
import re
import datetime
from ini import ini

def main():
    print "DropRC Client 1.0 Copyright (c) 2013-2016, Petros Kyladitis <www.multipetros.gr>\n"
    options = ini("client")
    commands_file = options["commands_file"]
    results_file = options["results_file"]
    delay = options["delay"]
    valid_commands = ["screenshot", "download", "rm", "rmdir", "rename", "mkdir", "ls", "copy"]
    valid_params = [1, 2, 1, 1, 2, 1, 1, 2]
    while True:
        if not(os.path.exists(commands_file)) and not(os.path.exists(results_file)):
            user_input = ""
            user_cmd = ""
            print "\nListening commands. At new line, enter '.' to end the input (send commands to server), '?' to see acceptable commands, or 'q' to quit."
            while user_cmd != ".":
                user_cmd = raw_input("> ")
                splitted_cmd = re.split(''' (?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', user_cmd)
                if splitted_cmd[0] in valid_commands:
                    if valid_params[valid_commands.index(splitted_cmd[0])] == (len(splitted_cmd) - 1):
                        user_input = user_input + user_cmd + "\n"
                    else:
                        print "Invalid number of parameters! Expected: " + str(valid_params[valid_commands.index(splitted_cmd[0])])
                elif user_cmd == "?":
                    for i in range(0, len(valid_commands)):
                        print valid_commands[i] + " -> expecting " + str(valid_params[i]) + " param(s)."
                elif user_cmd == "q":
                    return
                elif user_cmd == ".":
                    pass
                else:
                    print "Command not found! Valid commands: " + ", ".join(valid_commands)
            try:
                print "Writing commands file"
                fcommands = open(commands_file, 'w')
                fcommands.write(user_input)
                fcommands.close()
                print "Done!\n"
            except Exception as err:
                print err
        else:
            if os.path.exists(results_file):
                fresults = open(results_file, 'r')
                lines = fresults.read()
                fresults.close()
                print lines
                os.remove(results_file)
            print "Waiting for server response (next check at " + str(addSecs(delay)) + ")..."
            time.sleep(delay)

def addSecs(secs):
    now = datetime.datetime.now().time()
    checkdate = datetime.datetime(100, 1, 1, now.hour, now.minute, now.second)
    checkdate = checkdate + datetime.timedelta(seconds=secs)
    return checkdate.time()

if __name__ == "__main__":
    main()
