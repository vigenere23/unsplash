import requests
import subprocess
from urllib.parse import urlparse
from mimetypes import guess_extension
from pathlib import Path
from os import path, listdir
from shutil import rmtree, copyfile
from appscript import app, mactypes

from client.unsplash_request import UnsplashRequestBuilder
from commands.arguments import SetCommandArguments
from commands.command_executor import CommandExecutor


class ExecutorMacOS(CommandExecutor):
    def __init__(self):
        self.__CURRENT_WALLPAPER_DIR = path.join(Path.home(), 'Pictures', 'unsplash', 'current')
        self.__SAVED_WALLPAPERS_DIR = path.join(Path.home(), 'Pictures', 'unsplash', 'saved')

    def set(self, args: SetCommandArguments) -> None:
        builder = UnsplashRequestBuilder()

        # TODO add 'or config.X' in arguments
        builder.keyword_from(args.keywords or ['yellow flower', 'mountains', 'bike'])
        builder.resolution(args.resolution or '1440p')

        url = builder.build()
        print(f"Downloading new wallpaper from '{url}'...")

        image_response = requests.get(url, allow_redirects=True)
        image_id = urlparse(image_response.url).path.split('/')[-1]
        extension = guess_extension(image_response.headers['content-type'])

        filename = f'{image_id}{extension}'
        file_path = path.join(self.__CURRENT_WALLPAPER_DIR, filename)

        if path.isdir(self.__CURRENT_WALLPAPER_DIR):
            rmtree(self.__CURRENT_WALLPAPER_DIR)

        Path(self.__CURRENT_WALLPAPER_DIR).mkdir(parents=True)

        with open(file_path, 'wb') as f:
            print(f"Saving new wallpaper to '{file_path}'...")
            f.write(image_response.content)

        print('Setting new wallpaper... (this might lag a bit)')

        app('Finder').desktop_picture.set(mactypes.File(file_path))
        subprocess.call(['/usr/bin/killall', 'Dock'])

        print('DONE!')


    def save_current(self) -> None:
        current_wallpapers = listdir(self.__CURRENT_WALLPAPER_DIR)

        if not path.isdir(self.__SAVED_WALLPAPERS_DIR):
            Path(self.__SAVED_WALLPAPERS_DIR).mkdir(parents=True)

        for filename in current_wallpapers:
            current_file_path = path.join(self.__CURRENT_WALLPAPER_DIR, filename)
            saved_file_path = path.join(self.__SAVED_WALLPAPERS_DIR, filename)
            copyfile(current_file_path, saved_file_path)
