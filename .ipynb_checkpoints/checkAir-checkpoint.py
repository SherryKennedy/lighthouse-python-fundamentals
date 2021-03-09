def checkAir(samples, threshold):
    '''
       checkAir:  Will check a collection of air samples.
       Inputs:    'samples' as a list of strings; where each string represents a small air sample that is either clean or dirty. 
                  'threshold' as a number representing the highest acceptable amount of dirty samples.
       Outputs:   'airQ' as string to return Polluted if there are too many dirty air samples, 
                                                or Clean if the proportion of dirty samples is below the threshold.
                                                
      NOTES: a threshold of 0.4 means that there must be less than 40% of total samples classified as dirty for our air to be considered clean.
      Example Outputs:
                      Polluted
                      Polluted
                      Clean
    '''
    clean_count = samples.count('clean')
    dirty_count = samples.count('dirty')

    #threshold for too many dirty samples 
    air_dirty = (dirty_count / len(samples))
    if air_dirty < threshold:
        airQ = "Clean"
    else:
        airQ = "Polluted"
    return airQ

print(checkAir(
  ['clean', 'clean', 'dirty', 'clean', 'dirty', 'clean', 'clean', 'dirty', 'clean', 'dirty'],
  0.3
))

print(checkAir(
  ['dirty', 'dirty', 'dirty', 'dirty', 'clean'],
  0.25
))

print(checkAir(
  ['clean', 'dirty', 'clean', 'dirty', 'clean', 'dirty', 'clean'],
  0.9
))

