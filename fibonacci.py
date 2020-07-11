import time

def naivefib(n):
    '''
    naive solution - works as expected, 
    after n=40, excessive time
    '''
    if n == 0 or n == 1:
        return n
    solution = naivefib(n-1) + naivefib(n-2)
    return solution

def fastfibtopdown(n, memo = {0:0, 1:1}):
    '''
    top-down recursive dynamic programming solution - works as expected. 
    Python recursion limit of 1000 calls.
    '''

    try: 
        return memo[n]
    except:
        result = fastfibtopdown(n-1) + fastfibtopdown(n-2)
        memo[n] = result
        return result

def fastfibbottomup(n):
    '''
    bottom up iterative dynamic programming solution - working.
    Solution to 1000000th fnum is too large for memory so will crash my 16GB MacBookPro, but it will solve it in reasonable time.
    Each iteration only stores three variables. 
    '''
    if n == 0 or n == 1:
        return n
    nmin2, nmin1 = 0, 1     #base case
    for fib in range(n-1):  #draw this out on a bottomup table
        result = nmin2 + nmin1  #recurrence relation
        nmin2, nmin1 = nmin1, result
    return result

def testfib(typ):
    '''
    accepts an input to specify which algorithm to run, to what (n)umber to calculate
    returns the specified fibonacci number and the time required to calculate it.
    ejects to an early return if number is too large and will cause problems.
        is there a way to do this with try/except?
        ... for now this is purely manual
    '''
    n = int(input("input an integer: "))

    if typ == 'naive':
        if n >40:
            return "this will take too long... abort."
        tinit = time.time()    
        naive = naivefib(n)
        tfin = time.time()
        deltat = tfin-tinit
        return naive, deltat

    if typ == 'fastTD':
        if n >1000:
            return "this will make the computer explode... abort."
        tinit = time.time()    
        fast = fastfibtopdown(n)
        tfin = time.time()
        deltat= tfin-tinit
        return fast, deltat
        
    if typ == 'fastBU':
        if n >=1000000:
            return "About 11s to millionth fibnum, but this will make the computer explode... abort."
        tinit = time.time()    
        fast = fastfibbottomup(n)
        tfin = time.time()
        deltat= tfin-tinit
        return fast, deltat


print(testfib(str(input("'fastTD' or 'fastBU' or 'naive': ",))))