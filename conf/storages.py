from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class PublicMediaStorage(S3Boto3Storage):
    """Storage para imagens públicas no S3 com prints de debug"""
    
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = 'media'
    file_overwrite = False
    object_parameters = {
        'CacheControl': 'max-age=86400',
    }
    
    def _save(self, name, content):
        try:
            result = super()._save(name, content)
            return result
        except Exception as e:
            raise
