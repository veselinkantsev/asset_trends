#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.count_articles import get_articles, inspect_articles
import requests

from src import config as cfg


class MockResponse:
    @staticmethod
    def raise_for_status():
        return None

    @staticmethod
    def json():
        return {
            "count": 3,
            "next": None,
            "previous": None,
            "results": cfg.TEST_SAMPLE_ARTICLES,
        }


articles = MockResponse.json()["results"]


def test_get_articles_success(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = get_articles("http://fake_url", "fake_token")
    assert result == articles


def test_inspect_articles():
    source = "fake_source"
    assert [x["assets"] for x in inspect_articles(articles, source)] == [
        ["btc"],
        ["btc"],
    ]
