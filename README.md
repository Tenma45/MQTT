# MQTT  

### Defualt
must place this repo to D:\MQTT  
and python command is 'py'

### IF NOT Defualt, update .bat files
1.right click on broker.bat file, then click edit.  
2.change path in line 2 into your directory path contain broker.py file.  (ex. C:\MQTT-Project\broker.py)  
3.change command 'py' in line 2 into your python command. (ex. python python3 )  
4.save then close.  
5.repeat step 1-4 with subscribe.txt and publish.txt.  
  
### run  
command line with path to where contains .bat files
- run broker  
$ broker [host_ip_address]  
- run subscriber  
$ subscribe [host_ip_address] ["topic_name"]  
- run publishe  
$ publishe [host_ip_address] ["topic_name"] ["message"]  
