import requests
from lxml import html

extracted_data = []

script = '''
headers = {
    ['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
    ['cookie'] = 'AKAM_CLIENTID=36acd909bb7164bbb0172771f0c89623; _gcl_au=1.1.1961937657.1575360115; gb_lang=en; gb_pipeline=GB; gb_countryCode=EE; gb_currencyCode=USD; _ga=GA1.2.1176668311.1575360116; _fbp=fb.1.1575360117095.1368458341; aff_mss_info_bak={"bak":"bak"}; landingUrl=https://www.gearbest.com/flash-sale.html; od=gzvtwgwwfkpg1575360119025; gb_vid=2b0939c6-3747-abb7-ade2-3ae56a955c46; __atuvc=1%7C49%2C0%7C50%2C0%7C1%2C1%7C52%2C1%7C2; _derived_epik=dj0yJnU9T3lrc3NFVk53SmZxYkZ2M2dNV1gtNzZfVDlvZjhBWGEmbj10M0lkS3BXMkItenpES05lelI3ZDBnJm09MSZ0PUFBQUFBRjRTQldJJnJtPTEmcnQ9QUFBQUFGNFNCV0k; __atssc=google%3B1; ORIGINDC=4; gb_soa_www_session=eyJpdiI6Inoxd0kycTU0a05XTVd3UFNreklBbkE9PSIsInZhbHVlIjoiSkZhSmJTaDIwRjFCbndjVkZQdHdwbWJMUEVzdXpkblpcLzZCTjZzSmNFT21aTFRTQktJY3RYbG44K1paMUhwQ0swenFEVVVKbHBkcDNyZXJcL2NkZXJGUT09IiwibWFjIjoiY2E3ZGE3NjlhMjc2MGM2NGE5YTUyMWRhZDQ1NjEyMDFiOGI0MGYwZjZkODRhOTE0NjNlZDlhYjcwZGQ4MGEwOCJ9; gb_vsign=6c2561a8f5e4e7820dcf58f63fbd332ef37b28cb; _gid=GA1.2.1014777744.1578228610; osr_referrer=originalurl; osr_landing=https%3A%2F%2Fwww.gearbest.com%2Fcommunity; gb_fcm=2; gb_fcmPipeLine=GB; cdn_countryCode=EE; gb_pf=%7B%22rp%22%3A%22originalurl%22%2C%22lp%22%3A%22https%3A%2F%2Fwww.gearbest.com%2F%22%2C%22wt%22%3A1578239334465%7D; AKA_A2=A; WEBF_predate=1578239334; WEBF_guid=36acd909bb7164bbb0172771f0c89623_1578239330; ak_bmsc=249DCD5044D91A99B1A1C29F1CD6A10C6007333FB25E00006205125E66300834~plWoZM7Wn1QW3dawbq2IwB9VHSIo76QeujU0Lwe/uhBvU2/xNLj4PNmG/A7306jxmH4zxTcgwhwP+TYEhlTyNZ/TMI88cIKSi1rZTkG1wKtKOCI+ErCWAA7s5BniXY5QdY8t/8uI/MJwd/YgiTvNLbBIQJoOtQVNqkWhPWcYuMoW1rQiWU5CdPlFueH7YhYUteNZspDwjCX7KWVwBjhCeRtdZpiMeCpovPuu8C2PJnAPEDkGz03rerLtQgRfUizBRr; gb2019_gb_sid=4e6f913f-9a30-acce-945a-d02116d0d61f; bm_sv=3F98EF592B490E1603EB99D020AA5DA6~HJaTuTotT/2UDojtP+0olA/V+vLMq6f2oofJClCTXX9u7F3bdtF8kMLOnxEdEAEXd/aIdk/GSyj7MO4Q2npmq/SJU0iBVC/wYXw6714OrvPPpP4Cy0LashQX7SDyngxeevNAAdYj/A67iPNjj4cMnDODMDDgrVKUILS9Wg8mXl4=; gb_categoryAB=D; bm_mi=22CAC2671265EA12D826BDD4B670C24D~GvHED7bCbNb71I4eE5aCTQZs4Gc/sPq8qm7/jazr1ZRVFJw/oTc4K/RzkysHGxAJZEjP/eoONZv10yLwYw9eEvmqRbh1aYWJQDGeH7c+jnE0+7Hj5O6G9WquMyPoBKQfy52cewNbsclaIR0v9TSsJqQjMRHLn9H3/y7LkhsHdny/0SuEg1v/25f4nJTygYdr/cj+J0KbF8+ovKbkvdSLbQAptU0HhjICXjUZ8WDMAsUNSxxMbSEYVjdQwO07w88IKHjta7qWKp7oTIzmh0YJNQbGbQkn8OOnnO0Nv3HSXa0=; gb2019_gb_sid_4e6f913f-9a30-acce-945a-d02116d0d61f=false; gb_userinfo=eyJ1c2VyIjp7InVzZXJOYW1lIjoiIiwiZW1haWwiOiIiLCJhdmF0YXIiOiIiLCJpc05ld1VzZXIiOjAsInVzZXJJZCI6IjAifSwiY29sbGVjdCI6MCwiY2FydENvdW50IjowLCJpc0xvZ2luIjpmYWxzZSwidGlja2V0Q291bnQiOjAsInNpdGVNZXNzYWdlVGltZUludGVydmFsIjowfQ%3D%3D'
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