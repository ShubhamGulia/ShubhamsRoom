# writing it to a new file or can edit to the existing file
fw=open("shubhamsample.txt",'w')
fw.write("Hi how are you\n")
fw.write("See you soon\n")
fw.close()

# reading it from a old file

fr=open("shubhamsample.txt",'r')

# to write the data on the output scree we will have to store th saved data to variable

text=fr.read()

print(text)

fr.close()
#NEVER FORGET TO CLOSE THE OPEN FILE