import redis
r = redis.Redis(host='localhost',port=8888,db=0)

oldstart = r.get('m_start')
oldend = r.get('m_end')

print "start", oldstart , 'end',oldend

start = input("start:")
end = input("end:")
if start != '':
    r.set('m_start',start)

if end != '':
    r.set('m_end',end)

oldstart = r.get('m_start')
oldend = r.get('m_end')
print "start", oldend, 'end', oldend

