import http.client
from urllib.parse import urlparse
import requests
import json


def GET(url, str):

    # separate the url in to scheme, netloc, path, paraams, query and fragment

    # link = urlparse(url)
    # HOST = link.netloc
    # PATH = link.path
    # if PATH == "":
    #     PATH = "/"
    # QUERY = link.query


    receive = requests.get(url)
    HEADER = receive.headers
    if ("-v" in str):
        for key, value in receive.headers.items():
            print(key, ":", value)
        print(receive.text)
        with open('data.txt', 'w') as outfile:
            json.dump(dict(receive.headers),outfile, indent = 4)
            outfile.write(receive.text)
        outfile.close
    else:
        print(receive.text)
        with open('data.txt', 'w') as outfile:
            outfile.write(receive.text)
        outfile.close

    receive.close()



def POST(url, str):

    #process the string
    args = str.split(" ")
    
    BODY = {}
    argsLenth = len(str)
    if ("--d" in args):
        a = args.index("--d") + 1
        BODY = args[a:argsLenth]
        print(BODY)
    elif ("--f" in args):
        file = open(args[args.index("--f")+1],"r")
        BODY = (file.read())

    post = requests.post(url,json = BODY)

    print(post.text)




