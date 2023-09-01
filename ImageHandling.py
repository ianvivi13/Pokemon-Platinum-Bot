class PixelMatch:
    def __init__(self, x, y, r, g, b):
        self.pos = (x, y)
        self.rgb = (r, g, b)

    def test(self, image):
        return image.getpixel(self.pos) == self.rgb
