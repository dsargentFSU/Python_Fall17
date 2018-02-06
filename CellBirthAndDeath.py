"""
Dawn Sargent

We will simulate the birth and death process of cells, starting with a single 
cell, for 20 minutes or until there are no cells left. We want to examine
the mean and variance of the number of cells at the end of the study when given 
different average time till birth rates.
"""

from random import expovariate as randexp
import numpy as np

avgTillBirthList = [1, 1.05, 1.1] # Units are in minutes
totTrials = 10000
timeLimit = 20

for avgTillBirth in avgTillBirthList:
    
    avgTillDeath = 1 # Units are in minutes
    endCellCounts = []
    
    for trialNum in range(totTrials):

        count = 1
        cells = [0] # Each cell is an element of the list
                    # The value indicates the time at that cell's birth

        for x in cells: # Loop for each cell
        
            timer = x # Set timer to the cell's birth time
            
            # Loop for each cell's lifespan within the time limit
            while timer <= timeLimit:

                # Generate the cell's time till split and time till death
                timeTillSplit = randexp( 1 / avgTillBirth )
                timeTillDeath = randexp( 1 / avgTillDeath )
                
                # If the cell split before it died and before the time limit
                if timeTillSplit <= timeTillDeath and timer + timeTillSplit <= timeLimit:            
                    timer += timeTillSplit
                    cells.append( timer ) 
                    count += 1 
                
                # Else if the cell died before it split and before the time limit
                elif timeTillSplit > timeTillDeath and timer + timeTillDeath <= timeLimit:
                    count -= 1
                    timer = timeLimit + 1 # Break the loop for this cell
                    
                    
                else: # Then the cell neither split nor died before the time limit
                    timer = timeLimit + 1 # Break the loop for this cell
                    
        endCellCounts.append(count)
        
    avgEndCount = np.mean(endCellCounts)
    var = np.var(endCellCounts, ddof=1)    
    print()
    print("Given an avg till birth of " + str(avgTillBirth) + 
          " and avg till death of " + str(avgTillDeath) + ":")   
    print("Mean of the number of cells remaining: " + str(avgEndCount))
    print("With a variance of " + str(var) )     