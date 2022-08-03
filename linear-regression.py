# Overview: This program was written to perform linear regresson on a data set to find the line of best fit. To do so, it uses 
# gradient descent. Currently, the data is generated randomly.
# Creation Date: 1/13/2022
# Author: Shayan Bathaee
# Concepts were inspired by the following article: https://towardsdatascience.com/linear-regression-using-gradient-descent-97a6c8700931


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# DEFINE PARAMETERS
limit = True # set to true if you would like to limit the iterations 
iterations = 50 # number of desired iterations (only applies if limit is True)
learningRate = 0.001
Range = 20 # define how big the graph is

# DEFINE CLASS TO PERFORM REGRESSION
class Regression:
    def __init__(self, limit, iterations, learningRate, Range): # initialize the regression specifying iterations and range
        self.limit = limit
        self.iterations = iterations
        self.learningRate = learningRate
        self.m = self.b = 0 
        self.Range = Range
        self.X = np.arange(0, Range + 1, 1) # X is a numpy array of integers 0 through Range
        self.Y = self.m*self.X + self.b # this stores the data for the predicted line. It just starts as 0
        self.data = np.random.randint(0, Range + 1, Range + 1) # random data within the range. may improve on this later
        #self.data = self.X # this is used for testing

    def calculateLoss(self):
        self.loss = 0 # initialize the loss to 0
        n = self.Range + 1 # n = number of data points
        for x in range(0, n, 1): # for each data point
            self.loss += (self.data[x] - (self.m*x + self.b)) ** 2 # calculate the squared error
        self.loss = self.loss / n # divide the summation by n
        return self.loss # return the loss

    def learn(self):
        self.dm = 0 # initialize derivatives to 0
        self.db = 0
        n = self.Range + 1 # n = number of data points
        for x in range(0, n, 1): # for each data point
            self.dm += x*(self.data[x] - (self.m*x + self.b)) # summation for derivative with respect to m
            self.db += self.data[x] - (self.m*x + self.b) # summation for derivative with respect to b
        self.dm = (-2/n)*self.dm # scaling part of derivative with respect to m
        self.db = (-2/n)*self.db # scaling part of derivative with respect to b
        self.m = self.m - self.learningRate*self.dm # adjust m and b using the derivative values and learning rate
        self.b = self.b - self.learningRate*self.db
        

# INITIALIZE THE REGRESSION, INITIALIZE THE PLOT
LR = Regression(limit, iterations, learningRate, Range)
fig, ax = plt.subplots() # create a figure, make ax the only subplot
ax.grid()
# plt.figtext(0.5, 1, 'weertwer', ha="center", va="center")
dataText = ax.text(0.02, 0.86, 'weertwer', transform=ax.transAxes, backgroundcolor="white")
X = LR.X # X is a numpy array of integers 0 through Range
Y = LR.data # Y is a numpy array of random numbers within [0, Range]
line, = ax.plot(X, 0*X) # start by plotting the line at 0
count = 0


# DEFINE FUNCTIONS USED FOR ANIMATION
def init(): # Initialize the animation
    line.set_ydata(LR.m*X) # let y = 0
    dataText.set_text("m = 0\nb = 0\niterations = 0")
    return line, dataText # return the line 

def animate(i): # This function determines what changes in each frame
    displayString = "m = " + str(round(LR.m, 2)) + "\nb = " + str(round(LR.b, 2)) + "\niterations = " + str(i)
    if i == iterations and LR.limit == True:
        # display the final slope, y intercept, and iterations
        print(displayString)
        ani.event_source.stop() # stop if we reach our iteration count and limit is true
    LR.learn() # use gradient descent to update m and b
    line.set_ydata(LR.m*X + LR.b) # reset the line with our new m and b
    dataText.set_text(displayString)
    return line, dataText # return 


# BEGIN ANIMATION AND PLOTTING
ani = animation.FuncAnimation(fig, animate, init_func = init, interval = 1, blit = True)
plt.plot(X, Y, 'bo') # plot the data points
plt.ylim([0, 1.2*LR.Range]) # set the limits of the graph depending on our range (extra space added above for labels)
plt.xlim([0, LR.Range])
plt.show() # display the plot an animation
# display the final slope, y intercept, and iterations
if LR.limit == False or count < iterations:
    displayString = "m = " + str(round(LR.m, 2)) + ", b = " + str(round(LR.b, 2)) + ", iterations = " + str(count)
    print(displayString)
