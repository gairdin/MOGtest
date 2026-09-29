from unittest import mock

import pytest
import requests

from api.rickmorty import RickMortyAPI


# все тесты идут без сети: подменяю requests.get на заглушку
def test_rick_get_name():
    fake_data = {"name": "Insurance Rick"}

    with mock.patch("api.rickmorty.requests.get") as fake_get:
        fake_get.return_value.json.return_value = fake_data

        result = RickMortyAPI().get("character", 164)

    assert result["name"] == "Insurance Rick"


def test_rick_get_url():
    with mock.patch("api.rickmorty.requests.get") as fake_get:
        RickMortyAPI().get("location", 1)

    fake_get.assert_called_once_with(
        "https://rickandmortyapi.com/api/location/1",
        timeout=10,
    )


def test_timeout():
    with mock.patch("api.rickmorty.requests.get") as fake_get:
        RickMortyAPI(timeout=5).get("character", 1)

    fake_get.assert_called_once_with(
        "https://rickandmortyapi.com/api/character/1",
        timeout=5,
    )


def test_404():
    with mock.patch("api.rickmorty.requests.get") as fake_get:
        fake_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "404"
        )

        with pytest.raises(requests.exceptions.HTTPError):
            RickMortyAPI().get("character", 999)