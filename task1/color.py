import colourise


def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


class RGB:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f'RGB({self.r}, {self.g}, {self.b})'


class Color:
    def __init__(self, name: str, rgb: RGB):
        self.name = name
        self.rgb = rgb
        self.hex = rgb_to_hex(rgb.r, rgb.g, rgb.b)


def complement(color: Color):
    comp = colourise.complement_rgb(color.rgb.r, color.rgb.g, color.rgb.b)
    return Color(color.name + " (comp)", RGB(r=int(comp[0]), g=int(comp[1]), b=int(comp[2])))
