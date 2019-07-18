"""
 Implements a simple HTTP/1.0 Server
"""
import socket
import time

class Server():
    def __init__(self, server_config):
        self.SERVER_HOST = server_config['server_host']
        self.SERVER_PORT = server_config['server_port']
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.SERVER_HOST, self.SERVER_PORT))
        self.server_socket.listen(1)
        self.is_run = False
        print('Listening on port %s ...' % self.SERVER_PORT)
    
 
    def run(self, refresh_time):
        """ Run server """
        self.is_run = True
        
        def open_html(path):
            fin = open(path)
            content = fin.read()
            fin.close()
            return content
        
        while self.is_run == True:
            self.client_connection, self.client_address = self.server_socket.accept()
            request = self.client_connection.recv(1024).decode()
            template1 = open_html('templates/part1.html')
            template2 = open_html('templates/part2.html')
            content = open_html('templates/content.html')
            template3 = open_html('templates/part3.html')
            response = 'HTTP/1.0 200 OK\n\n' + template1 + str(refresh_time) + template2 + content + template3
            self.client_connection.sendall(response.encode())
            self.client_connection.close()
        
        self.server_socket.close()
        