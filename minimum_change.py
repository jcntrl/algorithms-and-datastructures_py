def minchange_rec(AC, TV): #working as intended
    """
    # Determines minimum number of coins to make TargetValue from AvailableCoins
    ## Non-optimized recursive solution. THIS WILL BE SLOW.
    Input: (int) list of AvailableCoins \n
    ### Note: 1 is always included in AvailableCoins
    Input: (int) TargetValue \n
    Output: (int) minimum number of coins to solve \n
    """

    result = TV #worst case scenario, provides upper bound to improve against
    if TV == 0: #basecase, when TV==0, stop this recursion
        return 0

    # now iterate over list of coins, qualify coin, 
    #   recurse to generate depth solution
    #       and compare to incumbent result and accept if better
    for coin in AC:
        if coin <= TV:
            tmp = 1 + minchange_rec(AC, TV-coin) #take current coin and recurse
            if tmp < result:
                result = tmp
            
    return result
        

def test(algo, tests, expected):
    """
    input/select which algo to test: recursive, topdown, bottomup
    input a list of integers to test, input a list of expected results
    returns nothing, prints results of test to console
    """
    # add a selector? how?

    for i in range(len(tests)):
        try:
            test = minchange_rec(AC, tests[i])
            assert test == expected[i]
            print('PASS', tests[i], '==>', test, 'should be:', expected[i])
        except:
            print('FAIL', tests[i], '==>', test, 'should be:', expected[i])




# test(
#     [0, 1, 4, 5, 6, 9, 10, 11, 14, 15, 16, 19, 20, 21, 24, 25, 26, 29, 30, 31, 49, 50, 51, 99, 100, 101],
#     [0, 1, 4, 1, 2, 5, 1,  2,  5,  2,  3,  6,  2,  3,  6,  1,  2,  5,  2,  3,  7,  1,  2,  8,  1,   2]
# )




AC=(100, 50, 25, 10, 5, 1)  #available coin denominations
TV = 21  #target value should be 4
print("\noverall function return: ", minchange_rec(AC, TV))


