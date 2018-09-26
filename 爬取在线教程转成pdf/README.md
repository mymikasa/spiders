## 爬虫抓取一个在线教程并且以将其保存为pdf的格式

主要使用的是wkhtmltopdf,这个库用于将html转化为pdf.本人的机器是ununtu, 所以只在这个机器上进行了测试.其他机器请小伙伴们自行测试.(-.-)   
> sudo apt-get install wkhtmltopdf
### 所需要的爬虫库
因为是一个比较小型的爬虫所以并没有使用框架,只需要安装一下几个库即可.
+ pip install requests        # 用于网络请求
+ pip install beautifulsoup4   # 用于操作html
+ pip install pdfkit  # wkhtmltopdf 的Python封装包
+ pip install PyPDF2    # 用于合并pdf

### 完成情况
![效果](spiders/爬取在线教程转成pdf/res.png)

### 弊端
虽然完成了所需功能,但是却并不实用.经过测试生成的pdf文件实在是太大了.计算机容量比较大的小伙伴们可以尝试一下.
![(^-^)](spiders/爬取在线教程转成pdf/big.png)
