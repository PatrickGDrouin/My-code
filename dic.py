dic = {"type" : "lightining", "name" : "pikachu"}

def print_error():
    print("no such thing")
    # return "no such thing"

dic.get("flavor", print_error())


