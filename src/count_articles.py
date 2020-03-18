#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import getenv
from collections import Counter
from datetime import datetime
from hashlib import md5
from time import sleep
from typing import Generator

import prometheus_client as prom
import requests

from src import constants as cfg


def get_articles(api_url: str, api_token: str) -> list:
    """Return a list of articles from all available pages."""

    # Eventually the list of all articles
    articles = []

    # Start from page 0 (i.e. the main URL)
    next_page = api_url

    # Walk through all pages
    while next_page:
        try:
            params = {"auth_token": api_token}
            req = requests.get(next_page, params=params)
            req.raise_for_status()
            res = req.json()
            articles = articles + res["results"]
            next_page = res["next"]
            sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"ERR: {e}")
            sleep(60)
            continue

    return articles


def inspect_articles(articles: list, source: str) -> Generator[dict, None, None]:
    """Process each article from a List, returning a summary of the main article attributes. """

    for article in articles:
        if not "currencies" in article.keys():
            continue
        currencies = [c["code"].lower() for c in article["currencies"]]
        md5sum = md5(f"{source}: {article['slug']}".encode()).hexdigest()[:7]
        try:  # Date format alternates
            published_at = datetime.strptime(
                article["published_at"], "%Y-%m-%dT%H:%M:%S.%f%z"
            ).strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            published_at = datetime.strptime(
                article["published_at"], "%Y-%m-%dT%H:%M:%S%z"
            ).strftime("%Y-%m-%d %H:%M:%S")
        scraped_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        summary = {
            "id": md5sum,
            "assets": currencies,
            "source": source,
            "published_at": published_at,
            "scraped_at": scraped_at,
            "title": article["title"],
        }

        yield summary


if __name__ == "__main__":

    # Prometheus metrics
    asset_articles_gauge = prom.Gauge(
        "asset_articles_total", "Total number of articles", ["asset", "source"]
    )
    prom.start_http_server(9126)

    # Run main loop
    while True:
        # Scrape CryptoPanic articles
        articles = inspect_articles(
            get_articles(cfg.NEWS_API_URL, getenv("NEWS_API_TOKEN")), cfg.NEWS_SOURCE
        )

        # Populate a list of found assets occurences
        assets = []
        for article in articles:
            assets = assets + article["assets"]

        # Count occurrences of each asset
        count = dict(Counter(sorted(assets)))

        for asset, occurences in count.items():
            asset_articles_gauge.labels(asset, cfg.NEWS_SOURCE).set(occurences)

        # Pause before next scrape
        sleep(60)
