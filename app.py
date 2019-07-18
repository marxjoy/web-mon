"""
Program that monitors web sites and reports
their availability. This tool is intended 
as a monitoring tool for web site 
administrators for detecting problems on
theis sites.
"""

import json
import threading
import webbrowser
import check_loop
import web_server

server_config = {'server_host': 'localhost', 'server_port': 8000}

with open('config.json') as json_data_file:
    data = json.load(json_data_file) # checking perdiod from config file
checking_period = int(data['checking_period']['sec'])

check_loop.main()
server = web_server.Server(server_config)
thread_server = threading.Thread(target=server.run, args=[checking_period])
thread_server.start()
webbrowser.open_new_tab('http://'+ server_config['server_host'] + ':' + 
                        str(server_config['server_port']))
check_loop.time_loop.start(block=True)
server.is_run = False