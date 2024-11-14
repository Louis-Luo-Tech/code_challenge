from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_s3_notifications as s3_notifications,
    core,
)

class ThumbnailStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket for input images
        bucket = s3.Bucket(
            self, 
            "ImageBucket",
            versioned=True,
            removal_policy=core.RemovalPolicy.DESTROY,  # For development purposes
            auto_delete_objects=True                    # For development purposes
        )

        # Lambda function to process images
        lambda_function = _lambda.Function(
            self, 
            "ThumbnailGeneratorFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="image_processing.lambda_imageProcessing",
            code=_lambda.Code.from_asset("lambda"),
            memory_size=512,
            timeout=core.Duration.seconds(30),
            environment={
                'BUCKET_NAME': bucket.bucket_name
            }
        )

        # Grant permissions
        bucket.grant_read_write(lambda_function)

        # Add event notification
        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3_notifications.LambdaDestination(lambda_function)
        )
