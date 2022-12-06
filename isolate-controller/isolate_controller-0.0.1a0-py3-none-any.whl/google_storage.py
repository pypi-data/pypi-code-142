from google.cloud import storage
import os

PROJECT_ID = os.environ.get("PROJECT_ID", "isolate-dev-gorgeous-swine")

BUCKET_NAME = f"{PROJECT_ID}_scheduled_jobs"


class GoogleStorageManager:
    client: storage.Client

    def __init__(self):
        self.client = storage.Client()

    def upload_isolate_request_for_job(self, job_id: str, request: bytes):
        bucket = self.client.get_bucket(BUCKET_NAME)
        bucket.blob(job_id).upload_from_string(request)
