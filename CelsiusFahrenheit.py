def C2F(celsius):
    if celsius<-273.15:
        return "This temperature doesnt make sense"
    else:
        fah=celsius*9/5 + 32
        return(fah)

temperature=[10,-20,-289,100]
for entry in temperature:
    print(C2F(entry))
