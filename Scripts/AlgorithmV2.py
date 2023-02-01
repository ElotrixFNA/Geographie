# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 08:07:24 2023

@author: jules
"""

import pandas as pd
#inputs: distance matrix(MUST INCLUDE), potentially a dictionary of fixed appointments, start and end of work time


#The point represented by the ID 0 will be treated as the starting point. In a first step the lower function will find the point with the smallest distance to zero and then go searching for the next closest point
class Itinerary:
    def __init__(self,df):
        self.df = df
                
    def Default(self):
        print(self)
        self = self.drop(0,axis=0)
        print(self)
        #Prints inicial Table
        visited = [0]
        #Saves all places where we jhave already been
        betriebe = len(self)
        #Gesamte Anzahl an zu besuchenen betrieben
        count = 0

        

        while count < betriebe:
            print(str(count)+' rounds')
            current = visited[-1]
                        
            print(str(current)+' current Column')
            currentindex = self[[current]]
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
                
                self = self.drop(smallestindex,axis=0)
                minrow = currentindex.idxmin()
                #Searches minimum Row
                smallestindex = minrow.loc[current]
                visited.append(smallestindex)



            else:
                self = self.drop(smallestindex,axis=0)
                minrow = currentindex.idxmin()
                smallestindex = minrow.loc[current]
                visited.append(smallestindex)


                #currentindex.drop(currentindex[smallestindex])
                print("pop")
            count = count + 1
            print(currentindex)
            print(visited)
            print('already done')
            
                            

            #INCLUDE PART ABOUT EXCLUDING ALREADY USED IDs
                
            #print(visited)
            
       # def ListFixedAppointment(Appointments):
        #    #for each hour in work range append an element in the list (if half-hour appoints, do that twice)
         #   for i in workRange:
          #      visited.append(0)
           # #place fixed appointments at their respective spot
            #for element in Appointments:
             #   key = element
              #  #find time for each id in fixed appointments list
               # time = list(Appointments.keys().index(key))
                #visitedindex = time-1
                #fixedindex.append(visitedindex)
                #place IDs with set time at their respective position in visited list
               # visited. insert(visitedindex, str(key))                        
            #return(visited)
        
        
        #def Fixedvisited(visited, df, Appointments):
            #for element in fixedindex:
               # newindex = fixedindex[element]-1
               # column=visited.index(element)
                #smallest = df[df[column]==df[column].min()]
                #visited.append(smallest).index(newindex)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

#Default(df)