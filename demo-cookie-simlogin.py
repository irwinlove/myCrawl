import urllib2
import urllib
import cookielib
# cookie=cookielib.CookieJar()
filename='cookie-login.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
postdata=urllib.urlencode({'account':'irwin2012@126.com','password':''})

loginUrl='http://www.zhihu.com/#signin'
result = opener.open(loginUrl,postdata)

cookie.save(ignore_discard=True,ignore_expires=True)

editUrl='http://www.zhihu.com/people/edit'
result=opener.open(editUrl)
print result.read()