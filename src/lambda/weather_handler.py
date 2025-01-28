import json
from datetime import datetime

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'  # For CORS
        },
        'body': json.dumps({
            'message': 'Weather API version 1.0',
            'status': 'operational',
            'timestamp': datetime.utcnow().isoformat()
        })
    }