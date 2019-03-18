# rfcomm-serial

## Description 説明
主にraspberry pi のhotaspdが不安定になった場合、BlueTooth通信で復帰を試みるためのもの


おまけ機能  

## Requirement
作動環境  
Raspberry Pi Model B and B+  
OS raspbian 8.0  
python 3.4.2  
hostapd v0.8.x  
Bluetoothトングルを使用 型番を忘れた lsusbの結果は  
Cambridge Silicon Radio, Ltd Bluetooth Dongle (HCI mode) と出た

## Install
ファイルを/home/pi/work/python/rfcomm/ に設置か書くパスを修正する  

サービスに登録する  
sudo ln -s /home/pi/work/python/rfcomm/rfcomm.service  /etc/systemd/system/rfcomm.service 等  

サービスを有効にする  
sudo systemctl enable rfcomm.service  

通信しあう機器とペアリングを行う  
