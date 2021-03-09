'''
The system will use special parking sensors to keep track of all parking spots and monitor which ones are available. Every time a vehicle enters the parking lot, the system directs them to an available spot for their particular vehicle type, or notifies them that no spots are available.
There are three kinds of possible vehicles: regular cars, small cars, and motorcycles.

Regular cars can only park in R spots.
Small cars can park in R or S spots.
Motorcycles can park in R, S, or M spots.
In the list of parking spots, spots are written in both lower-case and upper-case. 
An upper-case letter means that the particular spot is AVAILABLE, while lower-case letters mean that the spot is UNAVAILABLE.

Our function must return a list with the coordinates of the spot as an [X, Y] pair. See the example input and output below for an illustration.
'''

def whereCanIPark(spots, vehicle):
    '''
     whereCanIPark()  
     Inputs: spots as list;     representing parking spots
             vehicle as string; type of the vehicle that is looking for a parking spot
     returns: cood as [X,Y] pair;    the coordinates of an available parking spot for the vehicle  X col being how far across, Y row going down
              False as boolean;  if there is no available spot.
     Sample Output:
                [4, 0]
                false
                [3, 1]    #note orig said [3,5] but this value is correct according to data gave
    NOTES:  Regular cars can only park in R spots.
            Small cars can park in R or S spots.
            Motorcycles can park in R, S, or M spots.
    NOTES:  Lowercase() UNAVAILABLE spot
            Uppercase() AVAILABLE spot
    
    '''
    #loop through the spots, have list of a list 
    y=0
    x=0
    try:
        for spot in spots:
            #gets a row, so your y coord, track at bottom of for loop
            #console.log("SPOTS: ", spot)
            #reset x for new row have
            x=0
            for aspot in spot:
                #counter for x , goes across each column , for ind number, increase at bottom 
                coord = [x,y]
                #console.log("SPOT: ", aspot)
                if vehicle == 'regular':
                    #Regular cars can only park in R spots.
                    if aspot == 'R':
                        #found a spot, return coordinate
                        return coord    
                elif vehicle == 'small':
                    #Small cars can park in R or S spots.
                    if (aspot in ['R','S']):
                        return coord
                elif vehicle == 'motorcycle':
                    #Motorcycles can park in R, S, or M spots.
                    if (aspot in ['R','S','M']):
                        return coord
                    
                x+=1
            y+=1
            
        #if get here , did not find a spot 
        return False 
    
    except AssertionError as error:
        print(errors)   

    
    
    


print(whereCanIPark(
  [
    # COLUMNS ARE X
    # 0    1    2    3    4    5
    ['s', 's', 's', 'S', 'R', 'M'], # 0 ROWS ARE Y
    ['s', 'M', 's', 'S', 'r', 'M'], # 1
    ['s', 'M', 's', 'S', 'r', 'm'], # 2
    ['S', 'r', 's', 'm', 'r', 'M'], # 3
    ['S', 'r', 's', 'm', 'r', 'M'], # 4
    ['S', 'r', 'S', 'M', 'M', 'S']  # 5
  ],
  'regular'
))


print(whereCanIPark(
  [
    ['M', 'M', 'M', 'M'],
    ['M', 's', 'M', 'M'],
    ['M', 'M', 'M', 'M'],
    ['M', 'M', 'r', 'M']
  ],
  'small'
))

print(whereCanIPark(
  [
    ['s', 's', 's', 's', 's', 's'],
    ['s', 'm', 's', 'S', 'r', 's'],
    ['s', 'm', 's', 'S', 'r', 's'],
    ['S', 'r', 's', 'm', 'r', 's'],
    ['S', 'r', 's', 'm', 'R', 's'],
    ['S', 'r', 'S', 'M', 'm', 'S']
  ],
  'motorcycle'
))