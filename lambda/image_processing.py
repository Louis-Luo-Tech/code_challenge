import os
import boto3
from PIL import Image
from io import BytesIO


s3 = boto3.client('s3')

def lambda_imageProcessing(event, context):
    try:
        # Parse the S3 event to get the bucket name and object key
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        # Download the image from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        image = Image.open(BytesIO(response['Body'].read()))
        
        # Generate the thumbnail
        image.thumbnail((128, 128))
        buffer = BytesIO()
        image.save(buffer, 'JPEG')
        buffer.seek(0)
        
        # Upload the thumbnail to S3
        thumbnail_key = f"thumbnails/{os.path.basename(key)}"
        s3.put_object(
            Bucket=bucket,
            Key=thumbnail_key,
            Body=buffer,
            ContentType='image/jpeg'
        )
        
        return {
            'statusCode': 200,
            'body': f"Thumbnail created successfully and stored as {thumbnail_key}"
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error processing the image: {str(e)}"
        }
