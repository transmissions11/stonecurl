from touchstone_auth import TouchstoneSession, UsernamePassAuth, TwofactorType
import json
import sys

with open('credentials.json', encoding='utf-8') as f:
    config = json.load(f)

url = sys.argv[1]

with TouchstoneSession(url,
        auth_type=UsernamePassAuth(config['username'], config['password']),
        cookiejar_filename='cookiejar.pickle',
        twofactor_type=TwofactorType.DUO_PUSH,
        verbose=False) as s:
    r = s.get(url)
    print(r.text)
