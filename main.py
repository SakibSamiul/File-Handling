# READING A FILE
# f = open("myfile.txt", 'r')

# text = f.read()
# print(text)
# f.close()

# WRITING A FILE
 
# f = open("myfile2.txt", 'w')

# text = f.write("I'm excited to have the opportunity to share these skills with you. Let's create something cool together!")

# f.close()

# with statement

with open("myfile.txt", 'a') as f:
    f.write("I'm excited to have the opportunity to share these skills with you. Let's create something cool together!")

