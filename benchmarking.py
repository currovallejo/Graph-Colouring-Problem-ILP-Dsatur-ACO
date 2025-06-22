import time
import os

import pyomo.environ as pyo

import ilp
import dsatur
import ACO
import dataloader


def bm_solve_ilp(my_instance):
    colors = list(range(len(my_instance["nodes"])))
    my_model = ilp.build_ilp(my_instance["nodes"], colors, my_instance["edges"])
    solver = pyo.SolverFactory("glpk")
    solver.options["tmlim"] = 180
    start = time.time()
    res = solver.solve(my_model, tee=False)  # tee=True to print solver output
    end = time.time()
    elapsed_time = end - start
    res_condition = res.solver.termination_condition
    if res_condition == "maxTimeLimit":
        return elapsed_time, '-', res_condition
    else:
        y_values = my_model.y.get_values()
        cost = sum(y_values.values())

    return elapsed_time, cost, res_condition


def bm_solve_dsatur(my_instance):
    heu = dsatur.DSatur(my_instance["nodes"], my_instance["edges"])
    start = time.time()
    heu.solve()
    end = time.time()
    elapsed_time = end - start
    cost = heu.cost

    return elapsed_time, cost


def bm_solve_ACO(filename):
    g = ACO.create_graph(filename)
    start = time.time()
    final_costs, final_solution, iterations_needed = ACO.solve(
        g, num_ants=10, iter=10, a=1, b=3, decay=0.8
    )
    end = time.time()
    elapsed_time = end - start
    cost = final_costs

    return elapsed_time, cost


def main():
    data_folder = os.path.join(os.path.dirname(__file__), "data")
    files = sorted(
        os.listdir(data_folder),
        key=lambda x: int(x.split('_')[1])
    )
    ilp_flag = True
    ACO_flag = True
    # with open("benchmark_results.csv", "w") as f:
    #     f.write("file,ilp_elapsed_time,ilp_cost,ilp_termination_condition,dsatur_elapsed_time,dsatur_cost,ACO_elapsed_time,ACO_cost\n")

    start_index = files.index("gc_50_3")
    for file in files[start_index:]:
        print(f"Loading data from file {file}")
        my_instance = dataloader.load_instance(file)

        if ilp_flag:
            print(f"Solving {file} with ILP")
            ilp_elapsed_time, ilp_cost, res_condition = bm_solve_ilp(my_instance)
            if res_condition == 'maxTimeLimit':
                ilp_flag = False
        else:
            ilp_elapsed_time, ilp_cost, res_condition = '-', '-', '-'

        print(f"Solving {file} with DSatur")
        dsatur_elapsed_time, dsatur_cost = bm_solve_dsatur(my_instance)

        if ACO_flag:
            print(f"Solving {file} with ACO")
            ACO_elapsed_time, ACO_cost = bm_solve_ACO(file)
            if ACO_elapsed_time > 180:
                ACO_flag = False
        else:
            ACO_elapsed_time, ACO_cost = '-', '-'

        with open("benchmark_results.csv", "a") as f:
            f.write(
                f"{file},{ilp_elapsed_time},{ilp_cost},{res_condition},{dsatur_elapsed_time},{dsatur_cost},{ACO_elapsed_time},{ACO_cost}\n"
            )


if __name__ == "__main__":
    main()
