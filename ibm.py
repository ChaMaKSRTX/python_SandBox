#Sample functions: Evaluating the BMI
#Body Mass Index (BMI).
#As you can see, the formula gets two values:

#    weight (originally in kilograms)
#    height (originally in meters)

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254 #for diiferent height measure units


def lb_to_kg(lb):
    return lb * 0.4535923 #for different weght measure units


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None #for checking the trustworthy(Validity) of the information provided

    return weight / height ** 2 #The actual formula for calculation


print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7))) #prints out the result

