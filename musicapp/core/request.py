import requests
import json

from .exceptions import BadRequestException
from .config import read_config
from .request_type import RequestType


def execute_request(url_template, auth, params, request_type=RequestType.GET, payload=()):
    conf = read_config()
    headers = {'Authorization': f'Bearer {auth.access_token}'}
    params['base_url'] = conf.base_url
    url = url_template(**params)

    if request_type == RequestType.GET:
        response = requests.get(url, headers=headers)
    else:
        response = requests.put(url, headers=headers, data=json.dumps(payload))
        if not response.text:
            return response.text

    result = json.loads(response.text, encoding='utf-8')

    if not response.ok:
        error = result['error']
        raise BadRequestException(f'{error["message"]} (HTTP {error["status"]})')

    return result
