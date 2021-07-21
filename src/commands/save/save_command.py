from os import path, listdir
from pathlib import Path
from shutil import copyfile


class SaveCommand:
    def __init__(self):
        # TODO inject
        self.__current_wallpaper_dir = path.join(Path.home(), 'Pictures', 'unsplash', 'current')
        self.__saved_wallpapers_dir = path.join(Path.home(), 'Pictures', 'unsplash', 'saved')

    def execute(self):
        current_wallpapers = listdir(self.__current_wallpaper_dir)

        if not path.isdir(self.__saved_wallpapers_dir):
            Path(self.__saved_wallpapers_dir).mkdir(parents=True)

        for filename in current_wallpapers:
            current_file_path = path.join(self.__current_wallpaper_dir, filename)
            saved_file_path = path.join(self.__saved_wallpapers_dir, filename)
            copyfile(current_file_path, saved_file_path)
