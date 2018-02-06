"""
Dawn Sargent

Suppose n points are placed uniformly at random in the unit square.
We want to know the expected minimum distance between these points.
This program perfoms a Monte-Carlo simulation of this and graphs 
the distance versus n.
"""

from random import uniform as randu
from scipy.spatial.distance import pdist
from matplotlib import pyplot as plt
 
nList = [100, 200, 300, 400, 500] # values for n
numTrials = 1000
expectedValues = []   

for n in nList: 
    
    minDistances = []

    for trial in range(numTrials):
        points = [ [ randu(0, 1), randu(0, 1) ] for x in range(n) ]
        minDistances.append( min( pdist(points) ) )
    
    expectedValues.append( sum(minDistances) / n )

plt.plot(nList, expectedValues)
plt.show()

for count in range( len(nList) ): 
    print( "The expected value for n = " + str(nList[count]) + 
           " is about " + str(expectedValues[count]) ) 