# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:04:47 2023

@author: jules
"""


import pandas as pd
#inputs: distance matrix(MUST INCLUDE), potentially a dictionary of fixed appointments, start and end of work time


#The point represented by the ID 0 will be treated as the starting point. In a first step the lower function will find the point with the smallest distance to zero and then go searching for the next closest point
class Itinerary:
    def __init__(self,df, wStart, wEnd, fixed):
        #Distance matrix, Dataframe object
        self.df = df
        #hour of work start, integer
        self.wStart = wStart
        #hour of work end, integer
        self.wEnd = wEnd
        #hour of fixed appointment, dictonary: index of place = key, hour=value
        self.fixed = fixed
                
    def Default(self):
        print(self.df)
        self = self.df.drop(0,axis=0)
        print(self.df)
        #Prints inicial Table
        visited = [0]
        #Saves all places where we jhave already been
        betriebe = len(self.df)
        #Gesamte Anzahl an zu besuchenen betrieben
        count = 0

        

        while count < betriebe:
            print(str(count)+' rounds')
            current = visited[-1]
                        
            print(str(current)+' current Column')
            currentindex = self.df[[current]]
            #currentindex displays just the one Column, of the Place we are right now to find the smallest

            print(str(currentindex))
            minrow = currentindex.idxmin()
            print(minrow)
            #Searches minimum Row
            print(minrow.loc[current])
            smallestindex = minrow.loc[current]
            print(smallestindex)
            print(type(smallestindex))
            #Takes just the index of minrow 1 23 -> 1 
            print(str(smallestindex)+' current row')
            print(visited)

            if smallestindex in visited:
                
                self.df = self.df.drop(smallestindex,axis=0)
                minrow = currentindex.idxmin()
                #Searches minimum Row
                smallestindex = minrow.loc[current]
                visited.append(smallestindex)



            else:
                self.df = self.df.drop(smallestindex,axis=0)
                minrow = currentindex.idxmin()
                smallestindex = minrow.loc[current]
                visited.append(smallestindex)


                #currentindex.drop(currentindex[smallestindex])
                print("pop")
            count = count + 1
            print(currentindex)
            print(visited)
            print('already done')
        return(visited)
            
                            


    def Fixed(self):
        
        print(self.df)
        itinerary = []
        prior = 0
        print(self.fixed)
        #include line about false positive issue
        for i in range(self.wStart, self.wEnd):
            itinerary.append(i)
        itinerary[0]=0
        for element in self.fixed:
            print(self.fixed)
            print(element)
            #insert index of fixed appoint at correct point in itinerary. Using value to identify itinerary index for the key
            itinerary.insert(itinerary.index(self.fixed.get(element)),element)
            #determine preceeding appointments of current fixed appointment
            #determine distance between prior fixed appointment and current fixed appointment
            Dist = round(self.df.at[prior, str(element)])
            print(self.df.at[prior, str(element)])
            halfDist = round(Dist/2)
            quartDist=round(halfDist/2)
            print(Dist)
            print('Dist')
            #checking whether previous appointment within acceptable range
            #for loop listing all items in column of the index of the current fixed appointment
            print(range(Dist))
            print('range Dist')
            print(range(halfDist))
            print('half Dist range')
            #prior =
            for item in list(self.df[str(element)]):
                print(item)
                print('for item loop')
                if item in [range(quartDist+1)]:
                    print([range(quartDist)])
                    print('if1')
                    if item.index not in itinerary:
                        leftidx = element -1 
                        itinerary.insert(leftidx, item.index)
                        self.df.drop(str(item.index))
                        prior = item.index
                        print(prior)
                        print('prior')
                    else:
                        print('Error1')
                        pass
                    
                else:
                    print('else')
                    if item in [range(halfDist+1)]:
                        print('if2')
                        if item.index not in itinerary:
                            leftidx = element -1 
                            itinerary.insert(leftidx, item.index)
                            self.df.drop(str(item.index))
                            prior = item.index
                            print(prior)
                            print('prior')
                        else:
                            print('Error2')
                            pass
                    else:
                        print('else2')
                        if item in [range(Dist+1)]:
                            print('if3')
                            if item.index not in itinerary:
                                leftidx = element-1 
                                itinerary.insert(leftidx, item.index)
                                self.df.drop(str(item.index))
                                prior = item.index
                                print(prior)
                                print('prior')
                            else:
                                print('Error3')
                                pass
                        else:
                            print('there is no item in range')
                        #What to do, when there isn't an item that is within that distance?
                            
        print(itinerary)
        return(itinerary)

        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

#Default(df)