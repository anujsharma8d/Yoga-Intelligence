import json
import random

class_names = [
    "Downward Dog",
    "Tree Pose",
    "Warrior I",
    "Warrior II",
    "Child Pose"
]


def _parse_request(request):
    if hasattr(request, "json") and request.json is not None:
        return request.json

    body = request.body if hasattr(request, "body") else None
    if isinstance(body, bytes):
        body = body.decode("utf-8")
    if not body:
        return {}

    return json.loads(body)


def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method not allowed. Use POST."}),
            "headers": {
                "content-type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }

    try:
        data = _parse_request(request)
        keypoints = data.get("keypoints")

        if not keypoints or len(keypoints) != 51:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid keypoints data. Expected 51 values."}),
                "headers": {
                    "content-type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                }
            }

        predicted_class = random.choice(class_names)
        confidence = random.uniform(0.7, 0.95)
        remaining_confidence = 1.0 - confidence

        predictions = {}
        for class_name in class_names:
            predictions[class_name] = confidence if class_name == predicted_class else remaining_confidence / (len(class_names) - 1)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "predicted_pose": predicted_class,
                "confidence": confidence,
                "all_predictions": predictions
            }),
            "headers": {
                "content-type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
    except Exception as error:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(error)}),
            "headers": {
                "content-type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
