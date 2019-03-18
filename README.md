# rfcomm-serial

## Description 説明
主にraspberry pi のhotaspdが不安定になった場合、BlueToothのシリアル通信で復帰を試みるためのもの

おまけ機能  
GPIOに接続したLEDを点灯、消灯する

## Requirement
作動環境  
Raspberry Pi Model B+  
OS raspbian 8.0  
hostapd v0.8.x  
python 3.4.2  
pyserial 3.4 (# sudo pip3 install PySerial でインストール)  

Bluetoothトングルを使用 型番を忘れた lsusbの結果は  
Cambridge Silicon Radio, Ltd Bluetooth Dongle (HCI mode) と出た

## Install
ファイルを/home/pi/work/python/rfcomm/ に設置か書くパスを修正する  

サービスに登録する  
sudo ln -s /home/pi/work/python/rfcomm/rfcomm.service  /etc/systemd/system/rfcomm.service 等  

サービスを有効にする  
sudo systemctl enable rfcomm.service  

通信し合う機器とペアリングを行う  
以下のコマンドを実行  
sudo bluetoothctl  
[bluetooth] power on  
[bluetooth] discoverable on  
[bluetooth] agent on  
[bluetooth] default-agent  
"agent on"か"default-agent"の時に接続機器のペアリングを行ったはず  

## Usage 使い方

