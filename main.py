import md5
import redis
import time
r = redis.Redis(host='localhost',port=8888,db=0)


start = int(r.get('m_start'))
end   = int(r.get('m_end'))

count = end-start
current = start

time_start = time.time()
while 1:
    m1 = md5.new()
    current = current +1
    src = str(current)

    while len(src) < 6:
        src = '0'+src

    m1.update(src.encode(encoding='utf-8'))
    md5r = m1.hexdigest()
    r.set(md5r, src)
    if (current % 50000 == 0):
        print src, md5r
        per = float(current-start)/count *100
        print per , '%'
        r.set('m_start',src)
    if current == end:
        break
time_end = time.time()
print('time elapsed', time_end - time_start)