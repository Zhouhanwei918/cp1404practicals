COLOUR_TO_CODE = {"Absolute Zero": "#0048ba",
                 "Acid Green": "#b0bf1a",
                 "AliceBlue": "#f0f8ff",
                 "Alizarin crimson": "#e32636",
                 "Amaranth": "#e52b50",
                 "Amber": "#ffbf00",
                 "Amethyst": "#9966cc",
                 "AntiqueWhite": "	#faebd7",
                 "Apricot": "#fbceb1",
                 "Aqua": "#00ffff"}


print(COLOUR_TO_CODE)

while True:
    choose_color = input("Choose color: ").capitalize()
    if choose_color in COLOUR_TO_CODE:
        print("The color code for", choose_color, "is", COLOUR_TO_CODE[choose_color])
    else:
        print("Invalid color name. Please try again.")
