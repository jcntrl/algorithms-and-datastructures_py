import time


def minchange_rec(AC, TV): #working as intended
    """
    # Determines minimum number of coins to make TargetValue from AvailableCoins
    ## Non-optimized recursive solution. THIS WILL BE SLOW.
    ## ~8s to converge on solution for TV = 54. TV > 54... too slow to be patient for.
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

def minchange_TD(AC, TV, memo={}):
    """
    # Determines minimum number of coins to make TargetValue from AvailableCoins
    ## Top-down dynamic programming recursive solution. THIS WILL BE FASTER THAN SLOW.
    ## Much faster than non-optimized recursive; ~7ms to converge on solution for TV=54.
    Input: (int) list of AvailableCoins \n
    ### Note: 1 is always included in AvailableCoins
    Input: (int) TargetValue \n
    Output: (int) minimum number of coins to solve \n
    """

    result = TV #worst case scenario, provides upper bound to improve against
    if TV == 0: #basecase, when TV==0, stop this recursion
        return 0

    # now iterate over list of coins, qualify coin, 
    #  return if solution in memo, else recurse to generate depth solution and store in memo
    #       and compare to incumbent result and accept if better
    for coin in AC:
        if coin <= TV:
            if TV in memo:
                return memo[TV]
            else:
                tmp = 1 + minchange_TD(AC, TV-coin) #take current coin and recurse
            if tmp < result:
                result = tmp
                memo[TV] = tmp
            
    return result

def minchange_BU(AC, TV):
    """
    # Determines minimum number of coins to make TargetValue from AvailableCoins
    ## Bottum-up dynamic programming iterative solution. THIS WILL BE FASTER THAN SLOW.
    ## Much faster than non-optimized recursive; ~TODO ms to converge on solution for TV=54.
    Input: (int) list of AvailableCoins \n
    ### Note: 1 is always included in AvailableCoins
    Input: (int) TargetValue \n
    Output: (int) minimum number of coins to solve \n
    """
    # build and initialize solution value table:
    SVT = [ [ -1 for value in range(TV+1)] for coin in AC]
    # SVT = [['0-0', '0-1', '0-2'],['1-0,', '1-1', '1-2'], ['5-0', '5-1', '5-2'], ['10-0', '10-1', '10-2']]
    
    # implement iterative algorithm:
    for coinindex in range(len(AC)):
        for value in range(TV+1):
            # print(SVT[coinindex][value])
            if AC[coinindex] == 0 or value == 0:
                SVT[coinindex][value] = 0
            # else:
            #     NV = TV // AC[coinindex]
            #     RM = TV % AC[coinindex]
            #     SVT[coinindex][value] = NV + SVT[coinindex][RM]
            # # print(SVT[coinindex][value])




def timetest(available, target, func):
	t0=time.time()
	x = func(available, target)
	tf=time.time()
	print(func, x, tf-t0)




AC=(100, 50, 25, 10, 5, 1)  #available coin denominations
TV = 49
# print("\noverall function return: ", minchange_TD(AC, TV))

# timetest(AC, TV, minchange_rec)
# timetest(AC, TV, minchange_TD)

minchange_BU(AC=[0, 1, 5, 10], TV=1)
