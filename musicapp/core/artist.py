from .parameter import prepare_params
from .request import execute_request


def get_artist_albums(artist_id, auth, params=None):
    if artist_id is None or artist_id is '':
        raise AttributeError('Parameter artist_id should not be empty')

    url_template = '{base_url}/{type}/{artistid}/{postfix}{query}'
    url_params = {
        'type': 'artist',
        'artistid': artist_id,
        'postfix': 'albums',
        'query': prepare_params(params)
    }
    return execute_request(url_template, auth, url_params)
