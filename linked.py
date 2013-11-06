#!/usr/bin/python
#encoding:utf-8

from linkedin import linkedin
import requests

API_KEY = ''
API_SECRET = ''
RETURN_URL = 'http://localhost:8000'

print linkedin.PERMISSIONS.enums.values()

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())

print 'Open this url in your browser:\n\n' + authentication.authorization_url + '\n'

authentication.authorization_code = raw_input('Insert the actually url on your address bar:\n\n').split('?')[1].split('&')[0].split('=')[1]

authentication.get_access_token()

application = linkedin.LinkedInApplication(authentication)

print '\n'

print application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'wedding planners'})
