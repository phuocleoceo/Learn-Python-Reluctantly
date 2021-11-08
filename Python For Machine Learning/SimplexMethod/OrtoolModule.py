from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')


def InitVariable(n):
    x = []
    x.append(0)
    for i in range(1, n+1):
        x.append(solver.NumVar(0, solver.infinity(), 'x'+str(i)))
    return x


def LinearProgramming(n, x, constraints, objectives, option="Minimize"):
    for c in constraints:
        solver.Add(c)

    if option == "Minimize":
        solver.Minimize(objectives)
    elif option == "Maximize":
        solver.Maximize(objectives)

    # print("Number of variables =", solver.NumVariables())
    # print("Number of constraints =", solver.NumConstraints())

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("Objective value =", solver.Objective().Value())
        for i in range(1, n+1):
            print("x"+str(i), x[i].solution_value())
    else:
        print('The problem does not have an optimal solution.')

    # print("\nAdvanced usage:")
    # print("Problem solved in %f milliseconds" % solver.wall_time())
    # print("Problem solved in %d iterations" % solver.iterations())


##############################################################################

# n = 6
# x = InitVariable(n)

# constraints = []
# constraints.append(x[1]+x[4]+x[5]-x[6] == 2)
# constraints.append(x[2]+x[4]+x[6] == 12)
# constraints.append(x[3]+2*x[4]+4*x[5]+3*x[6] == 9)

# objectives = x[1]-x[2]-2*x[4]+2*x[5]-2*x[6]
# LinearProgramming(n, x, constraints, objectives, "Minimize")
# # LinearProgramming(n, x, constraints, objectives, "Maximize")

n = 6
x = InitVariable(n)

constraints = []
constraints.append(x[1]+x[2]-x[3]+x[5] == 7)
constraints.append(-4*x[2]+4*x[3]+x[4] == 12)
constraints.append(-5*x[2]+3*x[3]+x[5]+x[6] == 10)

objectives = x[2]-3*x[3]+2*x[5]
LinearProgramming(n, x, constraints, objectives, "Minimize")
#LinearProgramming(n, x, constraints, objectives, "Maximize")
