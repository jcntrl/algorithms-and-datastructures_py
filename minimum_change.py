

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


import time
def timetest(available, target, func):
	t0=time.time()
	x = func(available, target)
	tf=time.time()
	print(func, x, tf-t0)




AC=(100, 50, 25, 10, 5, 1)  #available coin denominations
TV = 54
# print("\noverall function return: ", minchange_TD(AC, TV))

timetest(AC, TV, minchange_rec)
timetest(AC, TV, minchange_TD)


