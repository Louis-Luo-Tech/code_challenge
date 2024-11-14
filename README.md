# code_challenge
code challenge task for senior data engnieer application

## Steps

### 1. install AWS CDK

bash 
npm install -g aws-cdk

### 2. install Python Dependencies

bash 
pip install -r dependency.txt -t

### 3. bootstrap the environment

bash
cdk bootstrap

### 4.Deploy the stack

bash

cdk deploy

## Security Consideration

1. IAM Roles and Policies: Ensure that the Lambda function has only the permissions it needs (read and write access to S3).
2. S3 Bucket Policies: Restrict public access and use bucket policies to enhance security.
3. Environment Variables: Store sensitive data such as bucket names securely.

## Optional Enhancements

1. API Gateway Integration: Create a RESTful endpoint to upload images and trigger the Lambda function.
2. CloudWatch Monitoring: Set up detailed logging and alerts to track performance and errors.



