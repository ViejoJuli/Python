from __future__ import print_function
from ortools.linear_solver import pywraplp
from ortools.init import pywrapinit
def main():
    solver= pywraplp.Solver('simple_mip_program',
                            pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    #Big M
    infinity = solver.infinity()
    #Create Variables
    x1 = solver.IntVar(0.0,1.0,"x1")
    x2 = solver.IntVar(0.0,1.0,"x2")
    x3 = solver.IntVar(0.0,1.0,"x3")
    x4 = solver.IntVar(0.0,1.0,"x4")
    x5 = solver.IntVar(0.0,1.0,"x5")
    print('Numero de variables=',solver.NumVariables())

    #Restrictions
    solver.Add(6*x1 + 6*x2 + 3*x3 + 2*x4 + 2*x5 <= 10)
    print('Numero de restricciones=', solver.NumConstraints())

    #Objective Function
    solver.Maximize(6*x1 + 6*x2 + 6*x3 + 10*x4 + 10*x5)

    #Call Solver
    status = solver.Solve()

    #Solution
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("OF Value=",solver.Objective().Value())
        print('x1 =',x1.solution_value())
        print('x2 =',x2.solution_value())
        print('x3 =',x3.solution_value())
        print('x4 =',x4.solution_value())
        print('x5 =',x5.solution_value())
    else:
        print('Moden has not optimal solution')

    #Additional Info
    print('\nAdditional Info')
    print('Problem solved in %f miliseconds'%solver.wall_time())
    print('Problem solved in %d iterations'%solver.iterations())
    print('Problem solved in %d nodes of BB'% solver.nodes())

if __name__ == '__main__':
    main()
