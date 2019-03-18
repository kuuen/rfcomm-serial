#coding:utf-8

import sys
import subprocess
import serial
import re

ser = None
INVALID_CMD = 'invalid Cmd'

with (serial.Serial('/dev/rfcomm0', 9600)) as ser:
    ser.write('要求受付開始'.encode('utf-8'))

    # 受信したメッセージはバイト列というもの b'文字列' となるdecode()して文字列にして改行コードを省いている
    recvStr = str(ser.readline().decode()).replace("\r\n", "")
    print("recv msg : {}".format(recvStr))

    result = [0]

    # 指示内容を確認
    if 'ledon' == recvStr:
        # シェルスクリプトでなく直接コマンドを書いても行けるはず
        reslut = subprocess.check_output('/home/pi/work/python/rfcomm/danboOn.sh', stderr=subprocess.STDOUT)
    elif 'ledoff' == recvStr:
        result = subprocess.check_output('/home/pi/work/python/rfcomm/danboOff.sh', stderr=subprocess.STDOUT)
    elif 'wifi' == recvStr:
        ser.write('wifi 再起動\r\n'.encode('utf-8'))
        result = subprocess.check_output('/home/pi/work/python/rfcomm/wifiRestart.sh', stderr=subprocess.STDOUT)
    elif 'reboot' == recvStr:
        ser.write('マシン再起動開始\r\n'.encode('utf-8'))
        result = subprocess.check_output('/home/pi/work/python/rfcomm/reboot.sh', stderr=subprocess.STDOUT)
    elif 'shutdown' == recvStr:
        ser.write('マシンシャットダウン開始\r\n'.encode('utf-8'))
        result = subprocess.check_output('/home/pi/work/python/rfcomm/shutdown.sh', stderr=subprocess.STDOUT)
    elif re.match(r'^ch ', recvStr) != None:
        ser.write('wifiチャンネル変更\r\n'.encode('utf-8'))
        ch = re.split(" +", recvStr)[1]
        if re.search(r'^[1-9]$|^1[0-3]$', ch) == None:
            ser.write('Channel specification error'.encode('utf-8'))
        else:
            cmds = []
            cmds.append('sudo')
            cmds.append('python3')
            cmds.append('/home/pi/work/python/rfcomm/wifi-ch-change.py')
            cmds.append('-c')
            cmds.append(ch)
            result = subprocess.check_output(cmds, stderr=subprocess.STDOUT)

    elif 'help' == recvStr:
        ser.write('help\r\n'.encode('utf-8'))
        ser.write('ledon, ledoff, wifi, reboot,shutdown, ch [1-13]'.encode('utf-8'))
        result[0] = 0
    else:
        print(INVALID_CMD + ':' + recvStr)
        ser.write('こんなの認めないわ'.encode('utf-8'))

    # resultが空、配列になりエラー内容が設定されていたらNGとする
    if len(result) > 0:
        ser.write('result: ng\r\n'.encode('utf-8'))
        print(result)
    else:
        ser.write('result: success\r\n'.encode('utf-8'))

    ser.write('終了\r\n'.encode('utf-8'))


