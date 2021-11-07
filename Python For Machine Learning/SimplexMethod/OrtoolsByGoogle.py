from ortools.linear_solver import pywraplp


def LinearProgrammingExample():
    solver = pywraplp.Solver.CreateSolver('GLOP')

    x1 = solver.NumVar(0, solver.infinity(), 'x1')
    x2 = solver.NumVar(0, solver.infinity(), 'x2')
    x3 = solver.NumVar(0, solver.infinity(), 'x3')
    x4 = solver.NumVar(0, solver.infinity(), 'x4')
    x5 = solver.NumVar(0, solver.infinity(), 'x5')
    x6 = solver.NumVar(0, solver.infinity(), 'x6')

    print('Number of variables =', solver.NumVariables())

    solver.Add(x1+x4+x5-x6 == 2)
    solver.Add(x2+x4+x6 == 12)
    solver.Add(x3+2*x4+4*x5+3*x6 == 9)

    print('Number of constraints =', solver.NumConstraints())

    solver.Minimize(x1-x2-2*x4+2*x5-2*x6)

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('x1 =', x1.solution_value())
        print('x2 =', x2.solution_value())
        print('x3 =', x3.solution_value())
        print('x4 =', x4.solution_value())
        print('x5 =', x5.solution_value())
        print('x6 =', x6.solution_value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())


LinearProgrammingExample()
