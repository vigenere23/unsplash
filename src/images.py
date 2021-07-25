import requests
from dataclasses import dataclass
from urllib.parse import urlparse
from mimetypes import guess_extension


@dataclass(frozen=True)
class WebImage:
    filename: str
    data: bytes


class ImageFetcher:
    def __init__(self, url: str):
        self.__url = url

    def fetch(self) -> WebImage:
        image_response = requests.get(self.__url, allow_redirects=True)

        image_id = urlparse(image_response.url).path.split('/')[-1]
        extension = guess_extension(image_response.headers['content-type'])
        filename = f'{image_id}{extension}'

        return WebImage(
            filename=filename,
            data=image_response.content
        )
