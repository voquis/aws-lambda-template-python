"""
Payload parsing unit tests
"""

import json
from example import payload

EVENT_DATA = {
    'key': 'value'
}

def test_payload_parse_invoke_direct():
    """
    Test directly invoked lambda function returns original payload
    """

    assert payload.get_content(EVENT_DATA) == EVENT_DATA

def test_payload_parse_invoke_lambda():
    """
    Test invoked lambda payload is parsed as JSON
    """

    event = {
        'body': json.dumps(EVENT_DATA),
        'headers': {
            'content-type': 'application/json'
        }
    }

    assert payload.get_content(event) == EVENT_DATA
