person = {
    "name":"Alex",
    "age":16,
    "gender":"female"
    }
print(person["age"])

cars = ("bmw","reno","lada")

cars2 = ["mersedes","kia"]

cars2.append("honda")

hours = 17
if hours>=5 and hours<12:
   print("morning")
elif hours>12 and hours<=17:
    print("day")
elif hours >17 and hours<=21:
    print("evening")
elif hours >21 or hours <=5:
    print("night")

string = "арбуз,дыня,яблоко,апельсин"

def fruits(fruits_str):
    list_fruits = string.split(",")
    return list_fruits[0],list_fruits[-1]
fruit1,fruit2 = fruits(string)
print(fruit1)