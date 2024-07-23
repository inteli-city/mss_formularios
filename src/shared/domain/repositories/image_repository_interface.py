from abc import ABC


class IImageRepository(ABC):

    def put_image(self, base_64_image: str, image_path: str, content_type: str = 'image/png') -> None:
        pass