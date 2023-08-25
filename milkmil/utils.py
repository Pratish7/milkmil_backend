from google.cloud import storage
from django.conf import settings
from google import auth

def upload_file_to_gcp(file_content, file_name):
    client = storage.Client()
    bucket = client.get_bucket(settings.BUCKET)
    blob = bucket.blob('milkmil/reports/{}'.format(file_name))
    blob.upload_from_file(file_content, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


def generate_download_link(file_name):
    client = storage.Client.from_service_account_json('gcp.json')
    bucket = client.bucket(settings.BUCKET)
    blob = bucket.blob('milkmil/reports/{}'.format(file_name))

    url = blob.generate_signed_url(
        version='v4',
        expiration=3600,
        method='GET'
    )

    return url


def upload_key_file_to_gcp(img_content, file_name, file_loc):
    client = storage.Client()
    bucket = client.get_bucket(settings.BUCKET)
    blob = bucket.blob('{}/{}'.format(file_loc, file_name + '.jpg'))
    blob.upload_from_string(img_content, content_type="image/jpeg")


def generate_key_download_link(file_name, file_loc):
    client = storage.Client.from_service_account_json('gcp.json')
    bucket = client.bucket(settings.BUCKET)
    blob = bucket.blob('{}/{}'.format(file_loc, file_name + '.jpg'))

    url = blob.generate_signed_url(
        version='v4',
        expiration=3600,
        method='GET'
    )

    return url
