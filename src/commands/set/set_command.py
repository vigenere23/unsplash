from abc import ABC, abstractmethod
from pathlib import Path
from os import path, listdir
from shutil import rmtree

from src.client.unsplash_request import UnsplashRequestBuilder
from src.commands.set.set_command_arguments import SetCommandArguments
from src.images import ImageFetcher, WebImage

class SetCommand(ABC):
    def __init__(self, current_wallpaper_dir: str):
        self.__current_wallpaper_dir = current_wallpaper_dir

    def execute(self, args: SetCommandArguments):
        url = self.__get_url(args)
        image = self.__fetch_image(url)

        self.__recreate_current_wallpaper_directory()
        image_path = self.__save_new_wallpaper(image)

        print('Setting new desktop wallpaper (this might cause lag)...')
        self._set_new_wallpaper(image_path)

        print('DONE!')

    @abstractmethod
    def _set_new_wallpaper(self, image_path: str):
        raise NotImplementedError()

    def __get_url(self, args: SetCommandArguments):
        builder = UnsplashRequestBuilder()

        # TODO add 'or config.X' in arguments
        builder.keyword_from(args.keywords or ['mountains'])
        builder.resolution(args.resolution or '1440p')

        url = builder.build()

        return url

    def __fetch_image(self, url: str):
        fetcher = ImageFetcher(url)
        
        print(f"Downloading new wallpaper from '{url}'...")

        return fetcher.fetch()

    def __recreate_current_wallpaper_directory(self):
        if path.isdir(self.__current_wallpaper_dir):
            rmtree(self.__current_wallpaper_dir)

        Path(self.__current_wallpaper_dir).mkdir(parents=True)

    def __save_new_wallpaper(self, image: WebImage):
        file_path = path.join(self.__current_wallpaper_dir, image.filename)

        with open(file_path, 'wb') as f:
            print(f"Saving new wallpaper to '{file_path}'...")
            f.write(image.data)

        return file_path
