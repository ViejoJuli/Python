from __future__ import print_function
from ortools.linear_solver import pywraplp
from ortools.init import pywrapinit

def create_model_data():
    data={}#Dictionary
    data['restrictions_coefficients']=[
        [1, 0],
        [0, 2],
        [3, 2],
    ] #A_Matrix
    data['boundaries'] = [4, 12, 18]#b_vector
    data['OF_coefficients'] = [3, 5]
    data['num_variables'] = 2
    data['num_restrictions'] = 3
    return data
def main():
    data=create_model_data()
    solver= pywraplp.Solver('simple_mip_program',
                            pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    #Big M
    infinity = solver.infinity()
    #Create Variables
    x={}
    for j in range(data['num_variables']):
        x[j] = solver.IntVar(0,infinity,'x[%d]'% j)
    print('Number of Vriables loaded =',solver.NumVariables())

    #Create Restrictions
    for i in range(data['num_restrictions']):
        constraint= solver.RowConstraint(0,data['boundaries'][i],'')
        for j in range(data['num_variables']):
            constraint.SetCoefficient(x[j],data['restrictions_coefficients'][i][j]) #Its organized firts by restrictions and later by variable
    print('Number of restrictions',solver.NumConstraints())
    
    #OF
    objectiveFunction=solver.Objective()
    for j in range(data['num_variables']):
        objectiveFunction.SetCoefficient(x[j],data['OF_coefficients'][j])
    objectiveFunction.SetMaximization()

    #Call Solver
    status = solver.Solve()

    #Solution
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("OF Value=",solver.Objective().Value())
        for j in range(data['num_variables']):
            print(x[j].name(),'=',x[j].solution_value())
        #Additional Info
        print('\nAdditional Info')
        print('Problem solved in %f miliseconds'%solver.wall_time())
        print('Problem solved in %d iterations'%solver.iterations())
        print('Problem solved in %d nodes of BB'% solver.nodes())
    else:
        print('Moden has not optimal solution')

    

if __name__ == '__main__':
    main()


