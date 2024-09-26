words = ["Donkey", "Begairat", "Besharam", "Badtameez"]

with open("first.txt", "r") as f:
    content = f.read()
    
for word in words:    
    content = content.replace(word, "#" * len(word))

with open("first.txt", "w") as f:
    f.write(content)
    