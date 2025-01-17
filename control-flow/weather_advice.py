#  Weather Recommendation Program
current_weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if current_weather == "sunny":
    print(f"It's {current_weather}, Wear a t-shirt and sunglasses.")
elif current_weather == "rainy":
    print(f"It's {current_weather}, Don't forget your umbrella and a raincoat.")
elif current_weather == "cold":
    print(f"It's {current_weather}, Make sure to wear a warm coat and a scarf")
else:
    print(f"I don't have recommendation for this weather: {current_weather}")