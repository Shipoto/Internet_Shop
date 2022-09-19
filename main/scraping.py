from decimal import Decimal

import requests
from bs4 import BeautifulSoup

from shop.models import Product


class ScrapingError(Exception):
    pass


class ScrapingTimeoutError(ScrapingError):
    pass


class ScrapingHTTPError(ScrapingError):
    pass


class ScrapingOtherError(ScrapingError):
    pass


def scraping():
    '''
    Scraping HTML text from web site
    :return: text of HTML
    '''
    URL_SCRAPING = 'https://www.citilink.ru/catalog/televizory/?sorting=price_asc'
    try:
        resp = requests.get(URL_SCRAPING, timeout=10.0)
    except requests.exceptions.Timeout:
        raise ScrapingTimeoutError("request timed out")
    except Exception as e:
        raise ScrapingOtherError(f'{e}')

    if resp.status_code != 200:
        raise ScrapingHTTPError(f"HTTP {resp.status_code}: {resp.text}")

    if resp.status_code != 200:
        raise Exception('http error access!')
    return resp


def souping():
    """
    Inserting "name of product", "code of product", "price" and "image"
    from all item on current page.
    :return: List of dictionaries.
    """
    data_list = {}
    html = scraping().text
    soup = BeautifulSoup(html, 'html.parser')
    soup_item = soup.find_all('div', class_='product_data__gtm-js product_data__pageevents-js ProductCardHorizontal '
                                            'js--ProductCardInListing js--ProductCardInWishlist')
    for item in soup_item:

        title = item.find('a', class_="ProductCardHorizontal__title Link js--Link Link_type_default")['title']
        data_list['name'] = title

        code = item['data-product-id']
        data_list['code'] = code

        price = item['data-price']
        price = Decimal(price)
        data_list['price'] = price

        picture_link = item.find('picture',
                                 class_="ProductCardHorizontal__picture "
                                        "js--ProductCardInListing__picture").find("source")['srcset']
        data_list['image_url'] = picture_link

        if not Product.objects.filter(code=data_list['code']).exists():
            Product.objects.create(
                name=data_list['name'],
                code=data_list['code'],
                price=data_list['price'],
                image_url=data_list['image_url'],
            )
    return data_list


if __name__ == '__main__':
    souping()
