import socket
import urllib2
import time
if __name__ == '__main__':  
	while 1:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
		time.sleep(5)  
		sock.connect(('localhost', 1000))  
		time.sleep(5)  
		#sock.send('(hello)')  
		data=sock.recv(42)
		if not data: break
		cur_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		print data+" "+cur_time
		
		user_name = "USERNAME"
		user_password="PASSWORKD"
		#user_status="Robot say hello to twitter by brucebot"
		user_status=data+" "+cur_time
		proxy_info = {
			'user' : 'username',
			'pass' : 'password',
			'host' : "proxy.com",
			'port' : 8080
			}

		# build a new opener that uses a proxy requiring authorization
		proxy_support = urllib2.ProxyHandler({"http" : \
		"http://%(user)s:%(pass)s@%(host)s:%(port)d" % proxy_info})
		opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
		# install it
		urllib2.install_opener(opener)
		#normal connect
		
		req=urllib2.Request('http://twitter.com/statuses/update.json')
		req.add_header('Authorization', 'Basic %s' % (user_name + ':' + user_password).encode("base64")[0:-1] )
		req.add_data("status=%s" % user_status)
		
		handle = urllib2.urlopen(req)
		result = handle.read()
		opener.close()
		sock.close()
