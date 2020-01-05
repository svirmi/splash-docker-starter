import requests

script = '''
splash.private_mode_enabled = false
assert(splash:go(args.url))
assert(splash:wait(1))
return splash:html()
'''

resp = requests.post(url='http://splash:8050/run', json={
    'lua_source': script,
    'url': 'https://facebook.com/'
})

print(resp.content)