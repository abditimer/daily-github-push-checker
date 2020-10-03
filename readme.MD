# Github Daily Push Checker
This python script, deployed on AWS Lambda, checks on a daily basis whether you have uploaded to github or not.

## Overview

![overview img](/overview.png)

The simple overview of this system:
1. The Code gets started by AWS CloudWatch on a daily basis
1. AWS runs the serverless AWS Lambda code
1. This runs our python code, which checks the last time we pushed to our github repo
1. If we have pushed in the last 24 hours
    1. The system does not do anything - Good job!
1. If you have not pushed code in the last 24 hours
    1. It sends you an email to remind you

In order to develop this automated python system, I utilised the free tier in AWS.

# Resources to help guide your implementation
1. Sending emails using [AWS SNS](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-send-email-ses/)
1. Understand more about [AWS Lambdas serverless tech](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html)
1. Deploying extra [python modules alongside your code](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html)
    1. *I had trouble using the python request module, the guide above shows how to push it to your aws lambda function alongside your code*
1. Here is a guide on using AWS via your [CLI](https://aws.amazon.com/cli/) 
