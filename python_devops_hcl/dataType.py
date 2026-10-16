#list

dtList = ["data1","data2","data3"]

print(type(dtList))



#tuple
dtTuple = ("tuple1","tuple2","tuple3","tuple4")
print(type(dtTuple))


#set

dtSet = {"set1","set1","set2","set2"}

print(type(dtSet))

#dictonary

dtDictonary = {"name":"gautam", "age":"25"}

print(type(dtDictonary))



services = ["service1","service2","vice3","vice4"]

for s in services:
    print(s)


print("------------------------------------------------------------------------------------------------------")

web_server = [s for s in services if s.startswith("ser")]
#web_servers = [s for s in servers if s.startswith("web")]
print(web_server)


status = {s: "up" for s in services}

print(status)