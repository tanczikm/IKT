vizho = int(input("Add meg a hőmérsékletet Celsius fokban! "))

if vizho < 0:
    print("A víz halmazállapota: szilárd")
elif vizho <= 100:
    print("A víz halmazállapota: folyékony")
elif vizho > 100:
    print("A víz halmazállapota: légnemű")