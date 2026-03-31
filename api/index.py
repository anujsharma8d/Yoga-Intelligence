import json


def handler(request):
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Yoga Pose Classification API is running!"}),
        "headers": {
            "content-type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    }
