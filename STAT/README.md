# STAT: Swarm Testing and Analysis Tool

STAT is a tool built on top of a swarm simulation that facilitates the creation and execution of swarm simulations.

## Description
STAT is a tool built on top of the k-task swarm simulation. The goal of STAT is to enhance the testing experience by expanding upon the functionality provided by k-task, and allow for a user-friendly way of generating a swarm test. STAT builds on the previous version of k-task by allowing custom tasks to be defined along with task links. This allows a tester to model tasks that are representative of the real world, along with reintroducing the task dependencies seen in the dimensional simulations. STAT allows for testing of various swarm configurations in an environment that is understandable and organized. Furthermore, STAT provides parameter checking so that the generated swarms are without error and understood by the user. All of these features enhance k-task to provide a testing platform which improves the understanding of the user and expands their swarm generating capabilities.

## Dependencies
This project requires a machine with a C compiler and Python version 3.0 or newer.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyplot and Pillow.

```bash
pip install pyplot pillow
```

## Usage
The k-task simulation will need to be compiled before running. Use the provided makefile in the src/Sim directory to build the simulation.

Run the following command in the src directory.

```bash
python main.py
```

## Roadmap
The following list contains suggested improvements to the STAT program. This list is provided in no particular order.
* Demand preview page to display task demand graphs before executing the k-task simulation.
* Add a help page.
* Allow the user to interact with the graphs produced for a test.
* Integrate the genetic algorithm program into STAT so that a user can train for weights after deciding on other swarm and task parameters.

## Authors and acknowledgment
STAT was written by John Cornwell with the support of Dr. David Mathias.
