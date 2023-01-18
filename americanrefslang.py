
# Dictionaries are different from lists as you look up the item by its key not its index

# Using curly brackets - Items are key value pairs and separated by colons

slang = {"cheerio":"goodbye", 'knackered':'tired','yonks':'ages'}
print(slang)

# To look up a value we send in a key (instead of an index)

print(slang['cheerio'])

#  Dictionaries can hold anything, numbers, strings, a mix of both

# We can create an empty dictionary using just a name = {}
# Example

slang = {}
slang['cheerio'] = 'goodbye'
slang['smashing'] = 'terrific'
slang['knackered'] = 'tired'
print(slang)

# To update values in your dictionary
slang['smashing'] = 'awesome'
print(slang)
# or to look up the key value use the following
print(slang['smashing'])

# Removing dcitionary items
slang = {"cheerio":"goodbye", 'knackered':'tired','yonks':'ages'}
del slang['cheerio']
print(slang)

# Get item that might not be there
slang = {"cheerio":"goodbye", 'knackered':'tired','yonks':'ages'}
slang['bloody'] # This throws an error

#instead use get


