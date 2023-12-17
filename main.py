recipes = {
        "spaghetti": ["pasta", "tomato sauce", "ground beef"],
        "salad": ["lettuce", "tomato", "cucumber", "dressing"],
        "curry":["chicken","onion","cocount milk","chili"],
        "guacamole":["avocado","lemon","cilantro"],
        "burschetta":["bread","tomatoes","pesto","parmesan"],
        "fried rice":["rice","soy sauce","egg","veggies"],
        "banana bread":["butter","banana","flour","sugar","egg","milk"],
        "loaded potatoes":["potatoe","corn","cheese","butter","cream cheese"],
        "roasted mushrooms":["mushroom","balsamic vinegar","garlic","oil"],
        "hummus":["chickpeas","tahini","yoghurt","lemon"]
    }
def get_recipe(ingredients):
    for recipe, recipe_ingredients in recipes.items():
        if set(ingredients).issubset(set(recipe_ingredients)):
            return f"Here's a {recipe} recipe: {', '.join(recipe_ingredients)}."

    return "Sorry, no matching recipe found."


def add_recipe():
    new_recipe_name = input("Enter the name of the new recipe: ")
    new_recipe_ingredients = input("Enter the ingredients (comma-separated): ").split(',')
    print(f"New recipe added: {new_recipe_name} - {', '.join(new_recipe_ingredients)}")


while True:
    user_ingredients = input("Enter the ingredient\s: ").split(',')
    recipe_result = get_recipe(user_ingredients)
    print(recipe_result)

    if "Sorry" in recipe_result:
        add_new_recipe = input("Do you want to add a new recipe? (yes/no): ").lower()
        if add_new_recipe == "yes":
            add_recipe()

    anotherIngredient = input("Do you want to enter another ingredient? (yes/no): ").lower()
    if anotherIngredient != "yes":
        break