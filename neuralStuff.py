import pandas as pd 
import numpy as np


# Initialize Stuff

# Define Size
size = 500
sigma = 2
# Make connection array
randMat = np.random.rand(size, size) # Connection matrix
columnSums = randMat.sum(axis=0)
connectionMatrix = sigma*randMat/columnSums
#print(connectionMatrix)

# Create starting state
#startingState = np.zeros(size)
startingState = np.random.randint(2, size=size)
#print('starting state is: ',startingState)


# Loop 

def iterateVector(state,connectionMatrix,size):

    # Multiplying by the connection array
    product = np.dot(connectionMatrix,state)

    # Rolling the dice
    #testMatrix = size*np.random.rand(size)
    testMatrix = np.random.rand(size) #SIZE ISSUE
    #print(testMatrix)
    newState = 1 * (product > testMatrix)

    return newState



#print('next state is :',testState)

workingState = startingState

resultMatrix = startingState
for i in range(0,5):

    # update state
    workingState = iterateVector(workingState,connectionMatrix,size)

    # save state
    resultMatrix = np.vstack((resultMatrix,workingState))

print(resultMatrix)



# # Plotting

# import matplotlib.pyplot as plt

# plt.imshow(resultMatrix)
# plt.show()


# import matplotlib.pyplot as plt

# plt.eventplot(resultMatrix.T)    
# plt.show() 

