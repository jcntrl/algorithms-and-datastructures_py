def minchange_TD(AC, TV):
    
    if TV == 0: #basecase
        return 0
    
    result = 0
    
    for coin in AC:
        print("coin", coin, "TV", TV)
        if coin <= TV:
            print(TV, ' - ', coin, ' = ', TV-coin)
            TV -= coin
            result += 1
            minchange_TD(AC, TV)
    return result
        

# def minchange(AC, TV):
#     result = 0
#     result = 

AC=(100, 50, 25, 10, 5, 1)
print("\nfuncreturn: ", minchange_TD(AC,4))
