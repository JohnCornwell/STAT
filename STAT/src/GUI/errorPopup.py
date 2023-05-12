#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    Oct 01, 2022 05:05:13 PM CDT  platform: Windows NT


import sys
import tkinter as tk
import tkinter.ttk as ttk
import globals
from GUI import autoScroll


# This class is meant to display an error window that can show multiple errors
# in a ScrollBox.
class ErrorGui:
    def __init__(self, top=None, error_list=None, title="Error"):
        """This class is used to generate an error popup window that
        displays multiple error messages in a scrolled textbox"""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40'  # X11 color: #666666
        _ana2color = 'beige'  # X11 color: #f5f5dc
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        self.top = top
        self.error_list = error_list
        self.title = title

        self.task_window = tk.Toplevel(self.top)
        self.task_window["bg"] = "black"
        self.task_window.geometry('400x300')
        self.task_window.resizable(False, False)
        self.task_window.grab_set()
        self.task_window.tk.call('wm', 'iconphoto', self.task_window._w, globals.icon)
        self.task_window.title(self.title)

        self.ErrorFrame = tk.Frame(self.task_window)
        self.ErrorFrame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.ErrorFrame.configure(relief='groove')
        self.ErrorFrame.configure(borderwidth="2")
        self.ErrorFrame.configure(relief="groove")
        self.ErrorFrame.configure(background="#000000")
        self.ErrorFrame.configure(highlightbackground="#d9d9d9")
        self.ErrorFrame.configure(highlightcolor="black")

        self.ErrorScrollText = autoScroll.ScrolledText(self.ErrorFrame)
        self.ErrorScrollText.place(relx=0.1, rely=0.3, relheight=0.5, relwidth=0.8)
        self.ErrorScrollText.configure(background="#f2b83d")
        self.ErrorScrollText.configure(font="-family {Arial} -size 13")
        self.ErrorScrollText.configure(foreground="black")
        self.ErrorScrollText.configure(highlightbackground="#d9d9d9")
        self.ErrorScrollText.configure(highlightcolor="black")
        self.ErrorScrollText.configure(insertbackground="black")
        self.ErrorScrollText.configure(insertborderwidth="3")
        self.ErrorScrollText.configure(selectbackground="#c4c4c4")
        self.ErrorScrollText.configure(selectforeground="black")
        self.ErrorScrollText.configure(wrap="none")
        # add extra space under a displayed error
        self.ErrorScrollText.configure(spacing3="5")

        self.TitleLabel = tk.Label(self.ErrorFrame)
        self.TitleLabel.place(relx=0, rely=0.05, relheight=0.1, relwidth=1)
        self.TitleLabel.configure(activebackground="#f9f9f9")
        self.TitleLabel.configure(anchor='center')
        self.TitleLabel.configure(background="#020202")
        self.TitleLabel.configure(compound='left')
        self.TitleLabel.configure(disabledforeground="#a3a3a3")
        self.TitleLabel.configure(font="-family {Arial} -size 15")
        self.TitleLabel.configure(foreground="#f2b83d")
        self.TitleLabel.configure(highlightbackground="#d9d9d9")
        self.TitleLabel.configure(highlightcolor="black")
        self.TitleLabel.configure(text=title)

        self.OKButton = tk.Button(self.ErrorFrame)
        self.OKButton.place(relx=0.39, rely=0.871, height=27, width=84)
        self.OKButton.configure(activebackground="beige")
        self.OKButton.configure(activeforeground="#000000")
        self.OKButton.configure(background="#f2b83d")
        self.OKButton.configure(compound='left')
        self.OKButton.configure(disabledforeground="#a3a3a3")
        self.OKButton.configure(font="-family {Arial} -size 10")
        self.OKButton.configure(foreground="#000000")
        self.OKButton.configure(highlightbackground="#f2b83d")
        self.OKButton.configure(highlightcolor="black")
        self.OKButton.configure(pady="0")
        self.OKButton.configure(command=lambda: self.close())
        self.OKButton.configure(text='''OK''')

        if self.error_list is not None:
            self.fill_text()
        else:
            self.ErrorScrollText.insert(0, "No error was provided.")

    def fill_text(self):
        for error in self.error_list:
            self.ErrorScrollText.insert(tk.END, error + "\n")

    def close(self):
        self.task_window.grab_release()
        self.task_window.destroy()