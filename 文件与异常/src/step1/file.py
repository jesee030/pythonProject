def file(name,encoding = 'utf-8'):
    '''
       读取文件内容,如文件存在，则输出文件信息，
       若文件不存在，则输出`无法打开指定的文件!`，
       若文件编码方案和打开指定编码方案不同，则输出`指定了未知的编码!`，
       若读取文件时解码错误，则输出`读取文件时解码错误!`
       :params name:文件名
       :params encoding:编码方案。默认为'utf-8'
       :return ：无返回值，直接输出
       '''
    #        请在此处添加代码       #
    # *************begin************#
    f = None
    try:
        f = open(name, 'r', encoding=encoding)
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


    # **************end*************#

if __name__ == '__main__':
    name,encoding = input().split(',')
    file(name=name,encoding=encoding)


