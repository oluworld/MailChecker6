#from rfc822 import Message
#from LineReader import LineReader
from etoffiutils import quickAppend, quickWrite, true, ensure_directory_present, Fill, quickReadFunc #dumptextfile
import time, os

from mc6_config import *

def beep():
	print '\a'
	print '\a'
	print '\a'
	
#def GetAccountList():
#	return [['acct-name', 'user', 'pass', 'server', MMSPOP]]

def tt():
	R=time.strftime("%y_%m%b%d=%H%M", time.localtime(time.time()))
	return R
	
def tt2():
	R=time.strftime("%y_%m%b%d (%H%M.%S)", time.localtime(time.time()))
	return R
	
def ttp():
	R=time.strftime("%Y_%m%b%d (%H%M:%S)", time.localtime(time.time()))
	return R

def get_uidl(l):
	R=l.strip().split()[0]
##	print 'get_idl(',l,') returns', R
	return R
	
def main(acct_):
#	user, passwd, host = get_info(acct)
#	handle = login(user, passwd, host)
	
	acct, user, passwd, host, h_ = acct_
	handle = h_(acct, user, passwd, host)
	count = handle.get_message_count()

	acct_file = '%s/_uidl_map'%acct
	ttx=tt()

	ensure_directory_present(acct)
	M=[]
	try:
		M=quickReadFunc(acct_file, get_uidl, true)
	except:
		pass
	
	for each in range(1,min(76,count+1)):
		print tt2(), 'Retrieving ',each, 'of', count,
		uidl = handle.get_id(each).split()[-1:][0]
		if uidl in M:
			print 'removing this message'
			handle.remove(each)
			continue
		else:
			print ''
		st = ttp()
		resp, msg_lines, octets = handle.get_message(each)
		ft = ttp()
		tort = '%s-%s-%s'%(acct, ttx, Fill(each, '0', 4))
		z = 0
		while z==0:
			try:
				quickWrite('%s/%s-M'%(acct,tort), \
					['Tort: '+tort, \
					 'UIDL: '+uidl, \
					 'Response: '+resp, \
					 'Download-Start: '+ st, \
					 'Download-Finish: '+ ft, \
					 'Octets: '+`octets`], true)
				z=1
			except IOError, e:
				if e.errno in (2, 28): # 28 - No space on device (Win98)
					time.sleep(5)
					beep()
					z = 1
				else: raise e
		if 1:
			quickWrite('%s/%s-C'%(acct,tort), msg_lines, true)
			quickAppend(acct_file, ['%s %s'%(uidl,tort)])
#			quickAppend('%s/_tmid_map'%acct, [' '])
		handle.remove(each)
	handle.quit()
	
for acct in GetAccountList():
	main(acct)

#use map
# or lisp comps
