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
        #self.workRange=list(range(workstart, workEnd))
        #self.visited = []
        #self. Appointments = fixed
       # self.fixedindex = []
        #self.exclusionlist = []
        self.df = df
        #def Decision(fixed):
         #   if fixed != NULL:
          #      FixedAppointments(self)
           # else:
            #    Default(self)    
            #test = pivoted[[0]]
                
    def Default(self):
        print(self)
        visited = [0]
        Betriebe = len(self)
        count = 0

        

        while count <= Betriebe:
            print(str(count)+' rounds')
            current = visited[-1]
            
            print(str(current)+' current Column')
            #print(str(type(current))+'current')
            #
            # print(self[[current]])
            currentindex = self[[current]]
            print(str(currentindex))

            minrow = currentindex.idxmin()
            smallestindex = minrow.loc[0]
            print(type(minrow))
            print(str(smallestindex)+' current row')

            while smallestindex in visited:
                #currentindex.drop(currentindex[smallestindex])
                currentindex = currentindex.drop(index = smallestindex)
                minrow = currentindex.idxmin()

                print("pop")
                

            print('already done')
            print(visited)
            visited.append(smallestindex)
            count=count+1
            return(visited)
            
                            

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