import tkinter as tk
from sys import platform
from GUI import statLogin
from Storage import directoryAccess
import globals

top = None
login = None


def main():
    """Main entry point for the application."""
    directoryAccess.setup()  # setup directory locations
    global top, login
    top = tk.Tk()
    top.protocol('WM_DELETE_WINDOW', top.destroy)
    top.geometry("{}x{}+0+0".format(top.winfo_screenwidth(), top.winfo_screenheight()))
    if platform == "linux" or platform == "linux2":
        # linux
        top.attributes("-zoomed", True)
    elif platform == "darwin" or platform == "win32" or platform == "cygwin":
        # OS X and Windows
        top.state("zoomed")
    # this is a little messy, but results in a clearer icon
    globals.icon = tk.PhotoImage(file='../Resources/bee.png')
    top.tk.call('wm', 'iconphoto', top._w, globals.icon)
    top.minsize(300, 300)
    top.resizable(True, True)
    top.title("STAT")
    top.configure(background="#000000")
    top.configure(highlightbackground="#d9d9d9")
    top.configure(highlightcolor="black")
    login = statLogin.LoginGui(top)
    top.mainloop()


if __name__ == '__main__':
    main()
