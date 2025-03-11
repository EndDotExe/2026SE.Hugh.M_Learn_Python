fruits = [
    {"fruit": "apple", "calories": "130"},
    {"fruit": "banana", "calories": "110"},
    {"fruit": "orange", "calories": "80"},
    {"fruit": "pear", "calories": "100"},
    {"fruit": "grape", "calories": "90"},
    {"fruit": "kiwi", "calories": "90"},
    {"fruit": "strawberry", "calories": "50"},
    {"fruit": "blueberry", "calories": "80"},
    {"fruit": "watermelon", "calories": "80"},
    {"fruit": "pineapple", "calories": "50"},
    {"fruit": "peach", "calories": "60"},
    {"fruit": "plum", "calories": "70"},
    {"fruit": "cherries", "calories": "100"},
    {"fruit": "cantaloupe", "calories": "50"},
    {"fruit": "honeydew", "calories": "50"},
    {"fruit": "tangerine", "calories": "50"},
    {"fruit": "nectarine", "calories": "60"},
    {"fruit": "avocado", "calories": "50"},
    {"fruit": "grapefruit", "calories": "60"},
    {"fruit": "lemon", "calories": "15"}
    ]

def main():
    nutrents = input("What fruit? ").lower()
    for fruit in fruits:
        if nutrents == fruit["fruit"]:
            print(f"Calories: {fruit['calories']}")

main()