
import base64
from src.shared.domain.repositories.image_repository_interface import IImageRepository
from src.shared.environments import Environments
import boto3

from src.shared.helpers.errors.usecase_errors import ErrorSavingImage

class ImageRepositoryS3(IImageRepository):

    def __init__(self):
        self.client = boto3.client('s3', 
                          aws_access_key_id=Environments.get_envs().aws_access_key, 
                          aws_secret_access_key=Environments.get_envs().aws_secret_access_key
                        )

    def put_image(self, base_64_image: str, image_path: str) -> None:
        try:
            file_content = base64.b64decode(base_64_image)
            self.client.put_object(Body=file_content, Bucket=Environments.get_envs().bucket_name, Key=image_path)
        
        except Exception as e:
            raise ErrorSavingImage(e.args[0])
