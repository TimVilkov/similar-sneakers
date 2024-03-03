COOKIES = {
    'gdprCountry': 'false',
    'visitorId': 'bdc8a7ac1c51c92fa852cfdd8570c12d6d3c3dcd902026ddef3883d7097b9517',
    'preferredLanguage': 'en',
    'exp_cognito_service': 'true',
    'one_trust_eu': 'false',
    'exp_wishlist_gql': 'false',
    'exp_desktop_pdp_image': 'false',
    'isp': 'ucom cjsc',
    '__cf_bm': '8rs1ry1JdRZE9CXNbJIGrKS9ldnUxhci7ZQmKkSys58-1709464247-1.0.1.1-NMXD53_ywRpqN5i95goR0503XL_YtHTjIPxlbLB1W3YY9UD_0WjZyvNhcsYWtjmsN_aJvqKIt0NGmy5ZIae_tA',
    'sid': '38764bdd6412ee5f41a26de1ccbbafb0',
    'lang': 'en_US',
    'country': 'ID',
    'pxcts': 'b09a4738-d94e-11ee-8f68-181c20391c95',
    '_pxvid': 'afc26189-d94e-11ee-a0fa-29e9a06ebff1',
    '_gcl_au': '1.1.546183520.1709464249',
    '_fwb': '111uSxGPbA4FnZtxXm6T6Xs.1709464249571',
    'wcs_bt': 's_15f8bbc72b9c:1709464249',
    '_px2': 'eyJ1IjoiYjA2OGY4ZDAtZDk0ZS0xMWVlLTgyZWUtMDk1YTllMTAxYmEyIiwidiI6ImFmYzI2MTg5LWQ5NGUtMTFlZS1hMGZhLTI5ZTlhMDZlYmZmMSIsInQiOjE3MDk0NjQ1NTAyMDksImgiOiI2Nzg5ODAxMjJiNjIyODRjZWZlZjE2ZDQ3YTU3NzAyYTVhNDVkYzYyMDA0YzZiMWFjN2NiNjBmN2RhODBkYmI0In0=',
    'shopping_bag': '65e45ababc3d4e6027af599a',
    '_sp_ses.c6c8': '*',
    '_sp_id.c6c8': '2ea74805-645f-49cb-adf0-02d3dfc68ad3.1709464250.1.1709464250.1709464250.1e4df9d8-1dcb-4ecc-827f-c389a148d333',
    '_pxhd': 'FNhth2MuaM-hLpjq9jcXlpAt-wmKki0H8gA4b601T/wj6NrATSOvOttdX3FqLWM0CLdA1AbWBzYbz9xr5XCbaw==:DBwafFfdsPf7LHxQzEEWBTQrtj9FGiz3UBQ2k1vpozdM3KZi2WZz7L1HGsXsIZz17QvwZjCPFHaSr7CBTWVmqiTTohneLztdXBiluDy71GU=',
    'FPGSID': '1.1709464251.1709464251.G-3L9QF4WT0T.lpa_awmJsCwkExuk3udc0g',
    '__zlcmid': '1KbmXbfumaslAAQ',
    '_fbp': 'fb.1.1709464251902.2030633000',
    '_ga': 'GA1.2.532824308.1709464250',
    '_gid': 'GA1.2.200825955.1709464253',
    '_gat': '1',
    'ab.storage.sessionId.e352e6f5-ea92-41e0-be85-df1e6a76e0b7': '%7B%22g%22%3A%22a70065c7-a353-b9ca-a6ba-ad45fc2d11f3%22%2C%22e%22%3A1709466052870%2C%22c%22%3A1709464252871%2C%22l%22%3A1709464252871%7D',
    'ab.storage.deviceId.e352e6f5-ea92-41e0-be85-df1e6a76e0b7': '%7B%22g%22%3A%2283dd37b2-1c49-f8c7-ce60-d6a3cf3c7a3a%22%2C%22c%22%3A1709464252872%2C%22l%22%3A1709464252872%7D',
    'lastRskxRun': '1709464253314',
    'rskxRunCookie': '0',
    'rCookie': 'w9hotcpmt3ba11iu2poh4ltbevnnn',
    '_tt_enable_cookie': '1',
    '_ttp': '1XzLnPm8aNwTMwzeFUyPRtW8dK8',
    '_ga_3L9QF4WT0T': 'GS1.1.1709464249.1.0.1709464283.0.0.0',
    '_dd_s': 'rum=0&expire=1709465190362&logs=1&id=55ad9d36-125b-4467-8549-2b0f9bd1b864&created=1709464248826',
}

HEADERS = {
    'authority': 'www.ssense.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'referer': 'https://www.ssense.com/en-id/men/shoes',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}


def get_params(page_number: int=1) -> dict: 
    """generate params for requests

    Args:
        page_number (int, optional): 

    Returns:
        dict: _description_
    """
    return {'page': '1',}