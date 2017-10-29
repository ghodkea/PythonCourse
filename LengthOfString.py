def lengthofstring(somestring):
    try:
        output=len(somestring)
        return(output)
    except TypeError:
        output=0
        print("Length function cannot be called on Integers or Floats")
        return(output)


print(lengthofstring("Mary Had a Little Lamb"))
print(lengthofstring(10))
print(lengthofstring(10.89))
