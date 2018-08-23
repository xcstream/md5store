import md5
import redis
import time
r = redis.Redis(host='localhost',port=8888,db=0)
start = 100000
end   = 999999

count = end-start
current = start

time_start = time.time()
while 1:
    m1 = md5.new()
    current = current +1
    src = str(current)
    m1.update(src.encode(encoding='utf-8'))
    md5r = m1.hexdigest()
    r.set(md5r, src)
    if (current % 5000 == 0):
        print src, md5r
        per = float(current-start)/count *100
        print per , '%'
    if current == end:
        break
time_end = time.time()
print('totally cost', time_end - time_start)