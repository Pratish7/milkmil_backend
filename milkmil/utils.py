from google.cloud import storage

def upload_file_to_gcp(file_content, file_name):
    client = storage.Client()
    bucket = client.get_bucket('pratish')
    blob = bucket.blob('milkmil/reports/{}'.format(file_name))
    blob.upload_from_file(file_content, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


def generate_download_link(file_name):
    client = storage.Client()
    bucket = client.bucket('pratish')
    blob = bucket.blob('milkmil/reports/{}'.format(file_name))

    url = blob.generate_signed_url(
        version='v4',
        expiration=3600,
        method='GET'
    )

    return url
