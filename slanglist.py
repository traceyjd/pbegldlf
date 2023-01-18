
slang = ["cheerio", "pip pip", "smashing"]
print(slang)

# append to list
slang.append("cheeky")
slang.append("yonks")
print(slang)

# To remove items from the list we can use the name of the item or its position
slang.remove("cheeky") # or del slang[3]
print(slang)

# To remove a slice of the list
del slang[:2]
print(slang)
