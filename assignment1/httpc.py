import sys
from http_lib import GET,POST

def main(kb):
    method = kb[0]
    print(method)
    url = kb[-1]
    print(url)
    del kb[0], kb[-1]
    body = " ".join(kb)
    print(body)

    if method == "GET":
        if "-d" not in body and "-f" not in body:
            print(f"[GET REQUEST] {body}")
            GET(url,body)
        else:
            print("\nError : GET REQUEST SHALL NOT BE USED WITH OPTIONS -d or -f")
    elif method == "POST":
        if (("-d" in body) or ("-f" in body)) is not (("-d" in body) and ("-f" in body)):
            print(f"[POST REQUEST] {body}")
            POST(url,body)
        else:
            print("\nError : POST REQUEST SHALL NOT USING -d and -f at the same time")

if __name__ == "__main__":
    main(sys.argv[1:])