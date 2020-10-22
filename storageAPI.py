from google.cloud import storage

storage_client = storage.Client()


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    blobs = storage_client.list_blobs(bucket_name)
    counter = 0
    for blob in blobs:
        counter += 1
    return counter


def list_buckets():
    """Lists all buckets."""
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        count = list_blobs(bucket.name)
        print("Bucket {} has {} objects.".format(bucket.name, count))


list_buckets()
