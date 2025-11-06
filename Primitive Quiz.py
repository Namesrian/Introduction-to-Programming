questions = {
    "France": "Paris",
    "Sweden": "Stockholm",
    "United Kingdom": "London",
    "Norway": "Oslo",
    "Germany": "Berlin",
    "Ukraine": "Kyiv",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Ireland": "Dublin",
    "Portugal": "Lisbon"
   
}
for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ")

    if answer.strip().lower() == capital.lower():
        print("Correct!\n")
    else:
        print(f"Wrong! The capital of {country} is {capital}.\n")