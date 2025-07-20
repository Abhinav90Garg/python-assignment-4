cont1=""
cont2=""
try:
    file = open('sample.txt', 'r')
    cont1=file.readline()
    cont2=file.readline()
    print("Reading file content :")
    print("Line 1:", cont1, "\nLine 2:", cont2)
except FileNotFoundError :
 print("Error: the file 'sample.txt' was not found ")
