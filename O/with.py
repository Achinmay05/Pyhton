# f = open("file.txt")
# print(f.read())
# f.close()

#the same can be written using with statement like this
with open("first.txt") as f:
    print(f.read()) #now you don't have to explicitly close the file
    

