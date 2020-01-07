import time, random, requests
from lxml import html

extracted_data = []

script = '''
headers = {
    ['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
    ['cookie'] = 'AKAM_CLIENTID=36acd909bb7164bbb0172771f0c89623; _gcl_au=1.1.1961937657.1575360115; gb_lang=en; gb_pipeline=GB; gb_countryCode=EE; gb_currencyCode=USD; _ga=GA1.2.1176668311.1575360116; _fbp=fb.1.1575360117095.1368458341; aff_mss_info_bak={"bak":"bak"}; landingUrl=https://www.gearbest.com/flash-sale.html; od=gzvtwgwwfkpg1575360119025; gb_vid=2b0939c6-3747-abb7-ade2-3ae56a955c46; __atuvc=1%7C49%2C0%7C50%2C0%7C1%2C1%7C52%2C6%7C2; _derived_epik=dj0yJnU9MHJBVU1oeGdBNVdHYlJsZm10ZmFyVlpfZkpKWWFjY1Ambj1VN0VPM2tzNWdRdFV3STlQTXpoOWZBJm09MSZ0PUFBQUFBRjRTMUV3JnJtPTEmcnQ9QUFBQUFGNFMxRXc; __atssc=google%3B1; ORIGINDC=3; AKA_A2=A; ak_bmsc=F028F5359CF8B73248F5588DE9632FCB17D46C37871F00002127145E386E397D~pl//CKmQeJvjsg1H548MKpTYDeJ+JB6+gFI6di7KFVMlNXfiYf3ASRbKsA3rTbdfElzBkIyuNY8GtpnJxyK1zVNHOOFp8kveUNpYuX3FfXOgEpSlsuUBQ8APzr92H1UBOlznODGKecFWV6ytxdtXfSOd3vpRrDKwn58BruSEgcyhT3RRSllSZ/I9TcQIZVGCeuQvjf4FCljQWQ8xavpyGGamEiyFqzibRUtBXnt6kbFp2W1EJasxjjfljpg+5cNopO; bm_sv=B5F276D7125934A629C9093583954B4E~WjVX93HPM0gUdgAhVAssWrSlrtzj/C/9NmHEc6B19TuSTYHE0148TdPVc3MT4dJSjTOboky+eYltJKhLLUQBrL9FN7rLT+1t0biex0EVo7TevOF5cnjoNO1TiV08WcwiD9Y9PiC18YASRdozsvvL6Hrcg1J8JldBReX1tm12d2M=; _gid=GA1.2.1733734356.1578379043; _dc_gtm_UA-48073707-1=1; WEBF_predate=1578379044; WEBF_guid=36acd909bb7164bbb0172771f0c89623_1578379044; osr_referrer=originalurl; osr_landing=https%3A%2F%2Fwww.gearbest.com%2Fflash-sale.html; gb_fcm=2; gb_fcmPipeLine=GB; cdn_countryCode=EE; gb_pf=%7B%22rp%22%3A%22originalurl%22%2C%22lp%22%3A%22https%3A%2F%2Fwww.gearbest.com%2Fflash-sale.html%22%2C%22wt%22%3A1578379044572%7D; gb2019_gb_sid_7c8e320e-2ac6-a416-b825-ab1e9a848187=false; gb2019_gb_sid=7c8e320e-2ac6-a416-b825-ab1e9a848187; gb_soa_www_session=eyJpdiI6IkxubmZXXC9rbTFZbGgwQkpRcjluK2p3PT0iLCJ2YWx1ZSI6InVLSlYwQm9uT1kzdHhPajlSWnpkdHlxdEtOdTlDWGdPc3Z0eU14VndMYXZRaGlNaytLVCtmOHNLWjBtWWZlOXVlXC9pcG5ObUNTa0ZlTEZ0dm9cL3k1V1E9PSIsIm1hYyI6ImYxOGZjMjM5M2NkYTFiM2E4ODRjNWU4NTdlOWE1M2Y1ZDQ4YmM1Zjc4NzMzNTA2NDJjNTBkNjU1OGI0MmVlOGUifQ%3D%3D; gb_vsign=6c2561a8f5e4e7820dcf58f63fbd332ef37b28cb; gb_categoryAB=D'
}
splash:set_custom_headers(headers)
splash.private_mode_enabled = false
assert(splash:go(args.url))
assert(splash:wait(1))
return splash:html()
'''

for x in range(105):

    time.sleep(random.randint(1, 7))

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
    extracted_data = []
    print("\nLoop index --------------------->>> ", x)