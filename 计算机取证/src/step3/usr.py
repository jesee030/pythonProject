# coding:utf-8
import exifread

def Evidence(path):
    #读取并打印图像的Exif头信息
    #   请在此添加实现代码   #
    # ********** Begin *********#
    f=open(path,'rb')
    tags= exifread.process_file((f))
    # for tag in tags:
    #     print(tag,":",tags[tag])
    if tags.get("Image Model") != None:
        print("具体型号: {}".format(tags.get("Image Model")))
    if tags.get("Image Software") != None:
        print("图像软件: {}".format(tags.get("Image Software")))
    if tags.get("Image DateTime")!=None:
        print("拍摄时间: {}".format(tags.get("Image DateTime")))
    if tags.get("GPS GPSLatitude")!=None and tags.get("GPS GPSLatitudeRef")!=None:
        print("GPS纬度: {} {}".format(tags.get("GPS GPSLatitude"),tags.get("GPS GPSLatitudeRef")))
    if tags.get("GPS GPSLongitude")!=None and tags.get("GPS GPSLongitudeRef")!=None:
        print("GPS经度: {} {}".format(tags.get("GPS GPSLongitude"),tags.get("GPS GPSLongitudeRef")))
    if  tags.get("Image Make")!=None:
        print("品牌信息: {}".format(tags.get("Image Make")))
    # print("具体型号: {}\n图像软件: {}\n拍摄时间: {}\nGPS纬度: {} {}\nGPS经度: {} {}\n品牌信息: {}".format(tags.get("Image Model"),
    #         tags.get("Image Software"),tags.get("Image DateTime"),tags.get("GPS GPSLatitude"),tags.get("GPS GPSLatitudeRef"),
    #         tags.get("GPS GPSLongitude"),tags.get("GPS GPSLongitudeRef"),tags.get("Image Make")))
    # ********** End **********#