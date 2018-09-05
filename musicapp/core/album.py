from .parameter import prepare_params
from .request import execute_request


def get_album_tracks(album_id, auth, params=None):
    if album_id is None or album_id is '':
        raise AttributeError('Parameter album_id should not be empty.')

    url_template = '{basic_url}/{type}/{albumid}/{postfix}{query}'
    url_params = {
        'type': 'album',
        'albumid': album_id,
        'postfix': 'tracks',
        'query': prepare_params(params)
    }
    return execute_request(url_template, auth, url_params)
