from abc import ABC, abstractmethod
from pathlib import Path
from os import path, listdir
from shutil import rmtree
import random

from client.unsplash_request import UnsplashRequestBuilder
from commands.set.set_command_arguments import SetCommandType
from commands.config.config_repository import ConfigRepository
from commands.set.set_command_arguments import SetCommandArguments
from images import ImageFetcher, WebImage

class SetCommand(ABC):
    def __init__(
        self,
        current_wallpaper_dir: str,
        saved_wallpaper_dir: str,
        config_repo: ConfigRepository
    ):
        self.__current_wallpaper_dir = current_wallpaper_dir
        self.__saved_wallpaper_dir = saved_wallpaper_dir
        self.__config = config_repo.get()

    def execute(self, args: SetCommandArguments):
        command_type = SetCommandType.parse(args.type or self.__config.type)

        if command_type is SetCommandType.NEW:
            self.__set_new(args)
        elif command_type is SetCommandType.SAVED:
            self.__set_saved()

    def __set_new(self, args: SetCommandArguments):
        url = self.__get_url(args)
        image = self.__fetch_image(url)

        self.__recreate_current_wallpaper_directory()
        image_path = self.__save_new_wallpaper(image)

        print('   ➜ Setting new desktop wallpaper (this might cause lag)')
        self._set_new_wallpaper(image_path)

    def __set_saved(self):
        images = listdir(self.__saved_wallpaper_dir)

        if len(images) == 0:
            raise Exception("No saved images available. Please save one first with 'unsplash save'.")
        
        image = f'{random.choice(images)}'
        image_path = path.join(self.__saved_wallpaper_dir, image)

        self.__recreate_current_wallpaper_directory()

        print('   ➜ Setting new desktop wallpaper (this might cause lag)')
        self._set_new_wallpaper(image_path)

    @abstractmethod
    def _set_new_wallpaper(self, image_path: str):
        raise NotImplementedError()

    def __get_url(self, args: SetCommandArguments):
        builder = UnsplashRequestBuilder()

        builder.keyword_from(args.keywords or self.__config.keywords)
        builder.resolution(args.resolution or self.__config.resolution)

        url = builder.build()

        return url

    def __fetch_image(self, url: str):
        fetcher = ImageFetcher(url)
        
        print(f"   ➜ Downloading new wallpaper from '{url}'")

        return fetcher.fetch()

    def __recreate_current_wallpaper_directory(self):
        if path.isdir(self.__current_wallpaper_dir):
            rmtree(self.__current_wallpaper_dir)

        Path(self.__current_wallpaper_dir).mkdir(parents=True)

    def __save_new_wallpaper(self, image: WebImage):
        file_path = path.join(self.__current_wallpaper_dir, image.filename)

        with open(file_path, 'wb') as f:
            print(f"   ➜ Saving new wallpaper to '{file_path}'")
            f.write(image.data)

        return file_path
