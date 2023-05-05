# k = killo, lb = pound, f = 0.45359237
# k = lb*f

# print("This is a Pound(lb) to Killo-gram(kg) converter. \n")
# pound = float(input("What is your weight in Pound? "))
# formula = 0.45359237
# #  output = "This is your weight in Killo-grams: "
# print("Your weight in Killo-grams is: ", + pound * formula)

pound = float(input("What is your weight in pound? "))
killo = pound * 0.45359237
if killo <= 50:
    print("Your weight in killo:", killo, "\nYou're underweight!")
elif 86 <= killo <= 108:
    print("Your weight in killo:", killo, "\nYou're overweight!")
elif killo >= 109:
    print("Your weight in killo:", killo, "\nYou're obese!")
else:
    print("Your weight in killo:", killo, "\nYou're in good shape!")
# If there are more than one "if" in a statement then use "elif" = "else if" and end it with "else"
