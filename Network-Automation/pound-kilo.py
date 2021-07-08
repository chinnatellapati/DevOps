# Convert weight from Pound to Kilo grams

weight = int(input("Weight : \n"))
units = input("lbs(L) or Kgs(K)")
if (units.upper()) == "L":
    converted = weight * 0.45
    print(f'You are {converted} killo grams')
else:
    converted = weight / 0.45
    print(f'You are {converted} Pounds ')


