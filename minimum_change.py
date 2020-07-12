def minchange_TD(AC, TV, res=0):
    
    if TV == 0: #basecase
        return res

    for coin in AC:
            # print("coin", coin, "TV", TV)
            if coin <= TV:
                # print(TV, ' - ', coin, ' = ', TV-coin)
                TV -= coin
                res += 1
                print('in loop res', res)
                minchange_TD(AC, TV, res)
    print('out of loop res', res)
    return res
        

AC=(100, 50, 25, 10, 5, 1)  #available coin denominations
TV = 4  #target value
print("\noverall function return: ", minchange_TD(AC, TV))
