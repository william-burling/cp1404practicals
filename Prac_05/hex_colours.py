COLOUR_CODES = {"brown1": "#ff4040", "AntiqueWhite": "#faebd7",
                "azure3": "#c1cdcd", "cyan1": "#00ffff",
                "chocolate": "#d2691e", "DarkGoldenrod": "#b8860b",
                "AliceBlue": "#f0f8ff", "aquamarine2": "#76eec6",
                "beige": "#f5f5dc", "BlueViolet": "#8a2be2"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")
