from urllib2 import Request, urlopen, URLError

request = Request('http://placekitten.com/')

try:
	response = urlopen(request)
	kittens = response.read()
	print kittens[0:1200]
except URLError, e:
    print 'No kittez. Got an error code:', e
