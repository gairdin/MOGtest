from unittest import mock

from api.rickmorty import RickMortyAPI


def test_rickmorty():
    fake_json = {'name': 'Insurance Rick'}

    with mock.patch('api.rickmorty.requests.get') as mock_get:
        mock_get.return_value.json.return_value = fake_json

        result = RickMortyAPI().get('character', 164)

    assert result['name'] == 'Insurance Rick'
    mock_get.assert_called_once_with(
        'https://rickandmortyapi.com/api/character/164',
        timeout=10,
    )