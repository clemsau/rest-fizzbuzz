import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status

from tests.utils import make_params


@pytest.mark.django_db
def test_query_parameter_missing():
    params = make_params(
        int1=3,
        int2=5,
        limit=10,
        string1="fizz",
    )

    client = Client()
    response = client.get(reverse("my-fizz-buzz") + "?" + params)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_invalid_query_parameter():
    params = make_params(int1=3, int2=5, limit="fuzz", string1="fizz", string2="buzz")

    client = Client()
    response = client.get(reverse("my-fizz-buzz") + "?" + params)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
