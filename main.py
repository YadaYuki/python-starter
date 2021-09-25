import requests


def hoge(a: int) -> str:
    return ""


print(
    requests.get(
        "https://brightechshop.com/products/ambience-solar-1w?variant=8038410879012"
    ).text
)
