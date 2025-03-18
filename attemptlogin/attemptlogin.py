login_fail = 0
posts = 0
fail_ip = []

with open("keystone.common.wsgi", "r") as login_file:
    for line in login_file:
        if "- - - - -] Authorization failed" in line:
            login_fail += 1
            fail_ip.append(line.split(" ")[-1])
        elif "POST" in line:
            posts += 1

print(f"number of failed attemp was: {login_fail}")
print(fail_ip)
print(f"number of posts is: {posts}")



    
