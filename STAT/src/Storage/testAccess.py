import os
import shutil
from os.path import normpath as normpath
import datetime
from util import cut
from Storage import directoryAccess


# This method returns the path of a given test name for the logged in user or the empty string
def find_test(name):
    if os.path.exists(normpath(directoryAccess.get_user() + "/" + name)):
        return normpath(directoryAccess.get_user() + "/" + name)
    else:
        return ""


# Create a directory for a test before running sim. This method returns an error if the
# test directory cannot be created.
def create_test(name):
    if os.path.exists(normpath(directoryAccess.get_user() + "/" + name)):
        return "This test name already exists."
    else:
        try:
            os.mkdir(normpath(directoryAccess.get_user() + "/" + name))
        except OSError:
            # need to do a full or partial move of remaining test files
            return "Unable to create test directory."
    return ""


# Move test files after sim has successfully executed. This method assumes
# that the requested test name is legal for the filesystem.
def move_test(name):
    # This is a redundant check that should not be false
    if os.path.exists(normpath(directoryAccess.get_user())):
        if os.path.exists(normpath(directoryAccess.get_user() + "/" + name)):
            try:
                num = open("Sim/run.num")
                run = num.read().strip(" \t\n")
                num.close()
                for file in os.listdir(normpath(directoryAccess.get_home() + "/Sim/Output/run." + run)):
                    # we are not using relative dirs, so we don't need dir_fds
                    os.replace(normpath(directoryAccess.get_home() + "/Sim/Output/run." + run + "/" + file),
                               normpath(directoryAccess.get_user() + "/" + name + "/" + file))
                return ""
            except OSError:
                # need to do a full or partial move of remaining test files
                return "Unable to move all files.\n" + recover_test(name)
        else:
            # If we cannot move the test to our user's dir, recover with the same name
            return "Unable to locate test " + name + " to move files into.\n" + recover_test(name)
    else:
        return "Unable to find user directory.\n" + recover_test(name)


# When a test cannot be placed in a user's directory, it must move to recovery.
# This method will return a message containing the recovery directory that the files
# were moved to, or a description of the error encountered. This method assumes that the
# requested test name is legal for the filesystem.
def recover_test(requested_name):
    # recoveryDir is the name given to our test by sim
    # destinationDir is the final destination of our test
    # find the highest numbered test in Output
    recoveryDir = None
    # we can alternatively consider using the run.num file, however, accessing that
    # file could have caused an error that led us here
    try:
        for test in os.listdir(normpath(directoryAccess.get_home() + "/Sim/Output")):
            if os.path.isdir(normpath(directoryAccess.get_home() + "/Sim/Output/" + test)):
                try:
                    # get run number from path/run."runnum"
                    # slices out of bounds produce an empty string
                    if recoveryDir is None or int(recoveryDir[4:]) < int(test[4:]):
                        recoveryDir = test
                except ValueError:
                    pass
    except FileNotFoundError:
        return "Sim Output directory is missing."
    if recoveryDir is None:
        return "Could not find a test to recover."
    # create test directory in Recovery
    if os.path.exists(normpath(directoryAccess.get_recovery() + "/" + requested_name)):
        try:
            # duplicate name, so use the current datetime for a (hopefully) unique test name
            destination = normpath(directoryAccess.get_recovery() + "/" +
                                   datetime.datetime.now().isoformat(timespec='seconds'))
            os.mkdir(destination)
        except OSError:
            return "Unable to create recovery directory after encountering duplicate test name."
    else:
        # the requested name of the test is available in the recovery dir
        try:
            destination = normpath(directoryAccess.get_recovery() + "/" + requested_name)
            os.mkdir(destination)
        except OSError:
            return "Unable to create a recovery directory."
    # move files into destination directory
    try:
        for file in os.listdir(recoveryDir):
            os.replace(normpath(recoveryDir + "/" + file), normpath(destination + "/" + file))
    except OSError:
        return "Could not copy all test data to recovery directory."
    return "Files have been moved to " + destination


def load_test(test):
    params = ""
    values = {}
    try:
        for file in os.listdir(normpath(directoryAccess.get_user() + "/" + test)):
            if file.endswith("params"):
                params = normpath(directoryAccess.get_user() + "/" + test + "/" + file)
                break
    except OSError:
        return "Could not find test params file.", values
    try:
        with open(params, "r") as paramsFile:
            for line in paramsFile:
                process_line(line, values)
    except OSError:
        return "Could not read from the test params file.", values
    return "", values


# Method to take a line and a dictionary. If there is a relevant assignment,
# this method will record the assignment in the given dictionary. This method 
# will strip trailing zeroes from values
def process_line(line, values):
    if "#" in line:
        pass
    elif "Num_tasks" in line:
        line = line.split("=")
        values["Num_tasks"] = cut(line[1].strip(" \t\n"))
    elif "Max_steps" in line:
        line = line.split("=")
        values["Max_steps"] = cut(line[1].strip(" \t\n"))
    elif "Target_path" in line:
        line = line.split("=")
        values["Target_path"] = line[1].strip(" \t\n")
    elif "Functions" in line:
        line = line.split("=")
        values["Functions"] = line[1].strip(" \t\n")
    elif "Range" in line:
        line = line.split("=")
        result = ""
        for s in line[1].strip(" \t\n").split(","):
            result += cut(s.strip(" ")) + ","
        values["Range"] = result[0: len(result) - 1]
    elif "Target.amplitude" in line:
        line = line.split("=")
        result = ""
        for s in line[1].strip(" \t\n").split(","):
            result += cut(s.strip(" ")) + ","
        values["Path_amplitude"] = result[0: len(result) - 1]
    elif "Target.period" in line:
        line = line.split("=")
        result = ""
        for s in line[1].strip(" \t\n").split(","):
            result += cut(s.strip(" ")) + ","
        values["Path_period"] = result[0: len(result) - 1]
    elif "Pop_size" in line:
        line = line.split("=")
        values["Pop_size"] = cut(line[1].strip(" \t\n"))
    elif "Thresh_init" in line:
        line = line.split("=")
        values["Thresh_init"] = cut(line[1].strip(" \t\n"))
    elif "Thresh_increase" in line:
        line = line.split("=")
        values["Thresh_increase"] = cut(line[1].strip(" \t\n"))
    elif "Thresh_decrease" in line:
        line = line.split("=")
        values["Thresh_decrease"] = cut(line[1].strip(" \t\n"))
    elif "Prob_check" in line:
        line = line.split("=")
        values["Prob_check"] = cut(line[1].strip(" \t\n"))
    elif "Response_prob" in line:
        line = line.split("=")
        values["Response_prob"] = cut(line[1].strip(" \t\n"))
    elif "Task_selection" in line:
        line = line.split("=")
        values["Task_selection"] = cut(line[1].strip(" \t\n"))
    elif "Intensity_variation" in line:
        line = line.split("=")
        values["Intensity_variation"] = cut(line[1].strip(" \t\n"))
        if "0" in values["Intensity_variation"]:
            values["Intensity_aging"] = "0"
        else:
            values["Intensity_aging"] = "1"
    elif "Intensity_aging_max" in line:
        line = line.split("=")
        values["Intensity_aging_max"] = cut(line[1].strip(" \t\n"))
    elif "Intensity_aging_min" in line:
        line = line.split("=")
        values["Intensity_aging_min"] = cut(line[1].strip(" \t\n"))
    elif "Intensity_aging_up" in line:
        line = line.split("=")
        values["Intensity_aging_up"] = cut(line[1].strip(" \t\n"))
    elif "Intensity_aging_down" in line:
        line = line.split("=")
        values["Intensity_aging_down"] = cut(line[1].strip(" \t\n"))
    elif "Kill_number" in line:
        line = line.split("=")
        values["Kill_number"] = cut(line[1].strip(" \t\n"))
    elif "First_extinction" in line:
        line = line.split("=")
        values["First_extinction"] = cut(line[1].strip(" \t\n"))
    elif "Extinction_period" in line:
        line = line.split("=")
        values["Extinction_period"] = cut(line[1].strip(" \t\n"))
    elif "Spontaneous_response_prob" in line:
        line = line.split("=")
        values["Spontaneous_response_prob"] = cut(line[1].strip(" \t\n"))
    elif "Hetero_range_max" in line:
        line = line.split("=")
        values["Hetero_range_max"] = cut(line[1].strip(" \t\n"))
    elif "Hetero_range_min" in line:
        line = line.split("=")
        values["Hetero_range_min"] = cut(line[1].strip(" \t\n"))
    elif "Hetero_radius_max" in line:
        line = line.split("=")
        values["Hetero_radius_max"] = cut(line[1].strip(" \t\n"))
    elif "Hetero_radius_min" in line:
        line = line.split("=")
        values["Hetero_radius_min"] = cut(line[1].strip(" \t\n"))
    elif "RP_gaussian_mu" in line:
        line = line.split("=")
        values["RP_gaussian_mu"] = cut(line[1].strip(" \t\n"))
    elif "RP_gaussian_std" in line:
        line = line.split("=")
        values["RP_gaussian_std"] = cut(line[1].strip(" \t\n"))
    elif "Thresh_dynamic " in line:
        line = line.split("=")
        values["Thresh_dynamic"] = cut(line[1].strip(" \t\n"))
    elif "Thresh_dynamic_init" in line:
        line = line.split("=")
        values["Thresh_dynamic_init"] = cut(line[1].strip(" \t\n"))


def delete_test(name):
    name = normpath(directoryAccess.get_user() + "/" + name)
    try:
        shutil.rmtree(name)
    except OSError:
        return "Unable to delete test."
    return ""


def list_tests():
    if os.path.exists(normpath(directoryAccess.get_user())):
        return os.listdir(normpath(directoryAccess.get_user()))
    else:
        return "Unable to find user directory."


# This function will collect data from the .stepdemand file
def read_demand(test_name):
    file_name = find_demand(test_name)
    if file_name == "":
        return "Could not find test demand file.", [], []
    demand_data = []
    action_data = []

    try:
        with open(normpath(directoryAccess.get_user() + "/" + test_name + "/" + file_name)) as f:
            for line in f:
                tokens = line.split()
                line_demand = list()
                line_action = list()
                for i in range(4, len(tokens), 12):
                    line_demand.append(float(tokens[i]))
                    line_action.append(float(tokens[i + 3]))
                # first line has no data
                if len(line_demand):
                    demand_data.append(line_demand)
                if len(line_action):
                    action_data.append(line_action)
    except OSError:
        return "Could not read from test demand file.", [], []
    except ValueError:
        return "Encountered unexpected data in test demand file.", [], []
    return "", demand_data, action_data


# This function will collect data from the .stepsummary file
def read_summary(test_name):
    file_name = find_summary(test_name)
    if file_name == "":
        return "Could not find test summary file.", [], [], [], [], []
    task_push = []
    rest_data = []
    task_switches = []
    percent_actor_switches = []
    percent_all_switches = []

    try:
        with open(normpath(directoryAccess.get_user() + "/" + test_name + "/" + file_name)) as f:
            for line in f:
                tokens = line.split()
                line_push = list()
                for i in range(16, len(tokens), 18):
                    line_push.append(float(tokens[i]))
                # first line has no data
                if len(line_push) and line[1] != "-1":
                    task_push.append(line_push)
                    rest_data.append(float(tokens[-9]))
                    task_switches.append(float(tokens[-7]))
                    percent_actor_switches.append(float(tokens[-5]))
                    percent_all_switches.append(float(tokens[-3]))

    except OSError:
        return "Could not read from test summary file.", [], [], [], [], []
    except ValueError:
        return "Encountered unexpected data in test summary file.", [], [], [], [], []
    return "", task_push, rest_data, task_switches, percent_actor_switches, percent_all_switches


# This function will collect data from the .stepaccuracy file
def read_accuracy(test_name):
    file_name = find_accuracy(test_name)
    if file_name == "":
        return "Could not find test accuracy file.", [], []
    accuracy_data = []
    swarm_performance = []

    try:
        with open(normpath(directoryAccess.get_user() + "/" + test_name + "/" + file_name)) as f:
            for line in f:
                tokens = line.split()
                line_accuracy = list()
                for i in range(9, len(tokens), 8):
                    line_accuracy.append(float(tokens[i]))
                accuracy_data.append(line_accuracy)
                swarm_performance.append(float(tokens[len(tokens) - 1]))
    except OSError:
        return "Could not read from test accuracy file.", [], []
    except ValueError:
        return "Encountered unexpected data in test accuracy file.", [], []
    return "", accuracy_data, swarm_performance


def read_stats(test_name):
    data = {}
    file_name = find_stats(test_name)
    if file_name == "":
        return "Could not find test final stats file.", []

    try:
        with open(normpath(directoryAccess.get_user() + "/" + test_name + "/" + file_name)) as f:
            for line in f:
                tokens = line.split()
                if tokens[0] == "avg_accuracy":
                    data["avg_accuracy"] = float(tokens[1])
                elif tokens[0] == "switch":
                    data["switch_avg"] = float(tokens[2])
                    data["switch_max"] = float(tokens[4])
                    data["switch_min"] = float(tokens[6])
                    data["spontaneous_avg"] = float(tokens[9])
                    data["spontaneous_max"] = float(tokens[11])
                    data["spontaneous_min"] = float(tokens[13])
    except OSError:
        return "Could not read from test final stats file.", []
    except IndexError:
        return "Missing data in test final stats file.", []
    except ValueError:
        return "Encountered unexpected data in test final stats file.", []
    return "", data


def find_summary(test_name):
    for file in os.listdir(normpath(directoryAccess.get_user() + "/" + test_name)):
        if file.endswith(".stepsummary"):
            return file
    return ""


def find_demand(test_name):
    for file in os.listdir(normpath(directoryAccess.get_user() + "/" + test_name)):
        if file.endswith(".stepdemand"):
            return file
    return ""


def find_accuracy(test_name):
    for file in os.listdir(normpath(directoryAccess.get_user() + "/" + test_name)):
        if file.endswith(".stepaccuracy"):
            return file
    return ""


def find_stats(test_name):
    for file in os.listdir(normpath(directoryAccess.get_user() + "/" + test_name)):
        if file.endswith(".finalstats"):
            return file
    return ""


def file_exists(file):
    return os.path.exists(file)


def save_graph(testname, fig, filename, **kwargs):
    fig.savefig(fname=normpath(find_test(testname) + "/" + filename), **kwargs)
