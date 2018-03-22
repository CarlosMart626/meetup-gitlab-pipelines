import requests


def test_admin_url():
    r = requests.get('https://api.github.com/events')
    assert r.status_code == 200