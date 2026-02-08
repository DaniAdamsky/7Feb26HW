MealPrepTime: int = int(input("Enter meal prep time in mins: "))
Price: float = float(input("Enter price in ILS: "))
is_quick_service: bool = MealPrepTime < 15
is_expensive: bool = Price > 100

if is_quick_service is True and is_expensive is False:
    print("recommended")
else:
    print("not recommended")

print(is_quick_service)
print(is_expensive)