# CryptoPanic API
NEWS_SOURCE = "cryptopanic.com"
NEWS_API_URL = "https://cryptopanic.com/api/v1/posts/"
NEWS_API_TOKEN = "<< SOURCED_FROM_ENV_FILE >>"

# Coingecko API
PRICE_SOURCE = "coingecko.com"
PRICE_API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Currency to check the price in
CURRENCY = "usd"

# Assets to check the price of
ASSETS = {
    "binancecoin": {"symbol": "bnb", "name": "Binance Coin"},
    "bitcoin": {"symbol": "btc", "name": "Bitcoin"},
    "eos": {"symbol": "eos", "name": "EOS"},
    "ethereum": {"symbol": "eth", "name": "Ethereum"},
    "litecoin": {"symbol": "ltc", "name": "Litecoin"},
}

# Other
DEFAULT_SLEEP = 60

# Test data
TEST_SAMPLE_ARTICLES = [
    {
        "kind": "news",
        "domain": "ambcrypto.com",
        "source": {
            "title": "AMBCrypto",
            "region": "en",
            "domain": "ambcrypto.com",
            "path": None,
        },
        "title": "Bitcoin's increasing correlation: What's driving it?",
        "published_at": "2020-03-08T19:00:46Z",
        "slug": "Bitcoins-increasing-correlation-Whats-driving-it",
        "currencies": [
            {
                "code": "BTC",
                "title": "Bitcoin",
                "slug": "bitcoin",
                "url": "https://cryptopanic.com/news/bitcoin/",
            }
        ],
        "id": 8144352,
        "url": "https://cryptopanic.com/news/8144352/Bitcoins-increasing-correlation-Whats-driving-it",
        "created_at": "2020-03-08T19:00:46Z",
        "votes": {
            "negative": 0,
            "positive": 0,
            "important": 0,
            "liked": 0,
            "disliked": 0,
            "lol": 0,
            "toxic": 0,
            "saved": 0,
            "comments": 0,
        },
    },
    {
        "kind": "news",
        "domain": "bitcoinist.com",
        "source": {
            "title": "Bitcoinist",
            "region": "en",
            "domain": "bitcoinist.com",
            "path": None,
        },
        "title": "Bitcoin Price Consolidating, is a Big Move About to Happen?",
        "published_at": "2020-03-08T19:00:24Z",
        "slug": "Bitcoin-Price-Consolidating-is-a-Big-Move-About-to-Happen",
        "currencies": [
            {
                "code": "BTC",
                "title": "Bitcoin",
                "slug": "bitcoin",
                "url": "https://cryptopanic.com/news/bitcoin/",
            }
        ],
        "id": 8144355,
        "url": "https://cryptopanic.com/news/8144355/Bitcoin-Price-Consolidating-is-a-Big-Move-About-to-Happen",
        "created_at": "2020-03-08T19:00:24Z",
        "votes": {
            "negative": 0,
            "positive": 0,
            "important": 0,
            "liked": 0,
            "disliked": 0,
            "lol": 0,
            "toxic": 0,
            "saved": 0,
            "comments": 0,
        },
    },
    {
        "kind": "news",
        "domain": "cointelegraph.com",
        "source": {
            "title": "CoinTelegraph",
            "region": "en",
            "domain": "cointelegraph.com",
            "path": None,
        },
        "title": "Diversity and Inclusion Major Themes at Hyperledger Global Forum 2020",
        "published_at": "2020-03-08T19:00:00Z",
        "slug": "Diversity-and-Inclusion-Major-Themes-at-Hyperledger-Global-Forum-2020",
        "id": 8144358,
        "url": "https://cryptopanic.com/news/8144358/Diversity-and-Inclusion-Major-Themes-at-Hyperledger-Global-Forum-2020",
        "created_at": "2020-03-08T19:00:00Z",
        "votes": {
            "negative": 0,
            "positive": 0,
            "important": 0,
            "liked": 0,
            "disliked": 0,
            "lol": 0,
            "toxic": 0,
            "saved": 0,
            "comments": 0,
        },
    },
]

TEST_SAMPLE_PRICES = {
    "bitcoin": {"usd": 8896.01},
    "ethereum": {"usd": 238.12},
    "litecoin": {"usd": 60.61},
}

TEST_SAMPLE_ASSETS = {
    "bitcoin": {"symbol": "btc", "name": "Bitcoin"},
    "ethereum": {"symbol": "eth", "name": "Ethereum"},
    "litecoin": {"symbol": "ltc", "name": "Litecoin"},
}

TEST_SAMPLE_ASSETS_CURRENCY = "usd"
