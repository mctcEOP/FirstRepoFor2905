# This function takes a list of ingrients and simulates making a sandwich

def build_sandwich(ingredients):
    if not ingredients:
        print("You need to choose ingredients")
        return

    print("Lets make a sandwich!")
    print("First, we grab some bread...")

    # loop each ingredient
    for i, ingredients in enumerate(ingredients, 1):
        print(f"Adding {ingredients}...")

        print("And top it with bread")

    # join ingredient

    print(f'\nCongrats! you made a {" and ".join(ingredients)} sandwich!')


def main():
    try:
        print("Welcome to sandwich maker!")
        # Get ingredients from user as a comma-seperated string
        ingredient_input = input("Enter Ingredient (seperated by comma)")
        # convert to list
        # split commas
        # remove empty space
        ingredients = [i.strip for i in ingredient_input.split(",")]
        # call build_sandwich function
        build_sandwich(ingredients)
        # add exception for errors
    except Exception as e:
        print("Error has occur")


# stardard Python Ideion to only run the main function.
if __name__ == "__main__":
    main()
