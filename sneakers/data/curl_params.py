COOKIES = {
    'visitorId': '83659f608c5ac9783e496cce24fbcb7b4ca2de31c6a9af3a602dc31f61543dd7',
    'exp_cognito_service': 'true',
    'one_trust_eu': 'false',
    'preferredLanguage': 'en',
    'sid': '73b655798ae87c1e64909806174870ce',
    '_gcl_au': '1.1.2103840220.1706352310',
    '_pxvid': '23b7fc1f-bd01-11ee-bcd8-ba64af460543',
    'lang': 'en_US',
    '_fbp': 'fb.1.1706352311811.230847416',
    '_fwb': '228s8T0KSFDb3kK7P9rIERm.1706352311847',
    'rskxRunCookie': '0',
    'rCookie': '5knst6f3q8s8qka3tlqaeolrvy3zl6',
    '__zlcmid': '1K1mS7zdPIMP5kF',
    '_pin_unauth': 'dWlkPVlqZzBNak0wTURjdE1qUTFOUzAwWmpCaExXRmlPVE10TW1ZNFpXWTNOVEkxT1dFMA',
    'exp_wishlist_gql': 'false',
    'exp_desktop_pdp_image': 'false',
    'isp': 'ucom cjsc',
    'shopping_bag': '65e4589d5f9ce05985c725a7',
    '_tt_enable_cookie': '1',
    '_ttp': 'bfpgBNbjD2uK3OGlDWi2yCxzAGP',
    'wcs_bt': 's_15f8bbc72b9c:1709463739',
    'clickref': '1100lyjccSvU',
    'exp_mobile_attributes': 'true',
    'gdprCountry': 'false',
    'exp_plp_larger_images_v2': 'true',
    'pxcts': '82c1b471-f3f7-11ee-84c4-8581394c8cc7',
    'ab.storage.deviceId.e352e6f5-ea92-41e0-be85-df1e6a76e0b7': '%7B%22g%22%3A%22e170b55b-7149-dc66-5832-77906429ae9a%22%2C%22c%22%3A1706352312647%2C%22l%22%3A1712395490915%7D',
    '_gid': 'GA1.2.1759167136.1712395491',
    'country': 'ID',
    '_ga': 'GA1.2.118326064.1706352311',
    'lastRskxRun': '1712395617590',
    'ab.storage.sessionId.e352e6f5-ea92-41e0-be85-df1e6a76e0b7': '%7B%22g%22%3A%229524d156-9f1f-e96c-4a72-4280b1cfcec9%22%2C%22e%22%3A1712397417615%2C%22c%22%3A1712395490914%2C%22l%22%3A1712395617615%7D',
    '_pxhd': 'kVGv5x8CnKXO8AwdC/mzdvY7t/A/5Oj3BfrXTZA/jAqWqbidDWtrrqHHn6woTp41OQNnCPbgaD-k0qWzEmQaYQ==:YOpml-e3TbQUZKMtQmhujd-GrSsOEmvWB/abhYe53ILw2XbgeMZCYEK8zUF6b9-OWQfOmsnGEcSoTYlsEhFq2GH7G3zcPkKmj6GfuZaE7eU=',
    '_ga_3L9QF4WT0T': 'GS1.1.1712395482.11.1.1712395735.0.0.2072946932',
    '_sp_id.c6c8': '5f17a18a-6cd8-49f9-82a0-c0a843b4e1af.1706352310.6.1712396933.1710874840.f1779988-a0f5-46e7-8534-65d9c8c6af15',
    '_px2': 'eyJ1IjoiYTUxODlmMzAtZjNmNy0xMWVlLTgyMGUtODlmMTYzODk1OGFkIiwidiI6IjIzYjdmYzFmLWJkMDEtMTFlZS1iY2Q4LWJhNjRhZjQ2MDU0MyIsInQiOjE1Mjk5NzEyMDAwMDAsImgiOiI2NWI5YzQxNDY1OWRlOGE0ODgxMDQzMDA5OGIwODE3ODVkZTE1MGFkMTk3MGI1YTg5OTZmNzQ5Mjk1NGExMTE5In0=',
    '_dd_s': '',
}

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-none-match': '"36412-FjmZr4rTIcrG3OXP0OlG1+l5fsQ"',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}


def get_params(page_number: int=1) -> dict: 
    """generate params for requests

    Args:
        page_number (int, optional): 

    Returns:
        dict: _description_
    """
    return {'page': str(page_number),}