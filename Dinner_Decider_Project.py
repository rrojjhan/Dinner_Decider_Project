import json
import random

meal_data = {
  "meals": [
    {
      "id": 1,
      "name": "One Pot Beef Rice",
      "section": "meat",
      "protein": "beef",
      "veggie": None,
      "starch": "root veg",
      "toppings": ["bacon bits", "fried onion", "sesame seeds"],
      "description": "A hearty one-pot dish with tender beef and root vegetables over rice."
    },
    {
      "id": 2,
      "name": "Beef Stew",
      "section": "meat",
      "protein": "beef",
      "veggie": None,
      "starch": "grains",
      "toppings": ["fried onion", "olive oil"],
      "description": "Classic slow-cooked beef stew served over hearty grains."
    },
    {
      "id": 3,
      "name": "Snapper & Root Veggie Chowder",
      "section": "meat",
      "protein": "fish",
      "veggie": None,
      "starch": "root veg",
      "toppings": ["cheddar cheese", "olive oil"],
      "description": "Creamy chowder with fresh snapper and roasted root vegetables."
    },
    {
      "id": 4,
      "name": "Salmon & Farro Grain Bowl",
      "section": "meat",
      "protein": "fish",
      "veggie": None,
      "starch": "grains",
      "toppings": ["sesame seeds", "olive oil"],
      "description": "Pan-seared salmon fillet served over a warm farro grain bowl."
    },
    {
      "id": 5,
      "name": "Roasted Broccoli & Farro Bowl",
      "section": "veggie",
      "protein": None,
      "veggie": "broccoli",
      "starch": "grains",
      "toppings": ["cheddar cheese", "sesame seeds"],
      "description": "Oven-roasted broccoli florets served over nutty farro grains."
    },
    {
      "id": 6,
      "name": "Roasted Broccoli & Root Veggie",
      "section": "veggie",
      "protein": None,
      "veggie": "broccoli",
      "starch": "root veg",
      "toppings": ["olive oil", "sesame seeds"],
      "description": "A wholesome roasted broccoli and root vegetable medley."
    },
    {
      "id": 7,
      "name": "Corn Bread",
      "section": "veggie",
      "protein": None,
      "veggie": "corn",
      "starch": "grains",
      "toppings": ["bacon bits", "cheddar cheese"],
      "description": "Golden skillet cornbread with sweet corn baked right in."
    },
    {
      "id": 8,
      "name": "Corn & Root Veggie Chowder",
      "section": "veggie",
      "protein": None,
      "veggie": "corn",
      "starch": "root veg",
      "toppings": ["cheddar cheese", "olive oil"],
      "description": "Hearty corn chowder with roasted root vegetables."
    },
    {
      "id": 9,
      "name": "Beef & Broccoli Grain Bowl",
      "section": "both",
      "protein": "beef",
      "veggie": "broccoli",
      "starch": "grains",
      "toppings": ["bacon bits", "sesame seeds"],
      "description": "Savory beef and broccoli over farro grains."
    },
    {
      "id": 10,
      "name": "Savory Beef & Root Veggie Stir Fry",
      "section": "both",
      "protein": "beef",
      "veggie": "broccoli",
      "starch": "root veg",
      "toppings": ["fried onion", "sesame seeds"],
      "description": "Sizzling stir fry with beef and broccoli over roasted root vegetables."
    },
    {
      "id": 11,
      "name": "Street Corn Chicken Rice Bowl",
      "section": "both",
      "protein": "chicken",
      "veggie": "corn",
      "starch": "grains",
      "toppings": ["cheddar cheese", "olive oil"],
      "description": "Grilled chicken and charred street corn served over seasoned rice."
    },
    {
      "id": 12,
      "name": "Sheet Pan Roasted Chicken",
      "section": "both",
      "protein": "chicken",
      "veggie": "corn",
      "starch": "root veg",
      "toppings": ["olive oil", "sesame seeds"],
      "description": "Easy sheet pan chicken with roasted corn and root vegetables."
    },
    {
      "id": 13,
      "name": "Cereal",
      "section": "dairy",
      "protein": None,
      "veggie": None,
      "starch": "grains",
      "toppings": ["bacon bits", "fried onion"],
      "description": "A classic breakfast cereal with cold milk — breakfast for dinner!"
    },
    {
      "id": 14,
      "name": "Grilled Cheese",
      "section": "dairy",
      "protein": None,
      "veggie": None,
      "starch": "grains",
      "toppings": ["bacon bits", "fried onion"],
      "description": "Golden toasted grilled cheese sandwich with gooey melted cheese."
    },
    {
      "id": 15,
      "name": "Lasagne",
      "section": "dairy",
      "protein": None,
      "veggie": None,
      "starch": "grains",
      "toppings": ["cheddar cheese", "olive oil"],
      "description": "Layered pasta with rich meat sauce, bechamel, and melted cheese."
    },
    {
      "id": 16,
      "name": "Baked Pasta",
      "section": "dairy",
      "protein": None,
      "veggie": None,
      "starch": "grains",
      "toppings": ["cheddar cheese", "bacon bits"],
      "description": "Oven-baked pasta loaded with creamy cheese sauce and golden crust."
    }
  ],
  "toppings": ["bacon bits", "fried onion", "cheddar cheese", "olive oil", "sesame seeds"]
}

with open('meals.json', 'w') as json_file:
    json.dump(meal_data, json_file, indent=4)

print("The meal data has been successfully saved to meals.json!")

# ── Load meals from the JSON file ──────────────────────────────
def load_meals():
    with open("meals.json", "r") as file:
        data = json.load(file)
    return data["meals"]


# ── Ask questions ───────────────────────────────────────────────
def ask_section():
    print("\nChoose a food section:")
    print("  1) Meat")
    print("  2) Veggie")
    print("  3) Both")
    print("  4) Dairy")

    while True:
        choice = input("Enter 1, 2, 3, or 4: ")
        if choice == "1": return "meat"
        if choice == "2": return "veggie"
        if choice == "3": return "both"
        if choice == "4": return "dairy"
        print("Invalid — try again.")


def ask_protein():
    print("\nChoose your protein:")
    print("  1) Beef")
    print("  2) Fish")
    print("  3) Chicken")

    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1": return "beef"
        if choice == "2": return "fish"
        if choice == "3": return "chicken"
        print("Invalid — try again.")


def ask_veggie():
    print("\nChoose your vegetable:")
    print("  1) Broccoli")
    print("  2) Corn")

    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1": return "broccoli"
        if choice == "2": return "corn"
        print("Invalid — try again.")


def ask_starch():
    print("\nChoose your starch:")
    print("  1) Grains  (rice, farro, pasta)")
    print("  2) Root Veg (potato, sweet potato)")

    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1": return "grains"
        if choice == "2": return "root veg"
        print("Invalid — try again.")


def ask_toppings():
    while True:
        choice = input("\nWould you like toppings? (yes / no): ").lower()
        if choice in ("yes", "y"): return True
        if choice in ("no",  "n"): return False
        print("Please type yes or no.")


# ── Filter meals based on the user's answers ────────────────────
def filter_meals(all_meals, section, protein, veggie, starch):
    results = []

    for meal in all_meals:
        if meal["section"] != section:
            continue
        if section in ("meat", "both") and meal.get("protein") != protein:
            continue
        if section in ("veggie", "both") and meal.get("veggie") != veggie:
            continue
        if meal["starch"] != starch:
            continue
        results.append(meal)

    return results


# ── Pick one meal from the filtered list ────────────────────────
def select_meal(filtered, all_meals):
    if len(filtered) == 0:
        print("\nNo exact match — here is a random suggestion:")
        return random.choice(all_meals)
    if len(filtered) == 1:
        return filtered[0]
    print(f"\nFound {len(filtered)} matches — picking one for you!")
    return random.choice(filtered)


# ── Show the final result ───────────────────────────────────────
def display_result(meal, toppings):
    print("\n" + "─" * 40)
    print(f"Tonight's dinner: {meal['name']}")
    print(f"{meal['description']}")
    if toppings:
        print(f"Toppings: {', '.join(toppings)}")
    print("─" * 40)

    again = input("\nWant another suggestion? (yes / no): ").lower()
    return again in ("yes", "y")


# ── Main — puts everything together ────────────────────────────
def main():
    print("Welcome to Dinner Decider!")
    all_meals = load_meals()
    running = True

    while running:
        section = ask_section()

        if section == "meat":
            protein = ask_protein()
            veggie  = None
        elif section == "veggie":
            veggie  = ask_veggie()
            protein = None
        elif section == "both":
            protein = ask_protein()
            veggie  = ask_veggie()
        else:                       # dairy
            protein = None
            veggie  = None

        starch   = ask_starch()
        filtered = filter_meals(all_meals, section, protein, veggie, starch)
        chosen   = select_meal(filtered, all_meals)

        if ask_toppings():
            toppings = chosen["toppings"]
        else:
            toppings = []

        running = display_result(chosen, toppings)

    print("\nEnjoy your meal! Bon appetit!")


if __name__ == "__main__":
    main()