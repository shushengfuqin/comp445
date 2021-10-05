from urllib.parse import urlparse
import requests
import json


def GET(url):

    # separate the url in to scheme, netloc, path, paraams, query and fragment
    link = urlparse(url)
    HOST = link.netloc
    PATH = link.path
    if PATH == "":
        PATH = "/"
    QUERY = link.querypi

    receive = requests.get(url)
    HEADER = receive.headers
    BODY = receive.content

    # get the header of the get request into json pretty
    with open('getheader.json', 'w') as outfile:
        json.dump(dict(HEADER), outfile, indent=4)

    # get the body of the get request into json pretty
    rbodyjson = receive.json()

    with open('getbody.json', 'w') as outfile:
        json.dump(rbodyjson, outfile, indent=4)


GET("http://httpbin.org/get")


def POST(url):

    # separate the url in to scheme, netloc, path, paraams, query and fragment
    link = urlparse(url)
    HOST = link.netloc
    PATH = link.path
    if PATH == "":
        PATH = "/"
    QUERY = link.query

    post = requests.post(url)
    HEADER = post.headers
    BODY = post.content

    # get the header of the get request into json pretty
    with open('postheader.json', 'w') as outfile:
        json.dump(dict(HEADER), outfile, indent=4)

    # get the body of the get request into json pretty
    rbodyjson = post.json()

    with open('postbody.json', 'w') as outfile:
        json.dump(rbodyjson, outfile, indent=4)


POST("http://httpbin.org/post")
