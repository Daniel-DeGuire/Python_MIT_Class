def remove_every_other(my_list):
    r = [] 
    for i in range(len(my_list)): 
        if i % 2 == 0: #Checks if even
            r.append(my_list[i]) #Append if even
    return r