# MQTT  

### Defualt directory
place this repo to D:\mqtt

### IF NOT Defualt directory, set .bat files as your directory
1.open file broker.txt  
2.change path in line 3 into your directory path contain broker.py file  
3.change command 'py' in line 3 up to your python version
3.save as named broker.bat and replace  
4.repeat step 1-3 with subscribe.txt and publish.txt (optional test.txt)
  
### run  
- run broker with  
$ broker [host_ip_address]  
- run subscriber  
$ subscribe [host_ip_address] ["topic_name"]  
- run publisher  
$ publisher [host_ip_address] ["topic_name"] ["message"]  
