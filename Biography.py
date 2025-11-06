dict = {
    "names": "Rian",
    "hometown": "Abu Dhabi",
    "age": 18
}
print (dict)


name = input("Enter your full name: ")        
hometown = input("Enter your hometown: ")
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Oops! Please enter a number for age next time.")
    age = None                             

person_info = {
    "Name": name,
    "Hometown": hometown,
    "Age": age
}
print(f"{person_info['Name']}\n{person_info['Hometown']}\n{person_info['Age']}")