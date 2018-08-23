# -*- coding: utf-8 -*-
import redis
import md5


r = redis.Redis(host='localhost',port=8888,db=0)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
<html>
<head>
    <meta charset='utf-8'>
</head>
<body>
<script src="https://cdn.bootcss.com/blueimp-md5/2.10.0/js/md5.min.js"></script>
<script src="https://cdn.bootcss.com/jquery/3.3.0/jquery.min.js"></script>
    <div style='text-align:center'>
        <div style='text-align:left: width:340px;background:#eeeeee;margin:0 auto;display:inline-block;padding:40px;border-radius:10px'>
        <div> 
            md5解密
            <input style='width:200px' id='m1'>
            <button  onclick='dec()'>解密</button>
        </div>
        <div>
            结果: <span id='d1'>
        </div>
        <div> 
            md5加密
            <input style='width:200px' id='m2'>
            <button onclick='enc()'>加密</button>
        <div>
            结果: <span id='d2'>
        </div>
        </div>
        </div>

    </div>
    <script>
        function dec(){
            $.get('/md5decode/'+ $('#m1').val(),function(r){
                console.log(r)
                $('#d1').html(r)
            })
        }
        function enc(){
            $.get('/md5encode/'+ $('#m2').val(),function(r){
                console.log(r)
                $('#d2').html(r)
            })
        }
    </script>
</body>
</html>  
"""

@app.route('/md5encode/<inputmd5>')
def encode(inputmd5):
    m1 = md5.new()
    src = str(inputmd5)
    m1.update(src.encode(encoding='utf-8'))
    md5r = m1.hexdigest()

    if r.get(md5r) == None:
        r.set(md5r,inputmd5)
    return md5r

@app.route('/md5decode/<inputmd5>')
def decode(inputmd5):
    if(len(inputmd5) == 32):
        result = r.get(inputmd5)
        if result == None:
            result = '未找到'
        return result
    else:
        return ''

app.run()

# start = 13900000000
# end   = 13999999999
#
# count = end-start
# current = start
#
# time_start = time.time()
# while 1:
#     m1 = md5.new()
#     current = current + 1
#     src = str(current)
#     m1.update(src.encode(encoding='utf-8'))
#     md5r = m1.hexdigest()
#     r.set(md5r, src)
#     if (current % 5000 == 0):
#         print src, md5r
#         per = float(current-start)/count *100
#         print per , '%'
#     if current == end:
#         break
# time_end = time.time()
# print('totally cost', time_end - time_start)