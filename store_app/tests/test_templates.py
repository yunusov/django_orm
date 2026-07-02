from http import HTTPStatus

import pytest
from bs4 import BeautifulSoup
from django.urls import reverse


@pytest.mark.django_db
def test_post_list_template(client, product_1, product_2, product_3):
    """Проверим шаблон списка постов."""
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK

    soup = BeautifulSoup(response.content, "html.parser")
    titles = [h5.get_text() for h5 in soup.find_all("h5")]
    assert "product_1" in titles
    assert "product_2" in titles
    assert "product_3" in titles
