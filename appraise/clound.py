import os
import oss2
from qcloud_image import Client, CIUrl, CIFile, CIBuffer, CIUrls, CIBuffers, \
    CIFiles
from itertools import islice
from PIL import Image

class Cloud():

    def cloud_init(self):
        """初始化"""
        accesskey = "LTAI4RwccFRxmMaU"
        accessid = "rwslPXNMB0DrVTSzwFjPEGumvy78ca"
        auth = oss2.Auth(accesskey, accessid)
        return auth

    def cloud_query_files(self, auth, bucketname):
        """
        查询一个存储桶里的所有文件
        返回一个list
        """
        bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com',
                             bucketname)
        file_list = [b.key for b in islice(oss2.ObjectIterator(bucket), 10)]
        return file_list




    def cloud_add_file(self, auth, bucketname, file):
        """
        向一个存储桶里添加一个文件
        无返回
        """
        print('ssssssssssssssss',os.getcwd())
        if file[0] == '/':
            name = file.split('/')[-1]
        else:
            name = file.split('\\')[-1]
        bucket = oss2.Bucket(
            auth, 'http://oss-cn-beijing.aliyuncs.com', bucketname)
        bucket.put_object_from_file(name, file)


    def cloud_remove_file(self, auth, bucketname, filename):
        """
        移除存储桶中间的一个文件
        :param auth:
        :param bucketname:
        :param filename:
        :return:无返回
        """
        bucket = oss2.Bucket(
            auth, 'http://oss-cn-beijing.aliyuncs.com', bucketname)
        print(filename)
        bucket.delete_object(filename)






