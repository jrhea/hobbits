import sys

from parser import (
    req_parse,
    req_marshal,
    res_parse,
    res_marshal,
)

reqres = sys.argv[1]
chars = int(sys.argv[2])

stdin = sys.stdin.read(chars)

if reqres == "request":
    print(req_marshal(req_parse(stdin)))
elif reqres == "response":
    print(res_marshal(res_parse(stdin)))
else:
    print("invalid request/response input")
