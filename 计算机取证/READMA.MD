## 第1关：zip压缩文件暴力破解
任务描述
本关任务：编写一个能暴力破解加密Zip文件的小程序。

相关知识
对于一个zip格式的压缩包，默认密码为6位，是数字和字母的组合。暴力破解的基本思路是，调用Python中的zipfile模块的extractall函数，尝试各种数字、字母组合，成功解压时返回相应的压缩密码。评测系统会判断返回的结果是否正确，正确即返回解压成功。

同学们可以思考下，如何破解密码是数字、字母、以及特殊字符的组合。
提示：itertools模块,使用迭代器可以防止爆破的位数太多而爆内存。

编程要求
有一个加密的Zip格式的压缩文件src/step1/evil.zip，它的密码未知。
现在已知密码是数字012345与字母asd的排列组合，请在右侧编辑器中的Try函数中，尝试破解这个文件的密码，并将其密码返回。
评测系统会尝试使用这个密码解压src/step1/evil.zip，如果解压成功，则会输出解压成功，否则会输出解压失败。

测试说明
使用密码成功解压时输出的解压成功即为通关条件。
## 第2关：PDF取证
任务描述
本关任务：编写一个能读取PDF元数据的小程序。

相关知识
曾经有一次案件，当时黑客组织发布了ANONOPS_The_Press_Release这份稿件，希腊警方在稿件的元信息中发现了作者Alex Tapanaris的名字，然后以此为证据将其逮捕，也就是所谓的电子取证。基本思路是，调用Python中的PyPDF2模块的getDocumentInfo函数，提取PDF文件中的元数据。

PyPDF2
PyPDF2是作为PDF工具包构建的python库，它能够:

提取文档信息（标题，作者，...）
按页拆分文档
逐页合并文档
裁剪页面
合并多个页面到一个页
对pdf文档进行加密解密
等等
注意，这个模块的名字对大小写是敏感的，所以，确保y是小写的，其他字母都是大写的
##### PdfFileReader
构造方法：
    PyPDF2.PdfFileReader(stream,strict = True,warndest = None,overwriteWarnings = True)
初始化一个 PdfFileReader 对象，此操作可能需要一些时间，因为 PDF 流的交叉引用表被读入内存。

| 参数                      | 含义                                                         |
| ------------------------- | ------------------------------------------------------------ |
| stream                    | File 对象或支持与 File 对象类似的标准读取和查找方法的对象，也可以是表示 PDF 文件路径的字符串。 |
| strict（bool）            | 确定是否应该警告用户所用的问题，也导致一些可纠正的问题是致命的，默认是 True |
| warndest                  | 记录警告的目标(默认是 sys.stderr)                            |
| overwriteWarnings(bool)\| | 确定是否 warnings.py 用自定义实现覆盖 Python 模块（默认为 True） |


PdfFileReader 对象的属性和方法

| 属性和方法                                         | 描述                                               |
| -------------------------------------------------- | -------------------------------------------------- |
| getDestinationPageNumber(destination)              | 检索给定目标对象的页码                             |
| getDocumentInfo()                                  | 检索 PDF 文件的文档信息字典                        |
| getFields(tree = None,retval = None,fileObj= None) | 如果此 PDF 包含交互式表单字段，则提取字段数据      |
| getFormTextFields()                                | 从文档中检索带有文本数据（输入，下拉列表）的表单域 |
| getNameDestinations(tree = None,retval= None)      | 检索文档中的指定目标                               |
| getNumPages()                                      | 计算此 PDF 文件中的页数                            |
| getOutlines(node = None,outline = None)            | 检索文档中出现的文档大纲                           |
| getPage(pageNumber)                                | 从这个 PDF 文件中检索指定编号的页面                |
| getPageLayout()                                    | 获取页面布局                                       |
| getPageMode()                                      | 获取页面模式                                       |
| getPageNumber(pageObject)                          | 检索给定 pageObject 处于的页码                     |
| getXmpMetadata()                                   | 从 PDF 文档根目录中检索 XMP 数据                   |
| isEncrypted                                        | 显示 PDF 文件是否加密的只读布尔属性                |
| namedDestinations                                  | 访问该getNamedDestinations()函数的只读属性         |


PdfFileWriter
这个类支持 PDF 文件，给出其他类生成的页面。

| 属性和方法                                                   | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| addAttachment(fname,fdata)                                   | 在 PDF 中嵌入文件                                            |
| addBlankPage(width= None,height=None)                        | 追加一个空白页面到这个 PDF 文件并返回它                      |
| addBookmark(title,pagenum,parent=None,color=None,bold=False,italic=False,fit=’/fit,*args’) |                                                              |
| addJS(javascript)                                            | 添加将在打开此 PDF 是启动的 javascript                       |
| addLink(pagenum,pagedest,rect,border=None,fit=’/fit’,*args)  | 从一个矩形区域添加一个内部链接到指定的页面                   |
| addPage(page)                                                | 添加一个页面到这个PDF 文件，该页面通常从 PdfFileReader 实例获取 |
| getNumpages()                                                | 页数                                                         |
| getPage(pageNumber)                                          | 从这个 PDF 文件中检索一个编号的页面                          |
| insertBlankPage(width=None,height=None,index=0)              | 插入一个空白页面到这个PDF文件并返回它，如果没有指定页面大小，就使用最后一页的大小 |
| insertPage(page,index=0)                                     | 在这个 PDF 文件中插入一个页面，该页面通常从 PdfFileReader 实例获取 |
| removeLinks()                                                | 从次数出中删除连接盒注释                                     |
| removeText(ignoreByteStringObject = False)                   | 从这个输出中删除图像                                         |
| write(stream)                                                | 将添加到此对象的页面集合写入 PDF 文件                        |
例子
分割文档（取第五页之后的页面），取第五页之后的页面，将test.pdf第五页之后的页面分割保存到copy.pdf。
```python
import PyPDF2
    from PyPDF2 import PdfFileReader
    from PyPDF2 import PdfFileWriter

def splitPdf():
    readFile = 'test.pdf'
    outFile = 'copy.pdf'
    pdfFileWriter = PdfFileWriter()
    # 获取 PdfFileReader 对象
    pdfFileReader = PdfFileReader(open(readFile, 'rb'))
    # 文档总页数
    numPages = pdfFileReader.getNumPages()
    #如果pdf页数大于5，再分割
    if numPages > 5:
        # 从第五页之后的页面，输出到一个新的文件中，即分割文档
        for index in range(5, numPages):
            pageObj = pdfFileReader.getPage(index)
            pdfFileWriter.addPage(pageObj)
            # 添加完每页，再一起保存至文件中
        pdfFileWriter.write(open(outFile, 'wb'))
splitPdf()
```
    
编程要求
现有一份来自黑客组织的PDF新闻稿step2/1.pdf。

请你对1.pdf稿件解析元信息，得出黑客信息，给警方提供线索。

在右侧编辑器中有一个Evidence函数，它有一个参数path，代表这个PDF的路径，或者是另一个类似的PDF文件的路径，它们的区别仅在于元数据上。

请你在这个函数中读取指定新闻稿的元数据，并将其按照<属性名> : <属性值>的格式打印出来。

注意：从PDF中读取的属性名会包含一些非字母符号，请在显示之前去掉这些符号。如果不知道有哪些符号，可以先输出一下原始的内容观察一下。

测试数据由评测系统读取并传递给Evidence函数，期间产生的输出将会与规定的输出进行比较，详细要求请见测试说明。


测试说明
应该得到的是：

Author : miao chunyu

Creator : Microsoft® Word 2013

CreationDate : D:20200202141604+08’00’

ModDate : D:20200202141604+08’00’

Producer : Microsoft® Word 2013

即测试集1的预期输出。

[Python 深入浅出 - PyPDF2 处理 PDF 文件](https://blog.csdn.net/xingxtao/article/details/79056341)

[利用python获取pdf文件元数据](https://blog.csdn.net/xuandao_ahfengren/article/details/85038089)

## 第3关：图像取证
### 任务描述
本关任务：编写一个能读取图像Exif头的小程序。

###  相关知识
警方通过某种渠道得到了一张照片，想知道照片拍摄位置，确定黑客的活动范围后将其逮捕。基本思路是，调用Python中的exifread模块的exifread.process_file函数，提取图像文件中的Exif头信息。

### 编程要求
现有一份来自黑客组织的泄露的照片step3/1.jpg。

请你对1.jpg相片解析，得出黑客信息，给警方提供线索。

请你在这个函数中读取指定相片的Exif头，并将其按照<属性名>: <属性值>的格式打印出来。

测试数据由评测系统读取并传递给Evidence函数，期间产生的输出将会与规定的输出进行比较，详细要求请见测试说明。


### 测试说明
应该得到的是：

具体型号: MI 6

图像软件: sagit-user 9 PKQ1.190118.001 9.10.17 release-keys

拍摄时间: 2019:12:10 11:56:45

GPS纬度: [22, 30, 45963/1250] N

GPS经度: [114, 2, 280679/10000] E

品牌信息: Xiaomi

即测试集1的预期输出。

[python Exifread, PIL練習 抽出圖片元數據](https://self.jxtsai.info/2016/09/python-exifread-pil.html)

[python第三方库之exifread库使用](https://blog.csdn.net/weixin_42218582/article/details/90732231)