print("Hello World")
print("Go")

hours = int(input("Enter hours: "))

if 12 <= hours < 24:
    print("PM")
elif 0 <= hours < 12:
    print("AM")
else:
    print("Incorrect hours!")


