import math

def bottomup(weights, values, limit):
    '''
    Builds the bottom-up (non-recursive) dynamic programming solution table to the 0-1 knapsack problem
    Objective:  maximize stored value
    Constraint:     weight capacity
    Reqs:   import math
    Inputs: 
        -list of item weights (num): [3.8, 7, 24.1, ...]
            -note that these will be converted to ceiling integers
        -list of item values (num): [0, 1.4, 2.1, 3, ...]
        -limit: (num)
            -will be converted to floor integer
        # TODO feature addition for later, not needed for MVS
        #   Resolution (num): divisions of weight, 1, 0.1, 0.01, etc. to specify precision of solution
    Output:
        returns mixed tuple (value(num), item list[1, 3, ...])
        '''
    
    # Sanitize and prepare inputs for operations:
    n = len(values)
    weights = [math.ceil(i) for i in weights]
    limit = math.floor(limit)
    SVT = [[-1 for i in range(limit+1)] for j in range(n+1)]

    # Do the darn thing:
    for item in range(n+1):
        for capacity in range(limit+1):
            if item == 0 or capacity == 0:
                SVT[item][capacity] = 0
            elif weights[item-1] <= capacity:
                SVT[item][capacity] = max( 
                    SVT[item-1][capacity], 
                    SVT[item-1][capacity-weights[item-1]]+values[item-1] 
                    )
            else:
                SVT[item][capacity] = SVT[item-1][capacity]
    print(SVT)
    return SVT[-1][-1]

def bottomup2(weights, values, limit, resolution):
    '''
    Builds the bottom-up (non-recursive) dynamic programming solution table to the 0-1 knapsack problem
    Objective:  maximize stored value
    Constraint:     weight capacity
    Reqs:   import math
    Inputs: 
        -list of item weights (num): [3.8, 7, 24.1, ...]
            -note that these will be converted to ceiling integers
        -list of item values (num): [0, 1.4, 2.1, 3, ...]
        -limit: (num)
            -will be converted to floor integer
        # TODO feature addition for later, not needed for MVS
        #   Resolution (num): divisions of weight, 1, 0.1, 0.01, etc. to specify precision of solution
    Output:
        returns mixed tuple (value(num), item list[1, 3, ...])
        '''
    
    # Sanitize and prepare inputs for operations:
    n = len(values)
    weights = [math.ceil(i) for i in weights]
    limit = math.floor(limit)
    SVT = [[-1 for i in range(limit+1)] for j in range(n+1)]

    # Do the darn thing:
    for item in range(n+1):
        for capacity in range(limit+1):
            if item == 0 or capacity == 0:
                SVT[item][capacity] = 0
            elif weights[item-1] <= capacity:
                SVT[item][capacity] = max( 
                    SVT[item-1][capacity], 
                    SVT[item-1][capacity-weights[item-1]]+values[item-1] 
                    )
            else:
                SVT[item][capacity] = SVT[item-1][capacity]
    print(SVT)
    return SVT[-1][-1]



x = bottomup([3, 3, 2, 5], [6, 7, 8, 9], 5)
print(x)
x = bottomup([5,3,4,2], [60,50,70,30], 5)
print(x)
x = bottomup([5.1,3.7,4,2.1], [60.1,50.2,70.5,30.8], 6.0)
print(x)


