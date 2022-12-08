import boto3
import base64
import json


def s3UploadGenURL(b64EncodedData, s3_file, bucket_name):
    s3 = boto3.client('s3')
    img = base64.b64decode(b64EncodedData)
    try:
        s3.put_object(
            Bucket=bucket_name, Key=s3_file, Body=img)
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket_name,
                'Key': s3_file
            },
        )

        print("Upload Successful", url)
        return json.dumps({"img_url": url})
    except FileNotFoundError:
        print("The file was not found")
        return None
