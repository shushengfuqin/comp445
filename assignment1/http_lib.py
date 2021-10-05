import http.client
from urllib.parse import urlparse
import requests
import json
import ast
import http_lib
import pprint


def GET(url,str):

    # separate the url in to scheme, netloc, path, paraams, query and fragment
    pp = pprint.PrettyPrinter(indent = 4)
    link = urlparse(url)
    HOST = link.netloc
    PATH = link.path
    if PATH == "":
        PATH = "/"
    QUERY = link.query

    str = str.split(" ")
    
    HEADER = ""
    start = 0
    for x in str:
        start += 1
        if (x == "-h"):
            HEADER += str[start] + ""
    
    conn = http.client.HTTPConnection(HOST,80)
    conn.request("GET", PATH, HEADER)
    receive = conn.getresponse()

    print("GET", PATH,"HTTP/",receive.version/10.)
    print("Host:", HOST,"\n")
    print(receive.reason, receive.status)
    
    if ("-v" in str):
        pp.pprint(receive.msg)
    else:
        pp.pprint(receive.getheaders())
    
    pp.pprint(receive.read())
    
    receive.close()
    # # get the header of the get request into json pretty
    # with open('getheader.json', 'w') as outfile:
    #     json.dump(dict(HEADER), outfile, indent=4)

    # # get the body of the get request into json pretty
    # rbodyjson = receive.json()

    # with open('getbody.json', 'w') as outfile:
    #     json.dump(rbodyjson, outfile, indent=4)


# GET("http://httpbin.org/get")


def POST(url,str):

    # separate the url in to scheme, netloc, path, paraams, query and fragment
    link = urlparse(url)
    HOST = link.netloc
    PATH = link.path
    if PATH == "":
        PATH = "/"
    QUERY = link.query
    if QUERY == "":
        QUERY = "?"+QUERY

    post = requests.post(url)
    HEADER = post.headers
    BODY = post.content

    args = str.split(" ")

    body = {}
    argsLenth = len(args)
    if ("-d" in args):
        print("data")
        a = args.index("-d") + 1
        body = args[a:argsLenth]
    elif ("-f" in args):
        print("file")
    # # get the header of the get request into json pretty
    # with open('postheader.json', 'w') as outfile:
    #     json.dump(dict(HEADER), outfile, indent=4)

    # # get the body of the get request into json pretty
    # rbodyjson = post.json()

    # with open('postbody.json', 'w') as outfile:
    #     json.dump(rbodyjson, outfile, indent=4)


# POST("http://httpbin.org/post")
