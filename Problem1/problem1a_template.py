##################################################################################
##################################################################################
## Template file for problem 1. 						##
## First, fill in your answer logic below					##
##################################################################################
#                                LOGIC GOES BELOW                     		#
##################################################################################
#
#First step is to get a random no which is equivalent to a no when we roll a die.
#Add these numbers to a list untill we get a no which is less than or equal to 
#penultimate no. Calculate the sum of these numbers and perform this simulation 10000
#times.
#
#
#
##################################################################################
##################################################################################
## You have to fill in two functions BELOW 					##
## Both take in input n = number of sides in the die 				##
## 										##									##
## 1. findSumDieRoll(n)	: Return expected value of sum 				##
## 2. findNumberOfRolls(n)  : Return expected value of number of rolls 		##
## 										##									##
## For both, you only have to fill in the math function where indicated     	##
## 										##									##
## You can run this template file to see the output of your functions       	##
## for a 6 sided die.								##
## Simply run: `python problem1_template.py`                            	##
## You should see the output printed once your program runs.                	##
##                                                                          	##
## DO NOT CHANGE ANYTHING ELSE BELOW. ONLY FILL IN THE LOGIC.      		##
##                                                                          	##
## Good Luck!                                                               	##
##################################################################################
##################################################################################


def findSumDieRoll(n):
    x=[]
    for i in range(10000):
        w=[0]
        while True:
            w.append(np.random.choice(np.arange(1,n) , 1, [1/n]*int(n)))
            if w[-1]<=w[-2]:
                break
        sum=np.sum(w)
        final_sum=sum-w[-1]
        x.append(final_sum)
    sumRolls=np.mean(x)

    return round(sumRolls, 2)

def findNumberOfRolls(n):
    x=[]
    for i in range(10000):
        w=[0]
        while True:
            w.append(np.random.choice(np.arange(1,n) , 1, [1/n]*int(n)))
            if w[-1]<=w[-2]:
                break
        rolls=len(w)-1
        x.append(rolls)
    
    numRolls =np.mean(x)

    return round(numRolls, 2)

if __name__ == "__main__":
    import numpy as np
    numberOfSides = 6.0
    sumOfRolls = findSumDieRoll(numberOfSides)
    numberOfRolls = findNumberOfRolls(numberOfSides)
    print('For a %i-sided die, expected value of sum: %.2f and number of rolls: %.2f'%(numberOfSides, sumOfRolls, numberOfRolls))
