import os
import oss2
import clound
from urllib.parse import unquote
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from urllib.parse import urljoin
from appraise.clound import Cloud
from clound import settings
bucketname = 'yun10'

def show_indent(requests):
    s = Cloud()
    auth = s.cloud_init()
    files = s.cloud_query_files(auth, bucketname)
    init = 'http://yun10.oss-cn-beijing.aliyuncs.com/{}'
    file_list = []
    for file in files:
        file = init.format(file)
        file_list.append(file)
    img = {
        "img_list": file_list,
    }
    print('-----------------')
    print(file_list)

    return render(requests, 'index.html', context=img)

def upload(requests):

    c = Cloud()
    auth = c.cloud_init()
    if requests.method == 'POST':
        img = requests.FILES.get("images", None)
        if not img:
            return HttpResponse("你没有选择图像")
        s = os.path.abspath(os.path.join(os.getcwd(), "./upload"))
        filename = os.path.join(s, img.name)
        print('------------------', filename)
        uploads = open(filename, 'wb+')
        for chunk in img.chunks():
            uploads.write(chunk)
        uploads.close()
        c.cloud_add_file(auth, bucketname, filename)
        os.remove(os.path.join(s, img.name))
        return render(requests, 'ok.html')

def deletephoto(requests, img):
    s = Cloud()
    auth = s.cloud_init()
    file = requests.build_absolute_uri().split('/')[-1]
    filename = unquote(file)
    s.cloud_remove_file(auth, bucketname, filename)
    return render(requests, 'ok.html')

def download(requests, img):
    s = Cloud()
    auth = s.cloud_init()
    filename = requests.build_absolute_uri().split('/')[-1]
    filename = unquote(filename)
    cs = os.path.abspath(os.path.join(os.getcwd(), "./upload"))
    bucket = oss2.Bucket(
        auth, 'http://oss-cn-beijing.aliyuncs.com', bucketname)
    bucket.get_object_to_file(filename, os.path.join(cs, filename))
    file = open(os.path.join(cs, filename), 'rb')
    print(file)
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="图片.jpg"'
    # file.close()
    # os.remove(os.path.join(cs, filename))
    return response
