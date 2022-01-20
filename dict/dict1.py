# Creating empty dictionaries
my_dict = {}
my_dict = dict()

# Creating a dictionary with keys and values
my_cat = {'name':'Mr sniffles','age':18, 'color':'black'}

# print cat name
catName = my_cat['name']



# Add data to dic
my_cat['playful']= " Yes"
print(my_cat)

# Dict methods
''' Get individual keys'''
print(my_cat.keys()) 
''' convert the above to a list of keys'''
print(list(my_cat.keys()))