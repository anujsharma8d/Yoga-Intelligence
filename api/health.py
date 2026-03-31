import json


def handler(request):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "healthy",
            "model_loaded": False,
            "message": "Demo mode - using mock predictions"
        }),
        "headers": {
            "content-type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    }
