import os
import subprocess
import sys

import globals
from util import valid_int, valid_numeric
from SimCommunication import cycleCheck as cc
from expressionYacc import parser
from expressionLex import lexer
from Storage import testAccess


# This method validates the list of tasks given to it. This method
# assumes that the global number of tasks is set.
def validate_tasks(data):
    error_list = list()
    globals.trees = [None] * globals.numTasks
    # init graph nodes for cycle check
    globals.graph = cc.Graph()
    for i in range(0, globals.numTasks):
        globals.graph.add_node(cc.Node("$t{}".format(i)))

    for i in range(0, globals.numTasks):
        globals.task = i
        globals.node = globals.graph.find_node("$t{}".format(i))
        globals.parserError = False
        globals.errorMessage = ""
        task = data[i]
        path = task.get("Profile")
        # the demand profile is assumed correct because it is a combobox
        if path != "custom" and not valid_numeric(task.get("Amplitude")):
            error_list.append("Task {} Demand Amplitude must be a positive int or float or 0.".format(i))
        if path != "custom" and path != "random" and not valid_int(task.get("Period")):
            error_list.append("Task {} Demand Period must be a positive int.".format(i))
        elif path != "custom" and path != "random" and int(task.get("Period")) == 0:
            error_list.append("Task {} Demand Period must be a positive int.".format(i))
        if not valid_numeric(task.get("Range")):
            error_list.append("Task {} Range must be a positive int or float or 0.".format(i))
        if path == "custom":
            # parse the custom function, and if correct, add to cycle check
            parser.parse(task.get("Function"), lexer=lexer)
            if globals.parserError is True:
                error_list.append("Task {} Function error: {}".format(i, globals.errorMessage))

    if globals.graph.cycle_check():
        error_list.append("There cannot be a cyclic dependency in the provided functions.")
    return error_list


def setup_tasks(data):
    pathString = ""
    ampString = ""
    perString = ""
    ranString = ""
    funString = ""
    for i in range(0, globals.numTasks):
        # task should be a dictionary with entries for each task attribute
        task = data[i]
        path = task.get("Profile").replace(" ", "_")  # paths in sim are snake case

        if i == 0:
            pathString += path
            ranString += task.get("Range")
        else:
            pathString += "," + path
            ranString += "," + task.get("Range")

        if path != "custom":
            if ampString == "":
                ampString += task.get("Amplitude")
            else:
                ampString += "," + task.get("Amplitude")
        else:
            if funString == "":
                funString += task.get("Function")
            else:
                funString += "," + task.get("Function")

        if path != "custom" and path != "random":
            if perString == "":
                perString += task.get("Period")
            else:
                perString += "," + task.get("Period")

    globals.graph.sort()
    orderString = ""
    nodes = globals.graph.get_nodes()
    for i in range(0, len(nodes)):
        if i == 0:
            orderString += nodes[i].name[2:]
        else:
            orderString += "," + nodes[i].name[2:]

    try:
        with open("Sim/params", "w") as params:
            params.write("Rerun -1\n")
            params.write("Print_params 0\n")
            params.write("Print_step 1\n")
            params.write("Num_tasks {}\n".format(globals.numTasks))
            params.write("Max_steps {}\n".format(globals.timesteps))
            params.write("Target_path  " + pathString + "\n")
            params.write("Functions  " + funString + "\n")
            params.write("Range  " + ranString + "\n")
            params.write("Path_amplitude " + ampString + "\n")
            params.write("Path_period " + perString + "\n")
            params.write("Order " + orderString + "\n")
    except IOError:
        return "Could not write to params file."
    return ""


# This method validates the swarm specification given to it.
# The swarm specification should be provided as a dictionary of swarm properties.
def validate_swarm(data):
    error_list = list()
    # intensity variation is turned on
    intensity_variation = data.get("Intensity_variation")
    # dynamic thresholds are turned on
    thresh_dynamic = data.get("Thresh_dynamic")
    population = 0
    try:
        n = int(data.get("Pop_size"))
        if n < 0:
            error_list.append("Population must be a positive int.")
        else:
            population = n
    except ValueError:
        error_list.append("Population must be a positive int.")

    if not valid_numeric(data.get("Thresh_init")):
        error_list.append("Thresh init must be a float with value 0.0 - 1.0, or 2.0, 3.0, 4.0, 5.0, 6.0, or 10.0.")
    else:
        n = float(data.get("Thresh_init"))
        if not (0.0 <= n <= 1.0 or n == 2.0 or n == 3.0 or n == 4.0 or n == 5.0 or n == 6.0 or n == 10.0):
            error_list.append("Thresh init must be a float with value 0.0 - 1.0, or 2.0, 3.0, 4.0, 5.0, 6.0, or 10.0.")

    if not valid_numeric(data.get("Prob_check")):
        error_list.append("Prob Check must be a double between 0.0 and 1.0.")
    else:
        n = float(data.get("Prob_check"))
        if not (0.0 <= n <= 1.0):
            error_list.append("Prob Check must be a double between 0.0 and 1.0.")

    if not valid_numeric(data.get("Response_prob")):
        error_list.append("Response Prob must be a double between 0.0 and 1.0 or equal to 2.0 or 3.0.")
    else:
        n = float(data.get("Response_prob"))
        if not (0.0 <= n <= 1.0 or n == 2.0 or n == 3.0):
            error_list.append("Response Prob must be a double between 0.0 and 1.0 or equal to 2.0 or 3.0.")

    if not valid_numeric(data.get("Spontaneous_response_prob")):
        error_list.append("Spontaneous Response must be a double between 0.0 and 1.0 or equal to 2.0 or 3.0.")
    else:
        n = float(data.get("Spontaneous_response_prob"))
        if not (0.0 <= n <= 1.0 or n == 2.0 or n == 3.0):
            error_list.append("Spontaneous Response must be a double between 0.0 and 1.0 or equal to 2.0 or 3.0.")

    if intensity_variation != "Off":
        # only validate aging when intensity variation is on
        if not valid_numeric(data.get("Intensity_aging_min")):
            error_list.append("Aging Min must be a real number.")
        else:
            n = float(data.get("Intensity_aging_min"))
            if n < 0:
                error_list.append("Aging Min must be a real number.")

        if not valid_numeric(data.get("Intensity_aging_max")):
            error_list.append("Aging Max must be a real number.")
        else:
            n = float(data.get("Intensity_aging_max"))
            if n < 0:
                error_list.append("Aging Max must be a real number.")

        if not valid_numeric(data.get("Intensity_aging_up")):
            error_list.append("Aging Up must be a real number.")
        else:
            n = float(data.get("Intensity_aging_up"))
            if n < 0:
                error_list.append("Aging Up must be a real number.")

        if not valid_numeric(data.get("Intensity_aging_down")):
            error_list.append("Aging Down must be a real number.")
        else:
            n = float(data.get("Intensity_aging_down"))
            if n < 0:
                error_list.append("Aging Down must be a real number.")

    if data.get("Thresh_dynamic_init") == "2" and thresh_dynamic != "2":
        error_list.append("Thresh Dynamic Init may only be 2 when Thresh Dynamic is 2.")
    if thresh_dynamic != "0":
        # dynamic thresholds are on, so increase and decrease should be set
        if not valid_numeric(data.get("Thresh_increase")):
            error_list.append("Thresh Increase must be a real number.")
        else:
            n = float(data.get("Thresh_increase"))
            if n < 0:
                error_list.append("Thresh Increase must be a real number.")

        if not valid_numeric(data.get("Thresh_decrease")):
            error_list.append("Thresh Decrease must be a real number.")
        else:
            n = float(data.get("Thresh_decrease"))
            if n < 0:
                error_list.append("Thresh Decrease must be a real number.")

    if not valid_numeric(data.get("Hetero_range_max")):
        error_list.append("Hetero Range Max must be a real number.")
    else:
        n = float(data.get("Hetero_range_max"))
        if n < 0:
            error_list.append("Hetero Range Max must be a real number.")

    if not valid_numeric(data.get("Hetero_range_min")):
        error_list.append("Hetero Range Min must be a real number.")
    else:
        n = float(data.get("Hetero_range_min"))
        if n < 0:
            error_list.append("Hetero Range Min must be a real number.")

    if not valid_numeric(data.get("Hetero_radius_max")):
        error_list.append("Hetero Radius Max must be a real number.")
    else:
        n = float(data.get("Hetero_radius_max"))
        if n < 0:
            error_list.append("Hetero Radius Max must be a real number.")

    if not valid_numeric(data.get("Hetero_radius_min")):
        error_list.append("Hetero Radius Min must be a real number.")
    else:
        n = float(data.get("Hetero_radius_min"))
        if n < 0:
            error_list.append("Hetero Radius Min must be a real number.")

    if not valid_numeric(data.get("RP_gaussian_mu")):
        error_list.append("RP Gaussian MU must be a real number.")
    else:
        n = float(data.get("RP_gaussian_mu"))
        if n < 0:
            error_list.append("RP Gaussian MU must be a real number.")

    if not valid_numeric(data.get("RP_gaussian_std")):
        error_list.append("RP Gaussian STD must be a real number.")
    else:
        n = float(data.get("RP_gaussian_std"))
        if n < 0:
            error_list.append("RP Gaussian STD must be a real number.")

    if not valid_int(data.get("Kill_number")):
        error_list.append("Kill Number must be an int between 0 and Population.")
    else:
        n = float(data.get("Kill_number"))
        if n < 0 or n > population:
            error_list.append("Kill Number must be an int between 0 and Population.")

    if not valid_int(data.get("First_extinction")):
        error_list.append("First Extinction must be a positive int.")
# Timesteps will be set after this and just before the test is started.
# We can allow extinction after the test which will have no effect
    else:
        n = float(data.get("First_extinction"))
        if n < 0:  # or n > globals.timesteps:
            error_list.append("First Extinction must be a positive int.")

    if not valid_int(data.get("Extinction_period")):
        error_list.append("Extinction Period must be a positive int.")
    else:
        n = float(data.get("Extinction_period"))
        if n <= 0:
            error_list.append("Extinction Period must be a positive int.")
    return error_list


def setup_swarm(data):
    try:
        with open("Sim/params", "a") as params:
            params.write("Pop_size " + data.get("Pop_size") + "\n")
            params.write("Thresh_init " + data.get("Thresh_init") + "\n")
            params.write("Thresh_increase " + data.get("Thresh_increase") + "\n")
            params.write("Thresh_decrease " + data.get("Thresh_decrease") + "\n")
            params.write("Prob_check " + data.get("Prob_check") + "\n")
            params.write("Response_prob " + data.get("Response_prob") + "\n")
            params.write("Task_selection " + data.get("Task_selection").lower() + "\n")
            if data.get("Intensity_variation") == "Off":
                params.write("Intensity_variation 0\n")
                params.write("Intensity_aging 0\n")
            elif data.get("Intensity_variation") == "Share Range":
                params.write("Intensity_variation 1\n")
                params.write("Intensity_aging 1\n")
            else:
                params.write("Intensity_variation 2\n")
                params.write("Intensity_aging 1\n")
            params.write("Intensity_aging_min " + data.get("Intensity_aging_min") + "\n")
            params.write("Intensity_aging_max " + data.get("Intensity_aging_max") + "\n")
            params.write("Intensity_aging_up " + data.get("Intensity_aging_up") + "\n")
            params.write("Intensity_aging_down " + data.get("Intensity_aging_down") + "\n")
            params.write("Kill_number " + data.get("Kill_number") + "\n")
            params.write("First_extinction " + data.get("First_extinction") + "\n")
            params.write("Extinction_period " + data.get("Extinction_period") + "\n")
            params.write("Spontaneous_response_prob " + data.get("Spontaneous_response_prob") + "\n")
            params.write("Hetero_range_max " + data.get("Hetero_range_max") + "\n")
            params.write("Hetero_range_min " + data.get("Hetero_range_min") + "\n")
            params.write("Hetero_radius_max " + data.get("Hetero_radius_max") + "\n")
            params.write("Hetero_radius_min " + data.get("Hetero_radius_min") + "\n")
            params.write("RP_gaussian_mu " + data.get("RP_gaussian_mu") + "\n")
            params.write("RP_gaussian_std " + data.get("RP_gaussian_std") + "\n")
            params.write("Thresh_dynamic " + data.get("Thresh_dynamic") + "\n")
            params.write("Thresh_dynamic_init " + data.get("Thresh_dynamic_init") + "\n")
            # the following parameters are skipped in the GUI
            params.write("Intensity_distribution 2\n")
            params.write("Hetero_center_distr 2\n")
            params.write("Hetero_radius_distr 2\n")
            # useful for intensity distribution. Included for completeness --
            params.write("Hetero_center_mu 1.2\n")
            params.write("Hetero_center_std 0.14\n")
            params.write("Hetero_radius_mu 0.7\n")
            params.write("Hetero_radius_std 0.14\n")
            # --
            params.write("Gnuplot_plots 0\n")
            params.write("Animate_thresh 0\n")
            params.write("Animate_stepwise 0\n")
            params.write("Print_step 1\n")
    except IOError:
        return "Unable to write to params file."
    return ""


# This method is responsible for writing task and swarm parameters to the params
# file. This method assumes that the given data has been validated.
def write_params(task_data, swarm_data):
    error = setup_tasks(task_data)
    if error != "":
        return error + "\n" + setup_swarm(swarm_data)
    else:
        return setup_swarm(swarm_data)


# This method is called when the persistent layer wants to set up a new test.
def setup_test(name):
    error = testAccess.create_test(name)
    return error


# This method is called to clean up after a test is finished running
def finish_test(name):
    # move the data from Sim/Output to the directory created for this test
    error = testAccess.move_test(name)
    return error


def run():
    line1, line2, line3 = "", "", ""
    if sys.platform == 'win32' or sys.platform == 'cygwin':
        cmd = [os.path.normpath(os.getcwd() + "/Sim/sim.exe"), "params", "opfiles"]
    else:
        cmd = [os.path.normpath(os.getcwd() + "/Sim/sim"), "params", "opfiles"]
    process = subprocess.Popen(args=cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,
                               cwd=os.path.normpath(os.getcwd() + "/Sim"))
    for stdout_line in iter(process.stdout.readline, ""):
        line3 = line2
        line2 = line1
        line1 = stdout_line
        yield stdout_line
    process.stdout.close()
    return_code = process.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd, output=line3)
