#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.check_prices import get_prices
import requests

from src import config as cfg


class MockResponse:
    @staticmethod
    def raise_for_status():
        return None

    @staticmethod
    def json():
        return cfg.TEST_SAMPLE_PRICES


def test_get_prices_success(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = get_prices(
        cfg.PRICE_API_URL, cfg.TEST_SAMPLE_ASSETS, cfg.TEST_SAMPLE_ASSETS_CURRENCY
    )
    assert result == cfg.TEST_SAMPLE_PRICES
