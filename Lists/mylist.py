list_a = ["a","b","c","d"] # list of strings
list_b = [1,2,3,4,5,6] # list of numbers
list_c = [1,"west",34,"longitude"] # mixed list

'''
You can have a list in an list( Nesting)
'''
list_d = [ ["a","b","c","d"],[1,2,3,4,5,6],[1,"west",34,"longitude"]] # nested list


# join lists using extend

list_e = list_a.extend(list_b) # this didnt work

'''
    List Methods

'''
list_a.append('e')
print(list_a)
print(list_e)
print(list_d)
