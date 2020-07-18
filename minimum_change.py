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

AC=(100, 50, 25, 10, 5, 1)  #available coin denominations
TV = 21  #result of TV = 21 should be 4
print("\noverall function return: ", minchange_rec(AC, TV))
