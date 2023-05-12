# This module is a collection of useful methods that do not fit in
# another module of this program
import re

# regular expressions for positive ints and floats
intPattern = re.compile(r"^\d+$")
doublePattern = re.compile(r"^\d+[.]\d+$")


def valid_int(string):
    return intPattern.match(string)


def valid_double(string):
    return doublePattern.match(string)


# returns True if the given string is recognized by either regex
def valid_numeric(string):
    return doublePattern.match(string) or intPattern.match(string)


# A method that will trim trailing zeroes from strings representing
# nonzero floating point numbers
def cut(string):
    if valid_double(string):
        try:
            val = float(string)
            if val != 0 and not val.is_integer():
                return string.rstrip("0")
            elif val.is_integer():
                return string.rstrip("0") + "0"
            else:
                return string
        except ValueError:
            # unexpected casting error, so return
            return string
    else:
        # not a string we can cut
        return string
