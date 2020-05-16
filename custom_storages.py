from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
# From the code along for the e-commerce from Code institute.

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION