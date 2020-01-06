import requests
from lxml import html

extracted_data = []

script = '''
headers = {
    ['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
    ['cookie'] = 'AKAM_CLIENTID=36acd909bb7164bbb0172771f0c89623; _gcl_au=1.1.1961937657.1575360115; gb_lang=en; gb_pipeline=GB; gb_countryCode=EE; gb_currencyCode=USD; _ga=GA1.2.1176668311.1575360116; _fbp=fb.1.1575360117095.1368458341; aff_mss_info_bak={"bak":"bak"}; landingUrl=https://www.gearbest.com/flash-sale.html; od=gzvtwgwwfkpg1575360119025; gb_vid=2b0939c6-3747-abb7-ade2-3ae56a955c46; __atuvc=1%7C49%2C0%7C50%2C0%7C1%2C1%7C52%2C1%7C2; _derived_epik=dj0yJnU9T3lrc3NFVk53SmZxYkZ2M2dNV1gtNzZfVDlvZjhBWGEmbj10M0lkS3BXMkItenpES05lelI3ZDBnJm09MSZ0PUFBQUFBRjRTQldJJnJtPTEmcnQ9QUFBQUFGNFNCV0k; __atssc=google%3B1; _gid=GA1.2.1014777744.1578228610; AKA_A2=A; ak_bmsc=00F3328BAAE3B1D549A7A2DFABCBD98417D46C37871F00000BD2125E9B4DDC5F~plt/pZImzsPz/XbYidpbzR/ta6Wj4Tx9uK55OintFpyYiYw9eEHqW8oRQNw8WriUfV5zSM77l1+pX01EYmxYsBmz1UF270mWKycFrZgAnf7nzm8q9pyZY92qcID4iuQ7Sw1JCGy4zQOiTVHWRTjnr3TCqKytuXV7WueoWHo/v8bs8W49NedCUaouBT7gndjYcmSJtGuRkD/fSeqA7yZ+7LC2F9wvrTP2lQ421+/WRFDYFJ2DvGZN2/IiciLeqncTJ+; bm_sv=F215FEE1D2AFAF5000EB34D8BB9108F4~WjVX93HPM0gUdgAhVAssWv7Y5TOol/BzPjqXilmXnTo2Motkrf6PyTYGn/SwCuiHrI7cGPv2LxZV+6lfCDXgiNcMuzRbZR4ktJ4vhx2FDt5ZUSX4NgNvmpethxLmOk9m4nqx8J0RsAIAql7ZkgFzZXchs7QphnWh9hWE5V79ZFE=; _dc_gtm_UA-48073707-1=1; WEBF_predate=1578291726; WEBF_guid=36acd909bb7164bbb0172771f0c89623_1578291726; osr_referrer=originalurl; osr_landing=https%3A%2F%2Fwww.gearbest.com%2Fflash-sale.html; gb_fcm=2; gb_fcmPipeLine=GB; cdn_countryCode=EE; gb_pf=%7B%22rp%22%3A%22originalurl%22%2C%22lp%22%3A%22https%3A%2F%2Fwww.gearbest.com%2Fflash-sale.html%22%2C%22wt%22%3A1578291726672%7D; gb2019_gb_sid_089cf632-d213-a175-9c51-af53c42a266f=false; gb2019_gb_sid=089cf632-d213-a175-9c51-af53c42a266f; gb_soa_www_session=eyJpdiI6IkpuYVwvXC9xRjNaMmdkdm1GZzJVRjgrUT09IiwidmFsdWUiOiJCWnpFMVVHeDBRQ2o5QlpHTEgrUkwydUs5bHNYMDk2QzJNU0ZmZThhWlNhdFlxSUtyR2pGcjhqdGhDZmdOMTRBdFwvN2hLeENlR0VNZFE5aUVWQTZhRkE9PSIsIm1hYyI6IjJlMmMzYjY0MWYyMjFlNTc1NzU2MWE2YWUxNjVjODE1MzAyNzg5NjU2ZTI3MzU1NmUzMzg5NWQ2MWVkMWQ3ZjQifQ%3D%3D; gb_vsign=6c2561a8f5e4e7820dcf58f63fbd332ef37b28cb; ORIGINDC=4; gb_categoryAB=D'
}
splash:set_custom_headers(headers)
splash.private_mode_enabled = false
assert(splash:go(args.url))
assert(splash:wait(1))
return splash:html()
'''

resp = requests.post(url='http://splash:8050/run', json={
    'lua_source': script,
    'url': 'https://www.gearbest.com/flash-sale.html'
})


tree = html.fromstring(html=resp.content)

deals = tree.xpath("//li[contains(@class, 'goodsItem')]/div[@class='goodsItem_content']")

for deal in deals:
    product = {
        'name': deal.xpath(".//div[@class='goodsItem_title']/a/text()")[0].strip(),
        'url': deal.xpath(".//div[@class='goodsItem_title']/a/@href")[0],
        # 'original_price': deal.xpath(".//div[@class='goodsItem_delete']/del/@data-currency/")[0],
        'discounted_price': deal.xpath(".//div[@class='goodsItem_detail']/span/@data-currency")[0],
    }
    extracted_data.append(product)

print(extracted_data)