# This file handles high level directory access by the application
# including accessing a directory for a given user.

import os
from os.path import normpath as normpath
import shutil
import globals

# Stylistically denotes as private to encourage use of access methods
__home = ""  # home directory
__accounts = ""
__user = ""  # this user's directory
__recovery = ""  # recovery directory


# This method is responsible for setting global directoy locations
def setup():
    set_home()
    set_account()
    set_recovery()


def set_home():
    global __home
    __home = os.getcwd()


# This method sets the location of the account directory and assumes the home
# directory is set. If the home directory is not set, this method will throw an error.
def set_account():
    global __accounts
    __accounts = normpath(__home + "/../Users")


# This method sets the location of the Recovery folder in the User directory.
# This method assumes that the set_account method was already called
def set_recovery():
    global __recovery
    __recovery = normpath(__accounts + "/Recovery")


def get_home():
    return __home


def get_user():
    return __user


def get_recovery():
    return __recovery


def login_user(name):
    global __user
    if os.path.exists(normpath(__accounts + "/" + name)) and name != "Recovery":
        globals.username = name
        __user = normpath(__accounts + "/" + name)
        return ""
    elif name == "Recovery":
        return "You are unable to access Recovery as an account."
    else:
        return "The user " + name + " does not exist."


def logout_user():
    global __user
    __user = ""
    globals.username = ""


def create_user(name):
    if os.path.exists(normpath(__accounts + "/" + name)):
        return "User " + name + " already exists."
    else:
        try:
            os.mkdir(normpath(__accounts + "/" + name))
        except OSError:
            return "Unable to create user directory for " + name + "."
        return ""


def delete_user(name):
    if os.path.exists(normpath(__accounts + "/" + name)):
        try:
            shutil.rmtree(normpath(__accounts + "/" + name))
        except OSError:
            return "Unable to delete user directory for " + name + "."
        return ""
    else:
        return "Cannot delete " + name + ": User does not exist."
