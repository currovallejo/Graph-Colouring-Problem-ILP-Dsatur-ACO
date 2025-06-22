# GRAPH COLOURING PROBLEM

This repository contains my solution to the **Graph Colouring Problem**, developed as part of a selection process.

## Problem Description

As every summer approaches, the students of Hill-climber Valley High School excitedly prepare for their graduation dance. With the prestigious titles of prom king and queen at stake, one thing is clear: showing up in the same colour outfit as a direct rival is a critical mistake—one that has already sparked heated arguments in the hallways.

To prevent things from escalating, Mr. Hamilton, the senior year coordinator, has asked for your help. Your mission: assign each student a dress colour for the event, ensuring that no two rival students wear the same colour—all while using the minimum number of colours possible.

You will be provided with a list of student pairs who are direct rivals. Some students—naturally, the most popular—may have more than one rival. Your task is not to take sides, but to avoid conflict entirely.

Can you maintain peace at Hill-climber Valley High School… at least until the crowning moment?

### Formal Definition

This is a classical **Graph Colouring Problem**, where:
- Each student is represented as a **node** in a graph.
- Rivalries between students are represented as **edges** between nodes.
- The goal is to assign a **colour** to each node such that no two connected nodes share the same colour.
- The objective is to **minimize the total number of colours used**—the chromatic number of the graph.

## Contents

The repository includes:

- **Technical Report**: A brief report written as if addressed to a tech lead (in Spanish).
- **Executive Summary**: A short, high-level summary as if addressed to a client (in Spanish).
- **Source Code**: All code used to model, solve, and benchmark the problem. Specifically:
  - [ACO.py](ACO.py): Implements the Ant Colony Optimization (ACO) metaheuristic.
  - [dataLoader.py](dataLoader.py): Loads graph data from instance files located in the `data` folder.
  - [decorators.py](decorators.py): Contains utility decorators, such as a timing decorator used to measure computation time during benchmarking.
  - [dsatur.py](dsatur.py): Implements the DSATUR heuristic for graph colouring.
  - [graph.py](graph.py): Models the graph data structure and associated operations.
  - [ilp.py](ilp.py): Formulates the Graph Colouring Problem as an Integer Linear Program (ILP). Includes a warm start using the DSATUR heuristic.
  - [benchmarking.py](benchmarking.py): Script to compare the performance of ACO, DSATUR, and ILP methods.
  - [main.py](main.py): Entry point to run and compare different algorithms manually. You can change the input file and algorithm parameters directly in the function calls within this script.
  - [plot.py](plot.py): Generates a visualization or GIF of the coloured graph, showing all nodes and their connections using distinct colours.

## Data

The graph instances used in this project were obtained from the **Discrete Optimization** course, freely available on **Coursera**, taught by Professor **Pascal Van Hentenryck** from the **University of Melbourne**.
