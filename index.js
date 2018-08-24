$('#mountpoint').html("<div style='text-align:center'><div style='text-align:left: width:370px;background:#eeeeee;margin:0 auto;display:inline-block;padding:40px;border-radius:10px;'> <div style='display:none' id='main'> <div>md5解密 <input style='width:300px' id='m1'> <button  onclick='dec()'>解密</button> </div> <div>结果: <span id='d1'></span> </div> </div> <div id='loading'>加载中... </div> </div> </div>")
var clientId = "clientId" + new Date().getTime() +'_' + Math.random();
client = new Paho.MQTT.Client("am.appxc.com", Number(8084), clientId);
client.onConnectionLost = function () {
    if (responseObject.errorCode !== 0) {
        $('#d1').html('断开链接，刷新重试')
    }
};
client.onMessageArrived = function () {
    var intv = setTimeout(function () {
        if($('#d1').html().trim()==''){
            $('#d1').html('未找到')
        }
    },700)
   var data = JSON.parse(message.payloadString);
    if(data.code==200){
        $('#d1').html(data.text)
        clearInterval(intv)
    }
};
client.connect({useSSL:true,onSuccess:function(){
    client.subscribe(clientId);
    $('#main').show()
    $('#loading').hide()
    $('#m1').val('e9c9a1413ebf17f0f15c5a716d77cd69')
}});

window.dec = function dec(){
    $('#d1').html('')
    var payload = {
        clientId:clientId,
        md5:$('#m1').val()
    }
    var message = new Paho.MQTT.Message(JSON.stringify(payload));
    message.destinationName = 'md5store';
    client.send(message);
}