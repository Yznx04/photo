from qcloud_image import Client, CIUrl, CIFile, CIBuffer, CIUrls, CIBuffers, \
    CIFiles

import os

# appid = '1256911928'
# secretid = 'AKIDSq495t2JbjhVRUIXMIUkcc6VpNo5QKv0'
# secretkey = 'Ac4mbinjcsLGh1oVxj1jXknfh6c1GQQS'
# bucket = 'BUCKET'
# client = Client(appid, secretid, secretkey, bucket)
# client.use_http()
# client.set_timeout(30)


s = os.path.abspath(os.path.join(os.getcwd(), "./upload"))
filepath = os.path.join(s, "j.txt")

print("s: %s" %s)
print("f: %s" %filepath)