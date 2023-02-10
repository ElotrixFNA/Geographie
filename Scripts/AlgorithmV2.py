# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:04:47 2023

@author: jules, Felix Erb
"""


import pandas as pd
import string
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
            #To get the last integer in visited

            print(str(current)+' current Column')
            currentindex = self.df[[current]]
            #currentindex displays just the one Column, of the Place we are right now to find the smallest

            print(str(currentindex))
            minrow = currentindex.idxmin()
            #gets the Index of the Row with the lowest value instead of the value itself
            print(minrow)
            #Searches minimum Row
            print(minrow.loc[current])
            smallestindex = minrow.loc[current]
            #gets just the row-index, so we can save the variable in visited
            print(smallestindex)
            print(type(smallestindex))
            #Takes just the index of minrow 1 23 -> 1 
            print(str(smallestindex)+' current row')
            print(visited)

            if smallestindex in visited:
                #if the nearest place is already visited we 
                self.df = self.df.drop(smallestindex,axis=0)
                #we drop the whole Row from the table, so its easier to find the smallest distant place
                #cause now the visited places arent in the original table anymore
                minrow = currentindex.idxmin()
                #Searches minimum Row
                smallestindex = minrow.loc[current]
                #extracts just the rowindex
                visited.append(smallestindex)
                #we add the nearest place to the visited list



            else:
                self.df = self.df.drop(smallestindex,axis=0)
                #we drop the Row since its the nearest place, and it isnt visited yet
                minrow = currentindex.idxmin()
                smallestindex = minrow.loc[current]
                #get the row-index of the minimum row again
                visited.append(smallestindex)
                #appends the rownumber to the visited list


                #currentindex.drop(currentindex[smallestindex])
                print("pop")
            count = count + 1
            print(currentindex)
            print(visited)
            print('already done')
        return(visited)
            

  
                               
                            ################
                            ################
                            #    FIXED     #
                            ################
                            ################




    def Fixed(self):
        self.df = self.df.drop(0,axis=0)
        #Drop The Row 0
        original_table = self.df
        #save the original table cause we have to come back to it later
        print(self.df)
        itinerary = []
        #empty itinerary
        visited = [0]
        #we start at 0 so we start with that value
        duration = 0.5
        #duration of a meeting
        fixedAPT = self.fixed
        #the Fixed appointments
        sortedFixed =  {k: v for k, v in sorted(fixedAPT.items(), key=lambda item: item[1])}
        #this command sorts the fixed appointments by its time (value)
        #sorts the fixed appointments by the Time they occur
        print(sortedFixed)

        betriebe = self.df.index
        #gets every location 1-3
        print(betriebe)
        fixedLocations = fixedAPT.keys()
        #this gets just the number of the location without the value
        freeAPT = [betriebe.drop(fixedAPT.keys())]
        #subtracts all location with those who have an fixed appointment.
        #with that we can check what location we could visit in the spare time
        print(len(betriebe))
        #length of betriebe
        print(freeAPT)
        currentTime = self.wStart

        count = 0


        for i in range(len(self.df) + 1):
            itinerary.append(string.ascii_uppercase[i])
            #fills up itinerary with the amount of Appointments 
            #Loads up itinerary with Letters A-D + 1 so 0 is inside

        while count < len(betriebe):
            #as long as the count is lower then 4
            print(len(betriebe))
            print(str(count) + ' current count')
            count = count + 1
            current = visited[-1]
            #sets the current location
            print('current Position ' + str(current))
            timeNextAppointment = min(sortedFixed.values())
            #gets the time of the next fixed appointment by getting the minimum value of the sorted fixed appointments
            nextaptLocation = min(sortedFixed.items(), key=lambda x: x[1])[0]
            #gets the location of the next fixed appointment 
            print(str(nextaptLocation) + ' is the next location and at ' + str(timeNextAppointment) + ' is next appointment')
            Difference = (timeNextAppointment - (currentTime + duration)) * 60
            #Gets the difference between the the time of the next appointment, the current time plus the duration in minutes
            print(str(Difference) + ' Minutes time frame')
            print(current)
            print(nextaptLocation)
            DurationToFixed =(self.df.loc[nextaptLocation, current])/60
            #is the duration of the drive to the next fixed appointment in minutes
            print(str(DurationToFixed) + ' minutes travel time to the fixed appointment')
            self.df = self.df.drop(fixedLocations,axis=0)
            #drops the fixed Locations from the table, so only those remain in the Dataframe that arent fixed
            
            while Difference - DurationToFixed > 0:
                #first error of the script i think, it gets permanently lower as the while goes on...
                print(Difference)
                print('if')

                print(fixedLocations)
                
                print(self.df)
                minrow = self.df.idxmin()
                #gets the minimum row from the starting point (0)
                nearestfreeloc = minrow.loc[current]
                #Gets the nearest free location, same prinzip as in the script without the fixed location
                print(nearestfreeloc)
                starttosmallest = (self.df.loc[nearestfreeloc, current])/60
                #is the traveltime from the startinpoint to the nearest Location without fixed appointment in minutes
                smallesttofixed =(original_table.loc[nextaptLocation, nearestfreeloc])/60
                #is the traveltime from the nearest location whiout fixed Appointment to the next fixed Appointment in minutes
                print(starttosmallest)
                print(smallesttofixed)
                DurationToFixed = duration + smallesttofixed + starttosmallest
                #Is the total time it takes to get from the starting location to the fixed appointment
                Difference = Difference - DurationToFixed
                #new Difference
                print(DurationToFixed)
                print(Difference)

                print(fixedLocations)

            del fixedAPT[nextaptLocation]
            #deletes the Fixed appointment what we visited from the List, means the one remaining would be location n. 1 at 10
            print(fixedAPT.keys())
    







                
            
            if Difference - DurationToFixed == 0:
                print('perfect route to Fixed')
            
            else:
                print('error')

            



                            
        print(itinerary)
        return(itinerary)

        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

#Default(df)