#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

import prometheus_client as prom
import requests

from src import config as cfg


def get_prices(url: str, assets: dict, currency: str) -> dict:
    """Return price in a given currency for a given asset."""

    try:
        asset_ids = [a for a in assets.keys()]
        parameters = {
            "ids": ",".join(asset_ids),
            "vs_currencies": currency,
        }
        req = requests.get(url, params=parameters)
        req.raise_for_status()
        prices = req.json()
    except requests.exceptions.RequestException as e:
        print(f"ERR: {e}")
        sleep(60)

    return prices


if __name__ == "__main__":

    # Define Prometeus metrics
    asset_price_gauge = prom.Gauge(
        f"asset_price_{cfg.CURRENCY}",
        f"Price in {cfg.CURRENCY.upper()} ",
        ["asset", "source"],
    )
    # Start Prometheus exporter
    prom.start_http_server(9126)

    # Run main loop
    while True:

        # Get asset prices
        prices = get_prices(cfg.PRICE_API_URL, cfg.ASSETS, cfg.CURRENCY)

        # Publish price metrics
        for price in prices.items():
            asset_price_gauge.labels(
                cfg.ASSETS[price[0]]["symbol"], cfg.PRICE_SOURCE
            ).set(price[1][cfg.CURRENCY])

        # Pause before next scrape
        sleep(60)
