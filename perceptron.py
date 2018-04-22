# perceptron.py
# Ericsson Schroeter
# AI: Homework 5
# Dr. Andrew Plummer

import sys
import numpy
import random
import matplotlib.pyplot as p

# Global Variables
l = 0.2                                     # Learning rate
w = [0,random.random(),-random.random()]    # Array of inital weights
x_1 = [-2,-1,0,1,2]                         # x_1 axis values (inputs)
x_2 = []                                    # x_2 (outputs)

# Data set arrays for training
# The NOT, OR, and AND functions were all sucessfully learned by the percpetron.py script.
# The results can viewed in the graphs outputed by the script.
# The XOR function was not due to the fact that its data set was not seperatable by a
# linear line regardless of the best efforts of the perceptron.  This can also be seen
# in the graphed results.

########## The blue line is the initial state of the percpetron. 'x' = True 'o' = False  This script can be compiled in Python and Python3. ##########

not_training_set = [[-1,1],[1,-1]]
and_training_set = [[-1,-1,-1],[-1,1,-1],[1,-1,-1],[1,1,1]]
or_training_set = [[-1,-1,-1],[-1,1,1],[1,-1,1],[1,1,1]]
xor_training_set = [[-1,-1,-1],[-1,1,1],[1,-1,1],[1,1,-1]]

# Enter desired data set to train perceptron
data = and_training_set

# Plot initial slope
for i in x_1:
    x_2.append(-1*(w[1]/w[2])*i-(w[0]/w[2]))

p.plot(x_1,x_2)

# Plot true and false data points based on data set being learned
if data == not_training_set:
    p.scatter(1,0,marker='o')
    p.scatter(-1,0,marker='x')
elif data == and_training_set:
    p.scatter(1,1,marker='x')
    p.scatter(-1,1,marker='o')
    p.scatter(1,-1,marker='o')
    p.scatter(-1,-1,marker='o')
elif data == or_training_set:
    p.scatter(1,1,marker='x')
    p.scatter(-1,1,marker='x')
    p.scatter(1,-1,marker='x')
    p.scatter(-1,-1,marker='o')
elif data == xor_training_set:
    p.scatter(1,1,marker='o')
    p.scatter(-1,1,marker='x')
    p.scatter(1,-1,marker='x')
    p.scatter(-1,-1,marker='o')

prev_w = []

# While current weight array is different from previous weights
while w != prev_w:
    
    # Copy current weights as previous weights
    prev_w = w[:]

    # For each element of the given data set
    for i in data:
        # Print current weights
        print(w)
        
        # If correct output is equal to true
        if i[-1] == 1:
            # Then check if the true and false data point are above and below the curve, respectivly
            # If the this the case then continue loop and don't modify the weights
            # Otherwise modify the weights accordingly
            if w[0] + w[1]*i[0] + w[2]*i[1] > 0:
                continue
            else:
                w[0] += l
                w[1] += l*i[0]
                w[2] += l*i[1]
        else:
            if w[0] + w[1]*i[0] + w[2]*i[1] < 0:
                continue
            else:
                w[0] += -1*l
                w[1] += -1*l*i[0]
                w[2] += -1*l*i[1]

    # Save the new curve data
    y = 0

    for i in x_1:
        x_2[y] = (-1*(w[1]/w[2])*i-(w[0]/w[2]))
        y += 1

# Plot and show the final slope
# If the plot function is contained in the while loop it will plot each slope per epoch
p.plot(x_1,x_2)

p.show()
