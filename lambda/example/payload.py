"""
Lambda payload handling
"""
import base64
import json
import urllib

def get_content(payload):
    """
    Parse incoming payload and retrieve content.
    Handles the following cases:
        - Invocation as a Python function
        - Invocation of Lambda function
        - Invocation behind an AWS HTTP v2 API Gateway
    """

    if 'body' not in payload and 'isBase64Encoded' not in payload and 'headers' not in payload:
        # Handle the direct invocation
        return payload

    content = payload['body']

    if 'isBase64Encoded' in payload:
        content = str(base64.b64decode(payload['body']), "utf-8")

    content_type = payload['headers'].get('content-type', '').lower()

    if 'application/x-www-form-urlencoded' in content_type:
        html_decoded = urllib.parse.unquote(content)
        content = urllib.parse.parse_qs(html_decoded)

    if 'application/json' in content_type:
        content = json.loads(content)

    return content
