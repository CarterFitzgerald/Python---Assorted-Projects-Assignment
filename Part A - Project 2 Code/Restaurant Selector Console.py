vegetarian_input = str(input("Is anyone in your party a vegetarian? "))
vegan_input = str(input("Is anyone in your party a vegan? "))
gluten_free_input = str(input("Is anyone in your party gluten-free? "))

if vegetarian_input == "yes":
    vegetarian = 1
else:
    vegetarian = 0

if vegan_input == "yes":
    vegan = 1
else:
    vegan = 0

if gluten_free_input == "yes":
    gluten_free = 1
else:
    gluten_free = 0

if vegetarian == 1 and vegan == 1 and gluten_free == 1:
    result = "Here are your restaurant choices: \n" \
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen"
elif vegetarian == 1 and vegan == 1 and gluten_free == 0:
    result = "Here are your restaurant choices: \n" \
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen"
elif vegetarian == 1 and vegan == 0 and gluten_free == 1:
    result = "Here are your restaurant choices: \n" \
                     "   Main Street Pizza Company\n"\
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen"
elif vegetarian == 0 and vegan == 1 and gluten_free == 1:
    result = "Here are your restaurant choices: \n" \
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen"
elif vegetarian == 0 and vegan == 1 and gluten_free == 0:
    result = "Here are your restaurant choices: \n" \
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen"
elif vegetarian == 0 and vegan == 0 and gluten_free == 1:
    result = "Here are your restaurant choices: \n" \
                     "   Main Street Pizza Company\n" \
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen"
elif vegetarian == 1 and vegan == 0 and gluten_free == 0:
    result = "Here are your restaurant choices: \n" \
                     "   Main Street Pizza Company\n"\
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen\n"\
                     "   Mama's Fine Italian"
else:
    result = "Here are your restaurant choices: \n" \
                     "   Joe's Gourmet Burgers\n"\
                     "   Main Street Pizza Company\n"\
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen\n"\
                     "   Mama's Fine Italian"

print(result)
