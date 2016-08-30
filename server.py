#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# DropRC Project, Server part
# Copyright (c) 2013-2016, Petros Kyladitis
#
# This program is free software distributed under the GNU GPL 3,
# for license details see at 'license.txt' file, distributed with
# this project, or see at <http://www.gnu.org/licenses/>.

import time
import os
import shutil
import urllib
import Image
import ImageGrab
from ini import ini

def main():
    print "DropRC Server 1.0 Copyright (c) 2013-2016, Petros Kyladitis <www.multipetros.gr>"
    options = ini("server")
    commands_file = options["commands_file"]
    results_file = options["results_file"]
    delay = options["delay"]
    print "\nServer is running..."
    while True:
        if os.path.exists(commands_file):
            output = ""
            commands = []
            fcmd = open(commands_file, 'r')
            lines = fcmd.read()
            commands = lines.split("\n")
            fcmd.close()
            for command in commands:
                if command.startswith("screenshot"):
                    cmd = command.split(" ", 1)
                    output = output + command + "\n"
                    output = output + '\n'.join(cmd_screenshot(cmd[1]))
                    output = output + "\n\n"
                elif command.startswith("download"):
                    cmd = command.split(" ", 2)
                    output = output + command + "\n"
                    output = output + '\n'.join(cmd_download(cmd[1], cmd[2]))
                    output = output + "\n\n"
                elif command.startswith("rm"):
                    cmd = command.split(" ", 1)
                    output = output + command + "\n"
                    output = output + '\n'.join(cmd_rm(cmd[1]))
                    output = output + "\n\n"
                elif command.startswith("rmdir"):
                    cmd = command.split(" ", 1)
                    output = output + command + "\n"
                    output = output + '\n'.join(cmd_rmdir(cmd[1]))
                    output = output + "\n\n"
                elif command.startswith("rename"):
                    cmd = command.split(" ", 2)
                    output = output + command + "\n"
                    output = output + '\n'.join(cmd_rename(cmd[1], cmd[2]))
                    output = output + "\n\n"
                elif command.startswith("mkdir"):
                    cmd = command.split(" ", 1)
                    output = output + command + "\n"
                    output = output + '\n'.join(cmd_mkdir(cmd[1]))
                    output = output + "\n\n"
                elif command.startswith("ls"):
                    cmd = command.split(" ", 1)
                    output = output + command + "\n"
                    output = output + '\n'.join(cmd_ls(cmd[1]))
                    output = output + "\n\n"
                elif command.startswith("copy"):
                    cmd = command.split(" ", 2)
                    output = output + command + "\n"
                    output = output + '\n'.join(cmd_copy(cmd[1], cmd[2]))
                    output = output + "\n\n"
                elif command == "":
                    pass
                else:
                    output = output + command + "\n"
                    output = output + "Command not found!\n\n"
            foutcontents = ""
            for outline in output:
                foutcontents = foutcontents + outline
            fout = open(results_file, 'a')
            fout.write(foutcontents)
            fout.close()
            os.remove(commands_file)
        time.sleep(delay)

def cmd_screenshot(path):
    output = []
    img = ImageGrab.grab()
    try:
        img.save(path)
        output.append("Done!")
    except Exception as err:
        output.append(err)
    return output

def cmd_download(url, path):
    output = []
    try:
        urllib.urlretrieve(url, path)
        output.append("Done!")
    except Exception as err:
        output.append(err)
    return output

def cmd_rm(path):
    output = []
    try:
        os.remove(path)
        output.append("Done!")
    except Exception as err:
        output.append(err)
    return output

def cmd_rmdir(path):
    output = []
    try:
        os.rmdir(path)
        output.append("Done!")
    except Exception as err:
        output.append(err)
    return output

def cmd_rename(old, new):
    output = []
    try:
        os.rename(old, new)
        output.append("Done!")
    except Exception as err:
        output.append(err)
    return output

def cmd_mkdir(path):
    output = []
    try:
        os.makedirs(path)
        output.append("Done!")
    except Exception as err:
        output.append(err)
    return output

def cmd_ls(path):
    output = []
    if not(os.path.isdir(path)):
        output.append("Directory " + path + " not exist!")
        return output
    output.append("Directory " + path + " contents:")
    if not(path.endswith("/")) or not(path.endswith("\\")):
        path = path + "/"
    elements = os.listdir(path)
    for element in elements:
        if os.path.isfile(path + element):
            output.append(element + " - " + str(os.path.getsize(path + element)) + " bytes")
        else:
            output.append(element + " - directory")
    return output

def cmd_copy(source, dest):
    output = []
    if not(os.path.isfile(source)):
        output.append("Source file not found")
        return append
    try:
        shutil.copy(source, dest)
        output.append("Done!")
    except Exception as err:
        output.append(err)
    return output

if __name__ == "__main__":
    main()
