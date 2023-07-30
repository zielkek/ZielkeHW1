"""
Title: Fermat Near Misses
File: ZielkeHW1
External Files Needed: N/A
Externaal Files Created: N/A
Programmer(s): Kevin Zielke
Programmer(s) Email: kevinzielke@lewisu.edu
Course & Section: CPSC 60500 - 002
Date of Completion: 07/29/2023

Program Details: This takes a user sumbitted n value, up to 12, and a user submitted k value, from 10 to 5000, 
and runs all possible combinations through Fermats Last Theorem, x^n + y^n ?= z^n, saving near misses starting at those with
less than aa 1% difference. The user may choose to display only the nearest miss found, or all misses in order of being found.

Resources: sites used for syntax and function clarification or options -  https://docs.python.org/3/library, https://www.geeksforgeeks.org/, https://www.w3schools.com/

"""
import bisect

def zVals(n, k):
    #creates list of z^n values                                            
    zList = []
    #go through all possibly z^n values and add to zList
    for i in range(0, (int((2*(k**n))**(1/n)))):            #range limits z values to the n root of the largest possible x^n + y^n value
        z = i**n
        zList.append(z)
    
    return zList

def xyzList(zList, xy):                                    
    #adds current xy value to list of z^n values in order and returns as new list 
    bisect.insort(zList, xy)
    zxyList = zList

    return zxyList

def findCloseZ(zxyList, xy):
    #finds z value closest to current xy                                
    z = (zxyList.index(xy) - 1)                             #z is the index directly below xy in the list
    
    if zxyList[len(zxyList) - 1] == xy:                     #if xy value is the last in the list
        zClose = zxyList[z]                                 #value below xy is closest z value

    else:                                                   #xy is not last value in list
        if (zxyList[z]/xy) > (xy/(zxyList[z+2])):           #check if xy is closer to the z value before or after it
            zClose = zxyList[z]                             #if xy is closer to the value before, that value is saved as zClose
        
        else:                                               #xy closer to value in front
            zClose = zxyList[z+2]                           #value in front of xy is the closest z
            
    return zClose

def zDiff(zClose, xy):
    #finds and returns the numerical difference between xy and closest z value                                     
    if xy > zClose:
         diff = xy - zClose
    else:
        diff = zClose - xy    
    return diff                                            

def percOff(diff, zClose, xy):                             
    #finds and returns the percentage, as decimal, difference between current xy and z
    if xy > zClose:
        offBy = diff/xy
        return offBy
    else:
        offBy = diff/zClose
        return offBy

def cutZlist(zList, z):                                    
    #removes values from z list less than current xy to reduce time needed to search list later
    zList = zList[z:]    
    return zList

def nearMisslist(missList, i, j, offBy, diff, n, zClose):   
    #adds values of new nearest miss to list 
    z = round(zClose**(1/n))                                #finds the n-sqrt(z) as current z is to the power of n
    x = i
    y = j
    percentOff = offBy * 100
    missList.append(x)
    missList.append(y)
    missList.append(z)
    missList.append(n)
    missList.append(diff)
    missList.append(percentOff)
    
    return missList

def xyAdd(n, k, m, missList):
    #calculates every x^n + y^n combination, calls and updates z^n values, and adds near misses to the list

    #runs as long as n is 3 or greater
    if n > 2:               
        #go through all possible x values                                 
        for i in range(10, k):                                
            zList = zVals(n, k)
            #go through all remaining y vals, start at x to avoid duplicate additions                                                            
            for j in range(i, k): 
                                 
                xy = (i**n) + (j**n)                        #xy is the current LHS of equation                                                                                

                zxyList = xyzList(zList, xy)                
                zClose = findCloseZ(zxyList, xy)            
                diff = zDiff(zClose, xy)                    
                offBy = percOff(diff, zClose, xy)           
                
                if j % 100 == 0:                            #every 100 y value iterations, reduce the size of the zList
                    z = (zxyList.index(xy) - 2)             #index in list of z values less than current xy and z value below 
                    zList = cutZlist(zList, z)                              
                    
                if offBy < m:                                #checks if difference percentage is lower than currest lowest
                    m = offBy
                    missList = nearMisslist(missList, i, j, offBy, diff, n, zClose)

        xyAdd(n-1, k, m, missList)                                    #xyAdd calls itself recursively with n being one lower
    
    return missList   

def nInput():
    #user enters their desired n value within the range
    n = int(input('Enter the exponent value between 2 and 12:\n'))              #exponent value
    if n < 3 or n > 12:                                                         #checks that n is in correct range
        print('Please provide a value between 2 and 12')
        nInput()
    return n

def kInput():
    #user enters their desired k value within the range                                                                                           
    k = int(input('Enter the k value, your x and y maximum, between 10 and 5000.\n'))                    #maxiumum x and y values
    if k < 10 or k > 5000:                                                                               #confirms k is in correct range
        print('Please provide a value for k that is between 10 and 5000')
        kInput()
    return k

def selectInput():                                                                                      
    #asks if user would like all found near misses or only the closest to zero
    print("\nProgram has completed, please choose if you would like the details of the nearest "
          "miss printed only, or if you would like all near misses found displayed.\n")
    print("A: Nearest Miss Only \nB: All Misses Starting at Less Than 1%: ")
    selection = input('Selection: ')
    selection = selection.upper()
    if selection != 'A' and selection != 'B':
        print("\nPlease enter A or B\n")
        selectInput()
    return selection

def displayMiss(selection, missList):
    #displays either the nearest miss or all near misses found based on user's previous selection.
    if selection == 'A':
        print("The nearest miss contains the following: \n x = ", missList[-6], "y = ", missList[-5], "z = ", 
          missList[-4], "n = ", missList[-3], "Value difference = ", missList[-2], "Percent difference = ", missList[-1], "%\n")
    elif selection == 'B':
        while len(missList) > 0:
            print("x = ", missList[0], "y = ", missList[1], "z = ", missList[2],"n = ", missList[3], "Value difference = ", missList[4], 
                  "Percent difference = ", missList[5], "%\n\n")
            missList = missList[6:]



def main():
    #introduces and starts the program
    input("     Welcome, this program will calculate the near misses of Fermat's Last Theorem, returning examples that are "
          "increasingly closer to 0, starting at a minimum difference of 1%. The program will calculate all near misses "
          "within the constraints provided, and then all you to choose if you would like only the nearest miss printed, or "
          "all near misses found presented. \n\n    The program is designed to accept exponent values from 3 to 12, and "
          "x y values, inputted as 'k', between 10 and 5000. Please see the readMe file if you would like to "
          "see options for increasing the n or k values.\n\n Once you are ready, press 'Enter' to continue and start the program.\n")

    n = nInput()                                          #calls function to obtain exponent value from user  
    k = kInput()                                          #calls function to obtain k value from user 
    m = .01                                               #current lowest % difference, start at 1%
    missList = []                                         
        #list containing values of near misses in order x, y, z, value difference, percent difference

    
    missList = xyAdd(n, k, m, missList)                   #calls primary function to run program

    

    selection = selectInput()                             #user choice of displaying all misses or only the nearest miss
    

    displayMiss(selection, missList)
    
   
    input('Press "Enter" to exit program')                  
        #allows program to remain open to view output until user chooses to close

    exit()

main()