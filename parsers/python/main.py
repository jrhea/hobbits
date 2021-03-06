#!/usr/bin/env python

from parser import (
    req_parse,
    req_marshal,
    res_parse,
    res_marshal,
)

################ MAIN ################

if __name__ == "__main__":
    example_ping_req = "EWP 0.1 PING none none 0 5 H\n12345"
    req_parsed = req_parse(example_ping_req)
    print(req_parsed)

    res_marshaled = req_marshal(req_parsed)
    #check marshaling of dict wo header
    print(res_marshaled)
    #check marshaling of string w header
    print(req_marshal("EWP 0.1 PING none none 0 5\n12345"))

    example_ping_res = "200 none 0\n"
    res_parsed = res_parse(example_ping_res)
    print(res_parsed)
    res_marshaled = res_marshal(res_parsed)
    #marshaling of dic wo header
    print(res_marshaled)
    #marshaling of string w header
    print(res_marshal("200 none 0 0\n"))