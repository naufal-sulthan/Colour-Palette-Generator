from PIL import Image


def image_to_color_palette(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = list(img.getdata())

    palette = sorted(set(pixels))
    palette = palette[:5]

    return palette


def get_palette_colours(image_path):
    palette = image_to_color_palette(image_path)

    return palette


# usage
palette_colours = get_palette_colours("Many Colorfull Hot Air Balloons.png")

for i, color in enumerate(palette_colours):
    print(f"Color {i + 1}: {color}")
