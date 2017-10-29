temperatures=[10,-20,-289,100]

def celsius_to_fahrenheit (celsius):
    output=celsius*9/5+32
    return(output)

file=open("TemperatureLogger.txt",'w')

for temperature in temperatures:
    if temperature > -273.15:
        fah=celsius_to_fahrenheit(temperature)
        file.write(str(fah)+"\n")
    else:
        0
file.close()
