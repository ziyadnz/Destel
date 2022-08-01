""" 
This is for cleaning extra lines in vimeo video subtitle. After run this it gives you a clean txt file
 """
file = open('subtitle1.txt')
  
# read the content of the file opened
content = file.readlines()
f = open("subtitle2.txt", "a")

# read 10th line from the file
index=3
string=""
for line in content:
    try:
        string+=content[index].rstrip()
        index+=4
    except:
        f.write(string)
        f.close()
        break