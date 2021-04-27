import usr
import zipfile

if __name__ == "__main__":
    pw = usr.Try()
    print(pw)
    zipFile = zipfile.ZipFile('D:\pythonProject\计算机取证\src\step1\evil.zip', 'r')
    try:
        zipFile.extractall('step1',pwd=bytes(str(pw), 'ascii'))
        print('解压成功')
    except:
        print('解压失败')
    finally:
        zipFile.close()    # 关闭文件