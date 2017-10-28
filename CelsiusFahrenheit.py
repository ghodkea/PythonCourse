def C2F(celsius):
    fah=celsius*9/5 + 32
    return(fah)

temperature=float(input("Enter temperature in Celsius: "))
output=C2F(temperature)
print(output)
