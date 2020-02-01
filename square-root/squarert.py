#Find the square root of 76 without using a library or raising a value to the (1/2) power.

guess = 7
num = 76
epochs = 100

step0 = guess
step1 = num/guess

step2 = (step0 + step1)*(1/2.)
step3 = num/step2

step4 = (step2 + step3)*(1/2.)
step5 = num/step4

step6 = (step4 + step5)*(1/2)
step7 = num/step6

step8 = (step6 + step7)*(1/2)
step9 = num/step8

step10 = (step8 + step9)*(1/2)
step11 = num/step10

step12 = (step10 + step11)*(1/2)
step13 = num/step12

step14 = (step12 + step13)*(1/2)
step15 = num/step14

step16 = (step14 + step15)*(1/2)
step17 = num/step14

step17 

#Need to turn this into a loop.
