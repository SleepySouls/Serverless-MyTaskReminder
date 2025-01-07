import boto3
import json
import os

sns = boto3.client("sns")

SNSTopicArn = os.environ['SNSTopicArn']

def lambda_handler(event, context):
    print("Event: ", json.dumps(event, indent=2))

    # Replace with your SNS topic ARN
    sns_topic_arn = SNSTopicArn  # Update with your topic ARN

    # Extract email from the Cognito event (user attributes)
    email = event["request"]["userAttributes"].get("email")

    if not email:
        print("No email found in user attributes.")
        raise ValueError("Failed to subscribe user to SNS topic: No email provided.")
    
    try:
        # Subscribe the user to the SNS topic
        response = sns.subscribe(
            Protocol="email",  # Specify protocol (e.g., email, SMS)
            TopicArn=sns_topic_arn,
            Endpoint=email,
        )

        print("Successfully subscribed user to SNS topic: ", response)

    except Exception as e:
        print("Error during SNS subscription: ", str(e))
        raise ValueError("SNS subscription failed.") from e

    # Return the event to continue the sign-up flow
    return event
