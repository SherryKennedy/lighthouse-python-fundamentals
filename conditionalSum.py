def conditionalSum(values, condition):
  '''
        conditionalSum: add values pass in array according to the condition passed 
        inputs: values
        inputs: condtion  'even' or 'odd'
        returns: sum_num
         epected output:
        6
        9
        144
        0
  '''
  sum_num =0
  if not values:
    return 0 
  try:
    for num in values:
      if ((condition=='even') and ((num %2)== 0)):
        #add all even values
        sum_num += num
      elif ((condition=='odd') and ((num %2)!= 0)):
        #add all odd numbers
        sum_num += num
  except AssertionError as error:
    print(error)
  return sum_num


print(conditionalSum([1, 2, 3, 4, 5], "even"))
print(conditionalSum([1, 2, 3, 4, 5], "odd"))
print(conditionalSum([13, 88, 12, 44, 99], "even"))
print(conditionalSum([], "odd"))


