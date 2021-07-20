class Resolution:
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def print(self):
        return f'{self.__width}x{self.__height}'

    def __str__(self):
        return self.print()

    def __repr__(self):
        return self.print()


class ResolutionFactory:
    def create(self, resolution: str) -> Resolution:
        resolution = resolution.lower().strip()

        if resolution== '8k':
            return Resolution(7680, 4320)
        if resolution == '4k':
            return Resolution(3840, 2160)
        if resolution == '2k':
            return Resolution(2048, 1080)

        if resolution == '1440p':
            return Resolution(2560, 1440)
        if resolution == '1080p':
            return Resolution(1920, 1080)
        if resolution == '720p':
            return Resolution(1280, 720)
        if resolution == '480p':
            return Resolution(852, 480)

        try:
            width, height = resolution.split('x')
            return Resolution(width, height)
        except ValueError:
            raise Exception("resolution should be in the form '<width>x<height>' or one of the predetermined standard resolutions.")
