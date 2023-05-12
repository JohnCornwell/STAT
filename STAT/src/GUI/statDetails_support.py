#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    Jun 15, 2022 03:24:44 PM CDT  platform: Windows NT

import tkinter as tk
from src.GUI import statDetails


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = statDetails.Window(_top1)
    root.mainloop()


if __name__ == '__main__':
    main()
