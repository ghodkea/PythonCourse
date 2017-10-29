File=open("FileHandling.txt",'r')
for line in File:
    print(len(line.rstrip("\n")))
File.close()
