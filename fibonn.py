import time

gb = 52

def fib_recur(n):
    if n <= 1 :
        return n
    else:
        return(fib_recur(n-1) + fib_recur(n-2))

startTime1 = time.time()
fib_recur(gb)
endTime1 = time.time()
print(gb)
print(startTime1, endTime1)

    


#def fib_itter(n):
    #fibNumbers = [0,1]  # to the list    
    #for i = [2,n]:
        #fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
	#next i
    #return fibNumbers[n] 

	
