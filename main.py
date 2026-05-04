import json

meal_data = {
  "meals": [
    {
      "id": 1,
      "name": "One Pot Beef Rice",
      "section": "meat",
      "protein": "beef",
      "veggie": None,
      "starch": "root veg",
      "toppings": [
        "bacon bits",
        "fried onion",
        "sesame seeds"
      ],
      "description": "A hearty one-pot dish with tender beef and root vegetables over rice."
    },
    {
      "id": 2,
      "name": "Beef Stew",
      "section": "meat",
      "protein": "beef",
      "veggie": None,
      "starch": "grains",
      "toppings": [
        "fried onion",
        "olive oil"
      ],
      "description": "Classic slow-cooked beef stew served over hearty grains."
    },
    {
      "id": 3,
      "name": "Snapper & Root Veggie Chowder",
      "section": "meat",
      "protein": "fish",
      "veggie": None,
      "starch": "root veg",
      "toppings": [
        "cheddar cheese",
        "olive oil"
      ],
      "description": "Creamy chowder with fresh snapper and roasted root vegetables."
    },
    {
      "id": 4,
      "name": "Salmon & Farro Grain Bowl",
      "section": "meat",
      "protein": "fish",
      "veggie": None,
      "starch": "grains",
      "toppings": [
        "sesame seeds",
        "olive oil"
      ],
      "description": "Pan-seared salmon fillet served over a warm farro grain bowl."
    },
    {
      "id": 5,
      "name": "Roasted Broc & Farro Bowl",
      "section": "veggie",
      "protein": None,
      "veggie": "broc",
      "starch": "grains",
      "toppings": [
        "cheddar cheese",
        "sesame seeds"
      ],
      "description": "Oven-roasted broccoli florets served over nutty farro grains."
    },
    {
      "id": 6,
      "name": "Roasted Broc & Root Veggie",
      "section": "veggie",
      "protein": None,
      "veggie": "broc",
      "starch": "root veg",
      "toppings": [
        "olive oil",
        "sesame seeds"
      ],
      "description": "A wholesome roasted broccoli and root vegetable medley."
    },
    {
      "id": 7,
      "name": "Corn Bread",
      "section": "veggie",
      "protein": None,
      "veggie": "corn",
      "starch": "grains",
      "toppings": [
        "bacon bits",
        "cheddar cheese"
      ],
      "description": "Golden skillet cornbread with sweet corn baked right in."
    },
    {
      "id": 8,
      "name": "Corn & Root Veggie Chowder",
      "section": "veggie",
      "protein": None,
      "veggie": "corn",
      "starch": "root veg",
      "toppings": [
        "cheddar cheese",
        "olive oil"
      ],
      "description": "Hearty corn chowder with roasted root vegetables."
    },
    {
      "id": 9,
      "name": "Beef & Broc Grain Bowl",
      "section": "both",
      "protein": "beef",
      "veggie": "broc",
      "starch": "grains",
      "toppings": [
        "bacon bits",
        "sesame seeds"
      ],
      "description": "Savory beef and broccoli over farro grains."
    },
    {
      "id": 10,
      "name": "Savory Beef & Root Veggie Stir Fry",
      "section": "both",
      "protein": "beef",
      "veggie": "broc",
      "starch": "root veg",
      "toppings": [
        "fried onion",
        "sesame seeds"
      ],
      "description": "Sizzling stir fry with beef and broccoli over roasted root vegetables."
    },
    {
      "id": 11,
      "name": "Street Corn Chicken Rice Bowl",
      "section": "both",
      "protein": "chick",
      "veggie": "corn",
      "starch": "grains",
      "toppings": [
        "cheddar cheese",
        "olive oil"
      ],
      "description": "Grilled chicken and charred street corn served over seasoned rice."
    },
    {
      "id": 12,
      "name": "Sheet Pan Roasted Chicken",
      "section": "both",
      "protein": "chick",
      "veggie": "corn",
      "starch": "root veg",
      "toppings": [
        "olive oil",
        "sesame seeds"
      ],
      "description": "Easy sheet pan chicken with roasted corn and root vegetables."
    },
    {
      "id": 13,
      "name": "Cereal",
      "section": "dairy",
      "protein": None,
      "veggie": None,
      "starch": "grains",
      "dairy_type": "breakfast",
      "dairy_sub": "milk",
      "toppings": [
        "bacon bits",
        "fried onion"
      ],
      "description": "A classic breakfast cereal with cold milk — breakfast for dinner!"
    },
    {
      "id": 14,
      "name": "Grilled Cheese",
      "section": "dairy",
      "protein": None,
      "veggie": None,
      "starch": "grains",
      "dairy_type": "breakfast",
      "dairy_sub": "cheese",
      "toppings": [
        "bacon bits",
        "fried onion"
      ],
      "description": "Golden toasted grilled cheese sandwich with gooey melted cheese."
    },
    {
      "id": 15,
      "name": "Lasagne",
      "section": "dairy",
      "protein": None,
      "veggie": None,
      "starch": "grains",
      "dairy_type": "dinner",
      "dairy_sub": "milk",
      "toppings": [
        "cheddar cheese",
        "olive oil"
      ],
      "description": "Layered pasta with rich meat sauce, bechamel, and melted cheese."
    },
    {
      "id": 16,
      "name": "Baked Pasta",
      "section": "dairy",
      "protein": None,
      "veggie": None,
      "starch": "grains",
      "dairy_type": "dinner",
      "dairy_sub": "cheese",
      "toppings": [
        "cheddar cheese",
        "bacon bits"
      ],
      "description": "Oven-baked pasta loaded with creamy cheese sauce and golden crust."
    }
  ],
  "toppings": [
    "bacon bits",
    "fried onion",
    "cheddar cheese",
    "olive oil",
    "sesame seeds"
  ]
}


#Write JSON file for creating a JSON file in Python
with open('meals.json', 'w') as json_file:
    json.dump(meal_data, json_file, indent = 4  )

print(f"The meal data has been successfully save to meals.json!")


# Make functions to handle the user's choices

"""FUNCTION ask_section():
    Display 'Choose a food section:'
    Display '1) Meat   2) Veggie   3) Both   4) Dairy'
 
    WHILE True:
        choice  ←  get input from user
        IF choice is '1': RETURN 'meat'
        IF choice is '2': RETURN 'veggie'
        IF choice is '3': RETURN 'both'
        IF choice is '4': RETURN 'dairy'
        ELSE: display 'Invalid — please enter 1, 2, 3, or 4'
"""
choice_order = ()

def ask_section():
    print('Choose a food section:')
    print('1) Meat   2) Veggie   3) Both   4) Dairy')
    while True:
        # Ask for the user's choices
        choice = input("Enter choice (1 -4): ").strip()
  
        # Return each choice the user picks.
        if choice == '1':
            
            return 'meat'
        elif choice == '2':
            return 'veggie'
        elif choice == '3':
            return 'both'
        elif choice == '4':
            return 'dairy'
        else:
            print('Invalid — please enter 1, 2, 3, or 4')

def ask_protein():
    print("Choose a protein:")
    print("1) Beef  2) Fish ")
    while True:
        choice = input("Enter choice (1-2): ").strip()
        if choice == '1': return 'beef'
        if choice == '2': return 'fish'
        #if choice ==  None : return None
        print("Invalid — please enter 1 or 2")

def ask_veggie():
    print("Choose a vegetable:")
    print("1) Broc   2) Corn")
    while True:
        choice = input("Enter choice (1-2): ").strip()
        if choice == '1': return 'broc'
        if choice == '2': return 'corn'
        print("Invalid — please enter 1 or 2")

def ask_starch():
    print("Choose a starch:")
    print("1) Grains   2) Root Veg")
    while True:
        choice = input("Enter choice (1-2): ").strip()
        if choice == '1': return 'grains'
        if choice == '2': return 'root veg'
        print("Invalid — please enter 1 or 2")

def ask_toppings():
    print("Would you like extra toppings?")
    print("1) Yes   2) No")
    while True:
        choice = input("Enter choice (1-2): ").strip()
        if choice == '1': return True
        if choice == '2': return False
        print("Invalid — please enter 1 or 2")
    
    

