"""
Date: 09-11-2024
Author: Francisco M Vallejo
Description: Master file to run the different algorithms and compare them manually,
    changing the input file in the main function and the parameters of the algorithms in
    the function calls.
"""

import ilp
import dsatur
import ACO
import dataLoader
import pyomo.environ as pyo
from plot import draw_from_nodes
from matplotlib import pyplot as plt
import matplotlib.lines as mlines


# Solving with ILP
# In less than 2 minutes:
# optimal gc_20_1
# 20% GAP gc_20_3
# 25% GAP gc_50_1
def solve_ilp(my_instance):
    print("\nSolving with ILP")
    colors = list(range(len(my_instance["nodes"])))
    my_model = ilp.build_ilp(my_instance["nodes"], colors, my_instance["edges"])
    solver = pyo.SolverFactory("glpk")
    solver.options["tmlim"] = 10
    res = solver.solve(my_model, tee=True)  # tee=True to print solver output
    y_values = my_model.y.get_values()
    print("Cost obtained with the ILP model: ", sum(y_values.values()))


# Solving with DSatur
# In less than 25 seconds can solve all instances
# Solution quality is not guaranteed to be optimal neither close to optimal for big instances
def solve_dsatur(my_instance):
    print("\nSolving with DSatur")
    heu = dsatur.DSatur(my_instance["nodes"], my_instance["edges"])
    heu.solve(save_history=True)
    print("Cost obtained with the DSatur heuristic: ", heu.cost)
    # fig, ax = plt.subplots(figsize=[14, 10], dpi=100)
    # draw_from_nodes(
    #     heu.N,
    #     ax=ax,
    #     plot_margins=False,
    #     use_labels=0,
    #     edge_alpha=0.2,
    #     edge_color="#68555D",
    #     layout_iter=1000,
    #     seed=12,
    # )
    # # Custom legend items
    # node_legend = mlines.Line2D(
    #     [],
    #     [],
    #     color="C0",
    #     marker="o",
    #     linestyle="None",
    #     markersize=8,
    #     label="Puntos coloreados (nodos) = alumnos",
    # )
    # edge_legend = mlines.Line2D(
    #     [],
    #     [],
    #     color="#68555D",
    #     linestyle="-",
    #     linewidth=2,
    #     alpha=0.2,
    #     label="Dos puntos coloreados conectados por una línea (arco) indica que son rivales \n y por lo tanto no pueden tener el mismo color",
    # )

    # # Add legend to the plot
    # ax.legend(
    #     handles=[node_legend, edge_legend],
    #     fontsize=24,
    #     loc="upper center",
    #     bbox_to_anchor=(0.5, -0.05),
    #     ncol=1,
    # )
    # fig.tight_layout()
    # plt.show()


# Solving with ACO
# Better solutions than DSatur for instances up to 250 nodes
# Cannot solve instances with more than 250 nodes (in a reasonable time)
def solve_ACO(filename):
    print("\nSolving with ACO")
    g = ACO.create_graph(filename)
    final_costs, final_solution, iterations_needed = ACO.solve(
        g, num_ants=10, iter=10, a=1, b=3, decay=0.8
    )
    print("Cost obtained with ACO: ", final_costs)


def main():
    filename = "gc_50_5"
    # Load data
    my_instance = dataLoader.load_instance(filename)
    # # Solve with ILP
    solve_ilp(my_instance)
    # Solve with DSatur
    solve_dsatur(my_instance)
    # Solve with ACO
    solve_ACO(filename)


if __name__ == "__main__":
    main()
