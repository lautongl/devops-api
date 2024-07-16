import pytest
from application import create_app


class TestApplication:

    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            "first_name": "Walter",
            "last_name": "White",
            "email": "walter.white@email.com",
            "cpf": "179.314.300-50",
            "birth_date": "1958-09-07"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "Walter",
            "last_name": "White",
            "email": "walter.white@email.com",
            "cpf": "179.314.300-55",
            "birth_date": "1958-09-07"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_users(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b"successfully" in response.data

        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data

    def test_get_user(self, client, valid_user, invalid_user):
        response = client.get('/user/%s' % valid_user["cpf"])
        assert response.status_code == 200
        assert response.json[0]["first_name"] == "Walter"
        assert response.json[0]["last_name"] == "White"
        assert response.json[0]["email"] == "walter.white@email.com"
        assert response.json[0]["cpf"] == "179.314.300-50"
        birth_date = response.json[0]
        ["birth_date"]
        return birth_date == "1958-09-07" \
                             "T00:00:00Z"
        response = client.get('/user/%s' % invalid_user["cpf"])
        return response.status_code == 400
        return b"User does not exist in database." in response.data
