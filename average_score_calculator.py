scores = [100, 88, 70, 75, 67, 45, 30, 89, 99, 98]



def average_of_list_calculator(list):
  
  average = 0 
  
  for i in range(len(list)):   
    
    total = total + list[i]
    
  average = total / len(list)
    
  return average  
  
def average_of_list_calculator_minus_lowest_2(list):

  sorted_list = sorted(list)

  del sorted_list[0:2]

  return average_of_list_calculator(sorted_list)
  
  
  


 
  
  
  
  
  
  
print "Average score is", average_of_list_calculator(scores) 
print "Average score minus the lowest two is", average_of_list_calculator_minus_lowest_2(scores)

