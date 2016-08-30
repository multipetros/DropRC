#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# DropRC Project, common functions for read/write options from ini file
# Copyright (c) 2013-2016, Petros Kyladitis
#
# This program is free software distributed under the GNU GPL 3,
# for license details see at 'license.txt' file, distributed with
# this project, or see at <http://www.gnu.org/licenses/>.

import os
import ConfigParser

def ini(section):
    commands_file = "drc.commands"
    results_file = "drc.results"
    sync_folder_path = "./"
    delay = 30
    INI_FILE = "droprc.ini"
    INI_SECTION = section
    config = ConfigParser.RawConfigParser()
    if not os.path.exists(INI_FILE):
        config.add_section(INI_SECTION)
        with open(INI_FILE, "wb") as configfile:
            config.write(configfile)
    else:
        config.read(INI_FILE)
        if not config.has_section(INI_SECTION):
            config.add_section(INI_SECTION)
            with open(INI_FILE, "wb") as configfile:
                config.write(configfile)
    if config.has_option(INI_SECTION, "delay"):
        ini_delay = config.getint(INI_SECTION, "delay")
        if ini_delay > 0:
            delay = ini_delay
    if config.has_option(INI_SECTION, "sync_folder_path"):
        ini_sync_folder_path = config.get(INI_SECTION, "sync_folder_path")
        if ini_sync_folder_path != "":
            sync_folder_path = ini_sync_folder_path
    print "- Current config -\nSecs delay.....: " + str(delay) + "\nSync folder...: " + sync_folder_path
    keep = raw_input("Use this? [y/n]: ")
    if keep[:1].lower() == "n":
        print "\nEnter the new values. Enter blank string to keep the default."
        usr_delay = raw_input("Secs delay [" + str(delay) + "]: ")
        if usr_delay.isdigit():
            delay = int(usr_delay)
            config.set(INI_SECTION, "delay", delay)
        usr_sync_folder_path= raw_input("Sync folder [" + sync_folder_path + "]: ")
        if usr_sync_folder_path != "":
            if usr_sync_folder_path.endswith(":"):
                sync_folder_path = usr_sync_folder_path + os.sep
            else:
                sync_folder_path = usr_sync_folder_path
            config.set(INI_SECTION, "sync_folder_path", sync_folder_path)
        with open(INI_FILE, "wb") as configfile:
            config.write(configfile)
    options = {"delay":delay, "commands_file":os.path.join(sync_folder_path,commands_file), "results_file":os.path.join(sync_folder_path,results_file)}
    return options
