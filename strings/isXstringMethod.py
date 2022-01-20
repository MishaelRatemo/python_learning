'''
Is x string methods
isalpha() - returns True if the string consists of letters only and is not blank
isalnum() - returns True if the string consists of numbers and letters and is not blank
isdecimal() - returns True if the string contains only numeric characters
isspace() - returns True if the string contains only space,tabs or new lines
istitle() - returns True if the string contains words that start with uppercase letters

'''


alpha = "I like old music"
password = "K34jndnks"
number_string = "12345"
tabbs = "       "
titles = "I Love Cups"
false_titles = "I love Cups"

print( alpha.isalpha() )
print( password.isalnum() )
print( number_string.isdecimal() )
print( tabbs.isspace() )
print( titles.istitle() )
print( false_titles.istitle())