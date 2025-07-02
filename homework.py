def changing_InName(name):
    j = 1
    new_name = ''
    
    for i in range(0, len(name), 2):
          new_name += name[i] + str(j)
          j+= 1
    return new_name    
name = input('enter the name you want to make change in it >>> ')
print(changing_InName(name))