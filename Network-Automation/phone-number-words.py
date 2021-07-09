# Program to print phone number in words
# Example : 1234 = One Two Three Four
digits_mapping = {
                "1": "One",
                "2": "Two",
                "3": "Three",
                "4": "Four",
                "5": "Five",
                "6": "Six",
                "7": "Seven",
                "8": "Eight",
                "9": "Nine",
                }
phone = input("phone:")
output = ""
for ch in phone:
   output += digits_mapping.get(ch, "!") + "  "
print(f'phone_number in words: {output}')



