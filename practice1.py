# server=["web1","web2","db1"]
# print(server[2])

services=["nginx","docker"]
services.append("jenkins")
print(services)

services=["nginx","docker"]
# services[1]="kubernetes"
# print(services)
services.remove("docker")
print(services)

ports=[22,80,443,8080,3306]
# print(ports[1])
# print(ports[2]) 

# ports.reverse()

print(ports[::2])

usage=[45,67,89,34,90]
for x in usage:
    if x >80:
        print("alert")
        break

    servers=["web","db","cache"]
    print(len(servers))

    


