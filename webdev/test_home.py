import pytest
from django.urls import reverse
from django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('principal:home'))


def test_home_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Breno Eustáquio - Portifólio</title>')


def test_home_title_link(resp):
    assert_contains(resp, 'href="#page-top">Breno Eustáquio</a>')
