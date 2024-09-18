string = '''chinmay the man the myth the legend'''
print(string)  

print(len(string))
print(string.endswith("may"))
print(string.startswith("ch"))
print(string.capitalize())
print(string.title())
print(string.find("legend"))

replaced_string = string.replace("legend", "Ghidorah")
print(replaced_string)