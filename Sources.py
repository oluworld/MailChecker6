
class MMSPOP:
	def __init__(self, acct, user, passwd, host):
		from poplib import POP3
		print '>> CONNECT',host
		H=POP3(host)
		#H._debugging=10
		print '>> USER',user
		ur=H.user(user)
		print '<<',ur
		print '>> PASS *****'
		pr=H.pass_(passwd)
		print '<<',pr
		print '++ logged in !! '
		self.H = H
	def get_message_count(self):
		return self.H.stat()[0]
	def get_message(self,i):
		return self.H.retr(i)
	def get_id(self, i):
		return self.H.uidl(i)
	def remove(self, i):
		return self.H.dele(i)
	def quit(self):
		return self.H.quit()

