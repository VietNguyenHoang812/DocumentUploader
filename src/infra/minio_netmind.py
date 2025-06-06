from io import BytesIO
from minio import Minio
from minio.error import S3Error

from src.core.config import MINIO_CONFIG


minio_client = Minio(
    MINIO_CONFIG['ENDPOINT'],
    access_key=MINIO_CONFIG['ACCESS_KEY'],
    secret_key=MINIO_CONFIG['SECRET_KEY'],
    secure=MINIO_CONFIG['SECURE']
)

def validate_directory(bucket_name: str, directory: str) -> None:
    """Ensure the bucket exists, creating it if necessary."""
    if not minio_client.bucket_exists(bucket_name):
        try:
            minio_client.make_bucket(bucket_name)
        except S3Error as e:
            raise Exception(f"Failed to create bucket {bucket_name}: {e}")
    
    try:
        # Upload an empty object to create the directory
        minio_client.put_object(bucket_name, directory, data=BytesIO(b''), length=0)
    except S3Error as e:
        raise Exception(f"Failed to create directory {directory} in bucket {bucket_name}: {e}")
    
def upload_file_to_minio(minio_directory: str, file_name_minio: str, file_path: str) -> None:
    try:
        bucket_name = MINIO_CONFIG['BUCKET_NAME']

        # Validate the directory and bucket
        validate_directory(bucket_name, minio_directory)
        
        # Upload the file
        object_name = f"{minio_directory}/{file_name_minio}"
        minio_client.fput_object(
            bucket_name=bucket_name,
            object_name=object_name,
            file_path=file_path
        )
    except S3Error as e:
        raise Exception(f"Failed to upload file to MinIO: {e}")
    
