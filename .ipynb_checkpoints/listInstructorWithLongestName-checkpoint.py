def instructorWithLongestName(instructors):
    '''
        instructorWithLongestName: takes in a list of values, with key, value pairs, 
                                   finds the name of the instructors in the list 
                                   returns the instructors with the longest name
        inputs: instructors, as list
        return: instructor , as dict list item
        Expected output:
            {name: "Jeremiah", course: "Data"}
            {name: "Domascus", course: "Web"}                            
    '''
    #print(any(isinstance(val, typ) for val in self))
    tempname =''
    iterCnt = 0
    instrData = []
    try:
        for instructor in instructors:
            for k, v in instructor.items():
                if k=='name':
                    if iterCnt > 0:
                        if len(v) > len(tempname):
                            tempname = v
                            instrData[0]= instructors[iterCnt]
                    else:
                        #first time through add value
                        tempname = v
                        instrData.append(instructors[iterCnt])
    
            iterCnt +=1  #keep track of instructor want to add
    finally:
        return instrData[0]

    
print(instructorWithLongestName([
  {'name': "Samuel", 'course': "iOS"},
  {'name': "Jeremiah",'course': "Data"},
  {'name': "Ophilia", 'course': "Web"},
  {'name': "Donald", 'course': "Web"}
]))
print(instructorWithLongestName([
  {'name': "Matthew", 'course': "Data"},
  {'name': "David", 'course': "iOS"},
  {'name': "Domascus", 'course': "Web"}
]))
