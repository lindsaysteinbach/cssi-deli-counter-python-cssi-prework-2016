
katz_deli = []

#1. line() function

def line(list):
  n=0
  new_list=""

  if (len(list)!=0):
    while n < len(list):
      new_customer = str(n+1) + ". " + list[n]
      new_list = new_list + " " + new_customer 
      n = n + 1
    return "The line is currently:" + new_list 
  else:
    return "The line is currently empty."

#2. take_a_number function

def take_a_number(list, name):
  list.append(name)
  number = len(list)
  message = "Welcome, " + name + ". You are number " + str(number) + " in line."
  return message

#3. now_serving() function

def now_serving(list):

  if (len(list)>0):
    current_name=list[0]
    del list[0]
    serving_message = "Currently serving " + current_name + "."
  else:
    serving_message = "There is nobody waiting to be served!"

  return serving_message
  
  
