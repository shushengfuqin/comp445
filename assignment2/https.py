import argparse
import os
import socket
import re

def server(port, dir):
    host = ''
    localdir = dir
    if dir is None:
        localdir = os.path.dirname(os.path.realpath(__file__))
    
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((host, port))
    listener.listen(5)
    if args.verbose:
        print('Httpfs server is listening at port', port)
    while True:
        files = os.listdir(localdir)
        conn, addr = listener.accept()
        request = conn.recv(1024).decode("utf-8")
        request = request.split('\r\n')
        mpv = request[0].split()
        method = mpv[0]
        path = mpv[1]

        index = request.index('') 
        data = ''
        for l in request[index+1:]:
            data += l + '\n'

        response = ''
        
        if method == 'GET':
            if path == '/':
                for f in files:
                    response += f + '\n'
            elif re.search(r'\/\w+.\w+', path):
                path = path.strip('/')
                if path in files:
                    theFile = open(localdir +'/'+ path, 'r')
                    response = theFile.read() + '\n'
                    theFile.close()
                else:
                    response = 'HTTP 404 - file(s) not found\n'
        elif method == 'POST':
            path = path.strip('/')
            if path in files:
                theFile = open(localdir +'/'+ path, 'w+')
                theFile.write(data)
                theFile.close()
                response = 'Data overwritten to file '+path
            elif path not in files:
                theFile = open(localdir +'/'+ path, 'w+')
                theFile.write(data)
                theFile.close()
                response = 'Data written to new file '+ path
            else:
                response = "HTTP 403 - action refused \n"

        conn.sendall(response.encode('utf-8'))
        conn.close()



parser = argparse.ArgumentParser(description="http fileserver")
parser.add_argument('-v', '--verbose', help = 'Prints debugginng messages', action='store_true')
parser.add_argument('-p', '--port', type = int, default= 8080,help='Specifies the port number that the server will listen and serve at.\n\n Default is 8080')
parser.add_argument('-d', '--directory', type = str, help='Specifies the directory that the server will use to read/write requested files. Default is the current directory when launching the application.')
args = parser.parse_args()
server(args.port,args.directory)