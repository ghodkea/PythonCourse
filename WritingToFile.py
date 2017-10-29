numbers = [1,2,3,4]
file = open("Numbers.txt",'w')
for number in numbers:
    file.write(str(number) + "\n")
file.close()
