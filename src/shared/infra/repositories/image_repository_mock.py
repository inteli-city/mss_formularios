from src.shared.domain.repositories.image_repository_interface import IImageRepository


class ImageRepositoryMock(IImageRepository):

    def save_image(self, base_64_image: str, image_path: str, content_type: str = 'image/png') -> None:
        pass