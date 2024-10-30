# 1 degrees Celsius to Fahrenheit	F = ( 9.5 × c ) + 32
def temp_converter(custemer, temp ):
        if custemer == "f":
            return ((temp * 1.8) + 32)
    
        elif custemer == "c":
            return [(temp - 32)*5/9]

