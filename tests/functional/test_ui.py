#!/usr/bin/env python3

import pytest
from flask import url_for


@pytest.mark.usefixtures('live_server')
class TestLiveServer():

    @pytest.mark.parametrize('page', [
        'home',
        'contact',
        'about',
        'services'
    ])
    def test_server_is_up_and_running(self, selenium, page):
        selenium.get(url_for(page, _external=True))
        assert selenium.title == 'Zapata'
