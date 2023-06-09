#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    Jun 15, 2022 04:31:25 PM CDT  platform: Windows NT
import subprocess
import sys
import threading
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, HORIZONTAL
from GUI import autoScroll, errorPopup, statResults
import globals
from GUI.Window import Window
from SimAnalysis import simGraph
from SimCommunication import simSetup


class ReviewGUI(Window):
    def __init__(self, top=None, previous=None, home=None, swarmData=None, demandFrame=None):
        """This class configures and populates the toplevel Window.
           top is the toplevel containing Window."""
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
        self.username = globals.username
        self.previous = previous
        self.home = home  # reference to the home screen that is passed to the Results screen after testing
        self.swarmData = swarmData
        self.demandFrame = demandFrame
        self.test_name = None
        self.next = None

        self.BaseFrame = tk.Frame(self.top)
        self.BaseFrame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.BaseFrame.configure(relief='groove')
        self.BaseFrame.configure(borderwidth="2")
        self.BaseFrame.configure(relief="groove")
        self.BaseFrame.configure(background="#000000")

        self.SwarmPropertiesLabel = tk.Label(self.BaseFrame)
        self.SwarmPropertiesLabel.place(relx=0.406, rely=0.076, height=40, width=240)
        self.SwarmPropertiesLabel.configure(background="#000000")
        self.SwarmPropertiesLabel.configure(compound='left')
        self.SwarmPropertiesLabel.configure(disabledforeground="#a3a3a3")
        self.SwarmPropertiesLabel.configure(font="-family {Arial} -size 24")
        self.SwarmPropertiesLabel.configure(foreground="#f2b83d")
        self.SwarmPropertiesLabel.configure(text='''Review and Test''')

        self.BackButton = tk.Button(self.BaseFrame)
        self.BackButton.place(relx=0.906, rely=0.107, height=44, width=107)
        self.BackButton.configure(activebackground="#f2b83d")
        self.BackButton.configure(activeforeground="#000000")
        self.BackButton.configure(background="#f2b83d")
        self.BackButton.configure(command=lambda: self.go_back())
        self.BackButton.configure(compound='center')
        self.BackButton.configure(disabledforeground="#a3a3a3")
        self.BackButton.configure(font="-family {Arial} -size 9")
        self.BackButton.configure(foreground="#000000")
        self.BackButton.configure(highlightbackground="#d9d9d9")
        self.BackButton.configure(highlightcolor="black")
        self.BackButton.configure(pady="0")
        self.BackButton.configure(text='''Back''')

        self.UsernameLabel = tk.Label(self.BaseFrame)
        self.UsernameLabel.place(relx=0.68, rely=0.015, height=60, width=285)
        self.UsernameLabel.configure(anchor='nw')
        self.UsernameLabel.configure(background="#000000")
        self.UsernameLabel.configure(compound='left')
        self.UsernameLabel.configure(disabledforeground="#a3a3a3")
        self.UsernameLabel.configure(font="-family {Arial} -size 13")
        self.UsernameLabel.configure(foreground="#f2b83d")
        self.UsernameLabel.configure(text='''Logged in as: {}'''.format(self.username))

        self.LogOutButton = tk.Button(self.BaseFrame)
        self.LogOutButton.place(relx=0.906, rely=0.015, height=44, width=107)
        self.LogOutButton.configure(activebackground="#f2b83d")
        self.LogOutButton.configure(activeforeground="#000000")
        self.LogOutButton.configure(background="#f2b83d")
        self.LogOutButton.configure(command=lambda: self.log_out_click())
        self.LogOutButton.configure(compound='center')
        self.LogOutButton.configure(disabledforeground="#a3a3a3")
        self.LogOutButton.configure(font="-family {Arial} -size 9")
        self.LogOutButton.configure(foreground="#000000")
        self.LogOutButton.configure(highlightbackground="#d9d9d9")
        self.LogOutButton.configure(highlightcolor="black")
        self.LogOutButton.configure(pady="0")
        self.LogOutButton.configure(text='''Log Out''')

        self.SwarmDetailsLabel = tk.Label(self.BaseFrame)
        self.SwarmDetailsLabel.place(relx=0.654, rely=0.228, height=21, width=154)
        self.SwarmDetailsLabel.configure(activebackground="#f9f9f9")
        self.SwarmDetailsLabel.configure(anchor='w')
        self.SwarmDetailsLabel.configure(background="#000000")
        self.SwarmDetailsLabel.configure(compound='left')
        self.SwarmDetailsLabel.configure(disabledforeground="#a3a3a3")
        self.SwarmDetailsLabel.configure(font="-family {Arial} -size 17")
        self.SwarmDetailsLabel.configure(foreground="#f2b83d")
        self.SwarmDetailsLabel.configure(highlightbackground="#d9d9d9")
        self.SwarmDetailsLabel.configure(highlightcolor="black")
        self.SwarmDetailsLabel.configure(text='''Swarm Details''')

        self.DemandDetailsLabel = tk.Label(self.BaseFrame)
        self.DemandDetailsLabel.place(relx=0.227, rely=0.228, height=21, width=171)
        self.DemandDetailsLabel.configure(activebackground="#f9f9f9")
        self.DemandDetailsLabel.configure(anchor='w')
        self.DemandDetailsLabel.configure(background="#000000")
        self.DemandDetailsLabel.configure(compound='left')
        self.DemandDetailsLabel.configure(disabledforeground="#a3a3a3")
        self.DemandDetailsLabel.configure(font="-family {Arial} -size 17")
        self.DemandDetailsLabel.configure(foreground="#f2b83d")
        self.DemandDetailsLabel.configure(highlightbackground="#d9d9d9")
        self.DemandDetailsLabel.configure(highlightcolor="black")
        self.DemandDetailsLabel.configure(text='''Demand Details''')

        self.TestButton = tk.Button(self.BaseFrame)
        self.TestButton.place(relx=0.461, rely=0.609, relheight=0.067, relwidth=0.084)
        self.TestButton.configure(activebackground="#f2b83d")
        self.TestButton.configure(activeforeground="#000000")
        self.TestButton.configure(background="#f2b83d")
        self.TestButton.configure(command=lambda: self.test())
        self.TestButton.configure(compound='center')
        self.TestButton.configure(disabledforeground="#a3a3a3")
        self.TestButton.configure(font="-family {Arial} -size 9")
        self.TestButton.configure(foreground="#000000")
        self.TestButton.configure(highlightbackground="#d9d9d9")
        self.TestButton.configure(highlightcolor="black")
        self.TestButton.configure(pady="0")
        self.TestButton.configure(text='''Test''')

        self.SwarmScroll = autoScroll.ScrolledText(self.BaseFrame)
        self.SwarmScroll.place(relx=0.55, rely=0.274, relheight=0.708, relwidth=0.32)
        self.SwarmScroll.configure(background="#f2b83d")
        self.SwarmScroll.configure(borderwidth="0")
        self.SwarmScroll.configure(font="-family {Courier} -size 13")
        self.SwarmScroll.configure(foreground="black")
        self.SwarmScroll.configure(highlightbackground="#d9d9d9")
        self.SwarmScroll.configure(highlightcolor="black")
        self.SwarmScroll.configure(insertbackground="black")
        self.SwarmScroll.configure(insertborderwidth="3")
        # the gold select will be white, and black background select will be gray
        self.SwarmScroll.configure(selectbackground="#ffffff")
        self.SwarmScroll.configure(selectforeground="black")
        self.SwarmScroll.configure(wrap="none")
        self.SwarmScroll.configure(spacing1=4)
        self.SwarmScroll.configure(spacing3=4)
        self.SwarmScroll.tag_configure("evenline", background="#000000", foreground="#f2b83d",
                                       selectbackground="#c4c4c4", selectforeground="black")

        self.DemandScroll = autoScroll.ScrolledText(self.BaseFrame)
        self.DemandScroll.place(relx=0.133, rely=0.274, relheight=0.709, relwidth=0.32)
        self.DemandScroll.configure(background="#f2b83d")
        self.DemandScroll.configure(font="-family {Courier} -size 13")
        self.DemandScroll.configure(foreground="black")
        self.DemandScroll.configure(highlightbackground="#d9d9d9")
        self.DemandScroll.configure(highlightcolor="black")
        self.DemandScroll.configure(insertbackground="black")
        self.DemandScroll.configure(insertborderwidth="3")
        self.DemandScroll.configure(selectforeground="black")
        self.DemandScroll.configure(wrap="none")
        self.DemandScroll.configure(spacing1=4)
        self.DemandScroll.configure(spacing3=4)
        # the gold select will be white, and black background select will be gray
        self.DemandScroll.configure(selectbackground="#ffffff")
        self.DemandScroll.tag_configure("oddline", background="#000000", foreground="#f2b83d",
                                        selectbackground="#c4c4c4", selectforeground="black")
        self.DemandScroll.tag_configure("title", justify="center", font=("Courier", 13, "bold"))

        if self.swarmData is not None:
            self.retrieve_data()

    def retrieve_data(self):
        self.set_demand()
        self.set_swarm()
        # color the SwarmScroll based on the number of lines inserted
        self.color()
        self.SwarmScroll.configure(state="disabled")
        self.DemandScroll.configure(state="disabled")

    # set DemandScroll with info pertaining to this test's demand
    def set_demand(self):
        if self.swarmData is None:
            messagebox.showinfo(title="Error", message="Fatal - Could not locate previous swarm data.")
            self.BaseFrame.destroy()
            del self
        elif self.demandFrame is None:
            messagebox.showinfo(title="Error", message="Fatal - Could not locate previous demand data.")
            self.BaseFrame.destroy()
            del self
        else:
            index = 0
            for task in self.demandFrame.tasks:
                if index % 2 == 0:
                    tag = "evenline"
                else:
                    tag = "oddline"
                # each task represents a TaskFrame as defined in statDemand
                self.DemandScroll.insert(tk.END, "Task {}\n".format(index), (tag, "title"))
                profile = task.DemandProfileEntry.get()
                self.DemandScroll.insert(tk.END, "Task Profile: {}\n".format(profile), tag)
                self.DemandScroll.insert(tk.END, "Range:        {}\n".format(task.RangeEntry.get()), tag)
                if profile == "custom":
                    self.DemandScroll.insert(tk.END, "Function:     {}\n".format(task.FunctionEntry.get()), tag)
                else:
                    # we need an amplitude and possibly a period
                    self.DemandScroll.insert(tk.END, "Amplitude:    {}\n".format(task.AmplitudeEntry.get()), tag)
                    if profile != "random":
                        self.DemandScroll.insert(tk.END, "Period:       {}\n".format(task.PeriodEntry.get()), tag)
                index += 1

    # set SwarmScroll with info pertaining to swarm behavior
    def set_swarm(self):
        # we validated data before this point, so simply display the data
        self.SwarmScroll.insert(tk.END, "Pop_size: ".ljust(22) + self.swarmData.get("Pop_size") + "\n")
        self.SwarmScroll.insert(tk.END, "Thresh_init: ".ljust(22) + self.swarmData.get("Thresh_init") + "\n")
        self.SwarmScroll.insert(tk.END, "Prob_check: ".ljust(22) + self.swarmData.get("Prob_check") + "\n")
        self.SwarmScroll.insert(tk.END, "Response_prob: ".ljust(22) + self.swarmData.get("Response_prob") + "\n")
        self.SwarmScroll.insert(tk.END, "Task_selection: ".ljust(22) + self.swarmData.get("Task_selection") + "\n")
        self.SwarmScroll.insert(tk.END, "Intensity_variation: ".ljust(22) +
                                self.swarmData.get("Intensity_variation") + "\n")
        if self.swarmData.get("Intensity_aging_max") != "":
            self.SwarmScroll.insert(tk.END, "Aging_max: ".ljust(22) + self.swarmData.get("Intensity_aging_max") + "\n")
        if self.swarmData.get("Intensity_aging_min") != "":
            self.SwarmScroll.insert(tk.END, "Aging_min: ".ljust(22) + self.swarmData.get("Intensity_aging_min") + "\n")
        if self.swarmData.get("Intensity_aging_up") != "":
            self.SwarmScroll.insert(tk.END, "Aging_up: ".ljust(22) + self.swarmData.get("Intensity_aging_up") + "\n")
        if self.swarmData.get("Intensity_aging_down") != "":
            self.SwarmScroll.insert(tk.END, "Aging_down: ".ljust(22) +
                                    self.swarmData.get("Intensity_aging_down") + "\n")
        self.SwarmScroll.insert(tk.END, "Kill_number: ".ljust(22) + self.swarmData.get("Kill_number") + "\n")
        self.SwarmScroll.insert(tk.END, "First_extinction: ".ljust(22) + self.swarmData.get("First_extinction") + "\n")
        self.SwarmScroll.insert(tk.END, "Extinction_period: ".ljust(22) +
                                self.swarmData.get("Extinction_period") + "\n")
        self.SwarmScroll.insert(tk.END, "Spontaneous_response: ".ljust(22) +
                                self.swarmData.get("Spontaneous_response_prob") + "\n")
        self.SwarmScroll.insert(tk.END, "Hetero_range_max: ".ljust(22) + self.swarmData.get("Hetero_range_max") + "\n")
        self.SwarmScroll.insert(tk.END, "Hetero_range_min: ".ljust(22) + self.swarmData.get("Hetero_range_min") + "\n")
        self.SwarmScroll.insert(tk.END, "Hetero_radius_max: ".ljust(22) +
                                self.swarmData.get("Hetero_radius_max") + "\n")
        self.SwarmScroll.insert(tk.END, "Hetero_radius_min: ".ljust(22) +
                                self.swarmData.get("Hetero_radius_min") + "\n")
        self.SwarmScroll.insert(tk.END, "RP_gaussian_mu: ".ljust(22) + self.swarmData.get("RP_gaussian_mu") + "\n")
        self.SwarmScroll.insert(tk.END, "RP_gaussian_std: ".ljust(22) + self.swarmData.get("RP_gaussian_std") + "\n")
        self.SwarmScroll.insert(tk.END, "Thresh_dynamic: ".ljust(22) + self.swarmData.get("Thresh_dynamic") + "\n")
        if self.swarmData.get("Thresh_dynamic_init") != "":
            self.SwarmScroll.insert(tk.END, "Thresh_dynamic_init: ".ljust(22) +
                                    self.swarmData.get("Thresh_dynamic_init") + "\n")
        if self.swarmData.get("Thresh_dynamic") != "0":
            self.SwarmScroll.insert(tk.END, "Thresh_increase: ".ljust(22) +
                                    self.swarmData.get("Thresh_increase") + "\n")
            self.SwarmScroll.insert(tk.END, "Thresh_decrease: ".ljust(22) +
                                    self.swarmData.get("Thresh_decrease") + "\n")

    def color(self):
        # get the number of lines, and tag every even line
        end = int(self.SwarmScroll.index('end-1c').split('.')[0])
        for i in range(end):
            if i % 2 == 0:
                self.SwarmScroll.tag_add("evenline", "{}.0".format(i), "{}.0 wordstart".format(i + 1))

    def go_back(self):
        self.destroy()

    # called when the user clicks the logout button
    def log_out_click(self):
        if messagebox.askokcancel(title="Log Out", message="Log Out? Any untested data will be lost."):
            self.log_out()

    # called when the user accepts logging out from this or any subsequent window
    def log_out(self):
        self.BaseFrame.destroy()
        self.next = None
        self.previous.log_out()
        del self

    def destroy(self):
        self.BaseFrame.destroy()
        del self

    # This method will generate a test name and timestep window
    def test(self):
        # write the args to the params file and run
        # task window is responsible for validating tasks
        # swarm window is responsible for validating swarm specification
        # get the name for the test and the number of timesteps to simulate
        self.get_final_args()

    # Validate the test name by attempting to make the test directory
    def setup_test(self):
        # Write the number of timesteps (which was validated) and other args to sim
        error = simSetup.write_params(self.previous.previous.collect_tasks(), self.previous.collect_data())
        if error != "":
            errorPopup.ErrorGui(top=self.top, error_list=list(error), title="Error Writing Sim Parameters")
            return False
        else:
            # We need to ensure name is legal for filesystem and not already in use
            # Since making a validation method for directory names will be complicated
            # and messy, it is better to just attempt to make the directory since the
            # user will not be able to enter any input after this point.
            error = simSetup.setup_test(self.test_name)
            if error != "":
                messagebox.showinfo(title="Title Error", message=("Cannot name the test {}."
                                                                  .format(self.test_name) + ": " + error))
                return False
        return True

    # This method runs sim. This method assumes that all arguments for sim were validated and written
    def execute_test(self):
        error = ""
        # we no longer need the task or swarm specification screens
        self.demandFrame.destroy()
        self.previous.destroy()
        # Display progress bar widget to alert user to progress
        popup, progressBar, info_label = self.place_pgbar()
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("bar.Horizontal.TProgressbar", foreground="#f2b83d", background="#000000")
        progressBar.configure(orient=HORIZONTAL, length=250, mode='determinate',
                              style="bar.Horizontal.TProgressbar")
        # gen is a generator that will output lines from sim as they are generated
        increment = 250 / globals.timesteps
        popup.update_idletasks()
        try:
            # This loop has to be very simple to prevent tkinter freezing or skipping values
            for val in simSetup.run():
                info_label.configure(text=val)
                progressBar["value"] += increment
                popup.update_idletasks()
        except subprocess.CalledProcessError as e:
            # Sim ended on an error code.
            popup.destroy()
            messagebox.showinfo(title="Error Executing Test", message=e.output)
            error = simSetup.finish_test(self.test_name)
            if error != "":
                messagebox.showinfo(title="Error Saving Test", message=error)
            # Go back to the details screen, or the home screen
            self.home.refresh()
            self.destroy()
            return

        # We need to copy files and generate the graphs in the user dir
        # This takes time, so we will do it on a separate thread from the GUI
        def background_graph():
            # after the test is over, attempt to copy the files to the user dir
            info_label.configure(text="Copying test files to user directory...")
            error_msg = simSetup.finish_test(self.test_name)
            # There was an error copying files, so we will be unable to generate graphs, go home
            if error_msg != "":
                popup.destroy()
                self.finish(error_msg)
            else:
                info_label.configure(text="Generating Demand Graphs...")
                progressBar["value"] = 0.0
                popup.update_idletasks()
                error_msg = simGraph.generate_demand(self.test_name)
                progressBar['value'] += 33.3
                info_label.configure(text="Generating Accuracy Graphs...")
                popup.update_idletasks()
                error_msg += simGraph.generate_accuracy(self.test_name)
                progressBar['value'] += 33.3
                info_label.configure(text="Generating Summary Graphs...")
                popup.update_idletasks()
                error_msg += simGraph.generate_summary(self.test_name)
                progressBar['value'] += 33.3
                popup.update_idletasks()
                # Now that we are finished, we can exit the thread and move to the next screen
                popup.destroy()
                self.finish(error_msg)
        # Execute the above method on a separate thread
        threading.Thread(target=background_graph).start()

    # This method is called when the test and all other work is done.
    def finish(self, error):
        if error != "":
            errorPopup.ErrorGui(top=self.top, error_list=list(error), title="Graph Generation Error")
        self.BaseFrame.destroy()
        statResults.ResultGui(top=self.top, home=self.home, name=self.test_name)
        del self

    # Show a progressbar for test execution. Returns a label to provide more information.
    # It is the responsibility of the caller to destroy the returned gui elements
    def place_pgbar(self):
        pb_window = tk.Toplevel(self.top)
        self.top.eval(f'tk::PlaceWindow {str(pb_window)} center')
        pb_window["bg"] = "black"
        pb_window.geometry('300x100')
        pb_window.resizable(False, False)
        pb_window.grab_set()
        pb_window.tk.call('wm', 'iconphoto', pb_window._w, globals.icon)
        pb_window.title("Running Test")
        base_frame = tk.Frame(pb_window, width=200, height=200, borderwidth=2, bg="black")
        base_frame.pack()
        info_label = tk.Label(base_frame, text="Starting Test...", bg="black", fg="#f2b83d",
                              font="-family {Arial} -size 13")
        info_label.grid(row=0, column=0, pady=5)
        progressBar = ttk.Progressbar(base_frame, orient=HORIZONTAL,
                                      length=100.0, mode='determinate')
        progressBar.grid(row=1, column=0, pady=5)
        return pb_window, progressBar, info_label

    # Create a popup window to get the number timesteps and test name
    def get_final_args(self):
        query_window = tk.Toplevel(self.top)
        self.top.eval(f'tk::PlaceWindow {str(query_window)} center')
        query_window["bg"] = "black"
        query_window.geometry('300x200')
        query_window.resizable(False, False)
        query_window.grab_set()
        query_window.tk.call('wm', 'iconphoto', query_window._w, globals.icon)
        query_window.title("Execute Test")
        base_frame = tk.Frame(query_window, width=200, height=200, borderwidth=2, bg="black")
        base_frame.pack()
        n_label = tk.Label(base_frame, text="Test Name:", bg="black", fg="#f2b83d",
                           font="-family {Arial} -size 13")
        n_label.grid(row=0, column=0, pady=5)
        name_input = tk.Entry(base_frame, bg="#f2b83d", fg="black", width=15, font="-family {Arial} -size 13")
        name_input.grid(row=1, column=0)
        t_label = tk.Label(base_frame, text="Timesteps:", bg="black", fg="#f2b83d",
                           font="-family {Arial} -size 13")
        t_label.grid(row=2, column=0, pady=5)
        timesteps_input = tk.Entry(base_frame, bg="#f2b83d", fg="black", width=15, font="-family {Arial} -size 13")
        timesteps_input.grid(row=3, column=0)

        # This will be called when the submit button is clicked. This method will call a validation
        # method. If the data is validated, then we will call the execute_test method.
        def on_submit():
            try:
                timesteps = int(timesteps_input.get())
                if timesteps < 1:
                    messagebox.showinfo(title="Error", message="Timesteps must be positive.")
                    return
            except ValueError:
                messagebox.showinfo(title="Error", message="Timesteps must be a positive integer.")
                return

            # We have ensured timesteps is a number, so we will run with the number and proposed name
            self.test_name = name_input.get()
            globals.timesteps = timesteps
            if self.setup_test():
                query_window.grab_release()
                query_window.destroy()
                self.execute_test()

        # this will be called when the popup is closed
        def on_closing():
            query_window.grab_release()
            query_window.destroy()

        query_window.protocol("WM_DELETE_WINDOW", on_closing)
        # For some reason, a 10 x 2 pixel button takes up more than 10 x 2 pixels...
        button_close = tk.Button(base_frame, width=10, height=2, text="Submit", background="#f2b83d",
                                 command=lambda: on_submit())
        button_close.grid(row=4, column=0, padx=10, pady=10)
