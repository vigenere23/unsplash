from __future__ import annotations
from typing import List
from urllib.parse import quote as urlencode
import random

from client.resolution import ResolutionFactory


class UnsplashRequestBuilder:
    def __init__(self):
        self.__base_url = 'https://source.unsplash.com/featured'
        self.__keyword = 'mountains'
        self.__resolution = ResolutionFactory().create('4k')

    def keyword_from(self, keywords: List[str]) -> UnsplashRequestBuilder:
        if not keywords or len(keywords) == 0:
            raise ValueError('at least one topic must be set.')

        self.__keyword = random.choice(keywords)
        return self

    def resolution(self, resolution: str) -> UnsplashRequestBuilder:
        self.__resolution = ResolutionFactory().create(resolution)
        return self

    def build(self) -> str:
        topics = urlencode(self.__keyword)
        resolution = self.__resolution.print()

        return f'{self.__base_url}/{resolution}/?{topics}'
