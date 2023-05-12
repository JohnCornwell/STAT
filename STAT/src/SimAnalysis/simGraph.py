# This module handles transforming data from a test directory into graphs.

import gc
import os
import sys
import subprocess
import matplotlib
import matplotlib.pyplot as plt
from os.path import normpath
from Storage import testAccess

resolution = 800
# This line is necessary because pyplots are created on a worker thread. This
# disables a tkinter window from being created which will crash the program.
# If you plan on making an interactive graph, you must ensure the worker thread
# graphs are created without spawning a hidden gui.
matplotlib.use('agg')


# -- Functions to graph all plots and store them as .png -- #

# helper function that graphs demand and action data
def graph_demand(test_name, demand_data, action_data):
    num_tasks = len(demand_data[0])  # can't rely on read num_tasks if data is incomplete
    timesteps = range(0, len(demand_data))

    plt.figure(0, figsize=(5, 4), dpi=resolution)  # shows demand of all tasks overlayed
    plt.title("All Tasks' Demand")
    plt.ylabel("Demand")
    plt.xlabel("Timestep")
    plt.figure(1, figsize=(5, 4), dpi=resolution)  # shows action of all tasks overlayed
    plt.title("All Tasks' Action")
    plt.ylabel("Action")
    plt.xlabel("Timestep")
    labels = list()
    for i in range(num_tasks):
        labels.append("Task {}".format(i))
        plt.figure(i + 2, figsize=(5, 4), dpi=resolution)
        plt.subplot(1, 1, 1)  # one figure per task. One plot per figure
        plt.title("Task {} Demand".format(i))
        plt.ylabel("New Demand")
        plt.xlabel("Timestep")
        task_demand = list(x[i] for x in demand_data)
        plt.plot(timesteps, task_demand)
        task_action = list(x[i] for x in action_data)
        plt.figure(num_tasks + 2 + i, figsize=(5, 4), dpi=resolution)
        plt.title("Task {} Action".format(i))
        plt.ylabel("Action")
        plt.xlabel("Timestep")
        plt.plot(timesteps, task_action)
        plt.plot()
        plt.figure(0)
        plt.plot(timesteps, task_demand)
        plt.figure(1)
        plt.plot(timesteps, task_action)

    plt.figure(0)
    legend = right_legend(plt, labels)
    testAccess.save_graph(test_name, plt, "All_Demand.png", bbox_extra_artists=(legend,), bbox_inches='tight')
    plt.close()
    plt.figure(1)
    legend = right_legend(plt, labels)
    testAccess.save_graph(test_name, plt, "All_Action.png", bbox_extra_artists=(legend,), bbox_inches='tight')
    plt.close()
    for i in range(2, num_tasks + 2):
        plt.figure(i)
        testAccess.save_graph(test_name, plt, "Task_{}_Demand.png".format(i - 2))
        plt.close(i)
    for i in range(num_tasks + 2, 2 * num_tasks + 2):
        plt.figure(i)
        testAccess.save_graph(test_name, plt, "Task_{}_Action.png".format(i - 2 - num_tasks))
        plt.close(i)

    for i in range(num_tasks):
        task_demand = list(x[i] for x in demand_data)
        task_action = list(x[i] for x in action_data)
        # plot new task demand vs agent action
        plt.figure(i, dpi=resolution)
        plt.subplot(1, 1, 1)
        plt.title("Task {} Demand v Delivered".format(i))
        plt.ylabel("New Demand/Action")
        plt.xlabel("Timestep")
        plt.plot(timesteps, task_demand, "b", linewidth=0.7)
        plt.plot(timesteps, task_action, "r", linewidth=0.4)

    for i in range(num_tasks):
        plt.figure(i)
        legend = right_legend(plt, ["New Demand", "Action"])
        testAccess.save_graph(test_name, plt, "Task_{}_Demand_v_Delivered.png".format(i),
                              bbox_extra_artists=(legend,), bbox_inches='tight')
        plt.close(i)


# Function to graph data from the .stepsummary file
def graph_summary(test_name, push_data, rest_data, task_switches, percent_actor_switches,
                  percent_all_switches):
    num_tasks = len(push_data[0])
    timesteps = range(0, len(push_data))

    # graph the pushes per task
    for i in range(num_tasks):
        plt.figure(i, figsize=(5, 4), dpi=resolution)
        plt.subplot(1, 1, 1)  # one figure per task. One plot per figure
        plt.title("Task {} Pushes".format(i))
        plt.ylabel("Number of Agents")
        plt.xlabel("Timestep")
        task_agents = list(x[i] for x in push_data)
        plt.plot(timesteps, task_agents, '.')

    for i in range(num_tasks):
        plt.figure(i)
        testAccess.save_graph(test_name, plt, "Task_{}_Pushes.png".format(i))
        plt.close(i)

    # graph single plots for the rest of the data

    # push data contains a list of task pushes for each timestep
    all_push = list(range(0, len(push_data)))
    for i in range(0, len(push_data)):
        # sum of agents pushing every timestep
        all_push[i] = sum(push_data[i])
    plt.figure(0, figsize=(5, 4), dpi=resolution)
    plt.subplot(1, 1, 1)
    plt.title("Agents Pushing")
    plt.ylabel("Number of Agents")
    plt.xlabel("Timestep")
    plt.plot(timesteps, all_push, '.')
    testAccess.save_graph(test_name, plt, "Agents_Pushing.png")
    plt.close(0)

    plt.figure(0, figsize=(5, 4), dpi=resolution)
    plt.subplot(1, 1, 1)
    plt.title("Agents Resting")
    plt.ylabel("Number of Agents")
    plt.xlabel("Timestep")
    plt.plot(timesteps, rest_data, '.')
    testAccess.save_graph(test_name, plt, "Agents_Resting.png")
    plt.close(0)

    plt.figure(0, figsize=(5, 4), dpi=resolution)
    plt.subplot(1, 1, 1)
    plt.title("Task Switches")
    plt.ylabel("Number of Switches")
    plt.xlabel("Timestep")
    plt.plot(timesteps, task_switches, '.')
    testAccess.save_graph(test_name, plt, "Task_Switches.png")
    plt.close(0)

    plt.figure(0, figsize=(5, 4), dpi=resolution)
    plt.subplot(1, 1, 1)
    plt.title("Percent Actor Switches")
    plt.ylabel("Percent of Active Agents")
    plt.xlabel("Timestep")
    plt.plot(timesteps, percent_actor_switches, '.')
    testAccess.save_graph(test_name, plt, "Percent_Actor_Switches.png")
    plt.close(0)

    plt.figure(0, figsize=(5, 4), dpi=resolution)
    plt.subplot(1, 1, 1)
    plt.title("Percent All Switches")
    plt.ylabel("Percent of All Agents")
    plt.xlabel("Timestep")
    plt.plot(timesteps, percent_all_switches, '.')
    testAccess.save_graph(test_name, plt, "Percent_All_Switches.png")
    plt.close(0)


def graph_accuracy(test_name, accuracy_data, swarm_performance):
    num_tasks = len(accuracy_data[0])
    timesteps = range(0, len(accuracy_data))

    # graph the accuracy of every task
    for i in range(num_tasks):
        plt.figure(i, figsize=(5, 4), dpi=resolution)
        plt.subplot(1, 1, 1)  # one figure per task. One plot per figure
        plt.title("Task {} Accuracy".format(i))
        plt.ylabel("Current Accuracy (Lower is Better)")
        plt.xlabel("Timestep")
        task_accuracy = list(x[i] for x in accuracy_data)
        plt.plot(timesteps, task_accuracy)

    for i in range(num_tasks):
        plt.figure(i)
        testAccess.save_graph(test_name, plt, "Task_{}_Accuracy.png".format(i))
        plt.close(i)

    # graph swarm performance (average task accuracy)
    plt.figure(0, figsize=(5, 4), dpi=resolution)
    plt.subplot(1, 1, 1)
    plt.title("Swarm Performance")
    plt.ylabel("Current Performance (Lower is Better)")
    plt.xlabel("Timestep")
    plt.plot(range(0, len(swarm_performance)), swarm_performance)
    testAccess.save_graph(test_name, plt, "Swarm_Performance.png")
    plt.close(0)


# This method should be called by the gui after the test has concluded.
# This method will produce demand graph output for the supplied test name.
# This method requires that a user is logged in and the given test exists
# in that user's directory
def generate_demand(test_name):
    # collect our data from files
    error, demand, action = testAccess.read_demand(test_name)
    if error != "":
        print(error)
    else:
        graph_demand(test_name, demand, action)
    # clear data to avoid large memory footprint
    del demand
    del action
    gc.collect()
    return error


# This method should be called by the gui after the test has concluded.
# This method will produce summary graph output for the supplied test name.
# This method requires that a user is logged in and the given test exists
# in that user's directory
def generate_summary(test_name):
    # collect our data from files
    error, push_data, rest_data, task_switches, percent_actor_switches, percent_all_switches = \
        testAccess.read_summary(test_name)
    if error != "":
        print(error)
    else:
        graph_summary(test_name, push_data, rest_data, task_switches, percent_actor_switches, percent_all_switches)
    del push_data
    del rest_data
    del task_switches
    del percent_actor_switches
    del percent_all_switches
    gc.collect()
    return error


# This method should be called by the gui after the test has concluded.
# This method will produce performance graph output for the supplied test name.
# This method requires that a user is logged in and the given test exists
# in that user's directory
def generate_accuracy(test_name):
    # collect our data from files
    error, accuracy, performance = testAccess.read_accuracy(test_name)
    if error != "":
        print(error)
    else:
        graph_accuracy(test_name, accuracy, performance)
    del accuracy
    del performance
    gc.collect()
    return error


# -- Functions to retrieve a graph -- #

# This function retrieves a graph for the given test and graph name
def open_graph(test_name, graph_name):
    test_dir = testAccess.find_test(test_name)
    if testAccess.file_exists(normpath(test_dir + "/" + graph_name)):
        if sys.platform == "win32" or sys.platform == "cygwin":
            os.startfile(normpath(test_dir + "/" + graph_name))
        elif sys.platform == "darwin":
            subprocess.call("open", normpath(test_dir + "/" + graph_name))
        else:
            subprocess.call(["xdg-open", normpath(test_dir + "/" + graph_name)])
        return ""
    return "Could not find the {} graph.".format(graph_name)


# -- Functions to place a legend in a plot -- #

# Place the graph legend to the right outside the graph. This method assumes the
# legend has already been given labels.
def right_legend(plot, labels):
    # Place a legend to the right of this plot.
    return plot.legend(labels=labels, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
