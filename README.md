# MQTT

### add path for using .bat files
  cd into directory contains .bat files
  $setx PATH "%PATH%;%CD%"

### set alias path as your directory
1.open file broker.txt
2.change path in line 3 into your directory path contain broker.py file
3.save as named broker.bat and replace
4.repeat step 1-3 with subscribe.txt and publish.txt

### run
1.run broker with 
  $ broker [host_ip_address]
2.run subscriber
  $ subscribe [host_ip_address] [topic_name]
3.run publisher
  $ publisher [host_ip_address] [topic_name] [message]
