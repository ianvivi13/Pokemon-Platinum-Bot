from PIL import ImageGrab


class PixelMatch:
    def __init__(self, x, y, r, g, b):
        self.pos = (x, y)
        self.rgb = (r, g, b)

    def test(self, image):
        return image.getpixel(self.pos) == self.rgb


def getScreenshot(window):
    if not window.isActive:
        window.activate()
    return ImageGrab.grab((window.left + 8, window.top + 31, window.right - 8, window.bottom - 8))