import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from PyPDF2 import PdfFileReader, PdfFileWriter
import pdfkit
import os
import time
import random
import shutil


#初始url
base_url = 'https://python3-cookbook.readthedocs.io/zh_CN/latest/'
# 模板html 用于生成pdf
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""

book_name = ""
chapter_info = []

def parse_title_and_url(html):
    soup = BeautifulSoup(html, 'lxml')
    # 获取书名
    global book_name
    book_name = soup.find('div', class_ ='wy-side-nav-search').a.content
    menu = soup.find_all('div', class_ = 'toctree-wrapper compound')

    chapters = menu[0].ul.find_all('li', class_='toctree-l1')

    for chapter in chapters:
        info = {}
        #获取一级标题和url
        info['title'] = chapter.a.text.replace('/', '').replace('*', '')
        info['url'] = base_url + chapter.a.get('href')
        info['child_chapters'] = []

        #获取二级标题和url
        if chapter.ul is not None:
            child_chapters = chapter.ul.find_all('li')
            for child in child_chapters:
                url = child.a.get('href')
                if '#' not in url:
                    info['child_chapters'].append({
                        'title': child.a.text.replace('/', '').replace('*', ''),
                        'url': base_url + child.a.get('href'),
                    })
        chapter_info.append(info)


def get_one_page(url):
    ua = UserAgent()
    headers = {"UserAgent": ua.random}
    data = requests.get(url, headers= headers)
    time.sleep(random.random() + 1)
    return data.content

def get_content(url):
    """
    解析URL
    :param url:目标url
    :return: html
    """
    html = get_one_page(url)
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div', attrs={'itemprop': 'articleBody'})
    #print(content)
    html = html_template.format(content=content)
    #time.sleep(10)
    return html

def save_pdf(html, filename):
    """
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }

    pdfkit.from_string(html, filename, options=options)


def parse_html_to_pdf():
    try:
        for chapter in chapter_info:
            ctitle = chapter['title']
            url = chapter['url']
            # 文件夹不存在则创建（多级目录）
            dir_name = os.path.join(os.path.dirname(__file__), 'gen', ctitle)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)

            html = get_content(url)

            pdf_path = os.path.join(dir_name, ctitle + '.pdf')
            save_pdf(html, os.path.join(dir_name, ctitle + '.pdf'))

            childeren = chapter['child_chapters']
            if childeren:
                for child in childeren:
                    html = get_content(child['url'])
                    pdf_path = os.path.join(dir_name, child['title'] + '.pdf')
                    save_pdf(html, pdf_path)
    except Exception as e:
        print(e)


def merge_pdf(infnList, bookname):
    pagenum = 0
    pdf_output = PdfFileWriter()

    for pdf in infnList:
        # 先合并一级目录的内容
        first_level_title = pdf['title']
        dir_name = os.path.join(os.path.dirname(__file__), 'gen', first_level_title)
        padf_path = os.path.join(dir_name, first_level_title + '.pdf')
        pdf_input = PdfFileReader(open(padf_path, 'rb'))
        print(first_level_title)
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        #print(page_count)
        for i in range(0, page_count):
            pageObj = pdf_input.getPage(i)
            pdf_output.addPage(pageObj)
            pdf_output.write(open(bookname, 'ab'))
            #print(pdf_output)
        # 添加书签
        parent_bookmark = pdf_output.addBookmark(
            first_level_title, pagenum=pagenum)

        # 页数增加
        pagenum += page_count

        # 存在子章节
        if pdf['child_chapters']:
            for child in pdf['child_chapters']:
                second_level_title = child['title']
                padf_path = os.path.join(dir_name, second_level_title + '.pdf')

                pdf_input = PdfFileReader(open(padf_path, 'rb'))
                
                # 获取 pdf 共用多少页
                page_count = pdf_input.getNumPages()
                #print(page_count)
                for i in range(page_count):
                    pdf_output.addPage(pdf_input.getPage(i))
                    pdf_output.write(open(bookname, 'ab'))                

                # 添加书签
                pdf_output.addBookmark(
                    second_level_title, pagenum=pagenum, parent=parent_bookmark)
                # 增加页数
                pagenum += page_count

    # 合并
    pdf_output.write(open(bookname, 'ab'))
    # 删除所有章节文件
    shutil.rmtree(os.path.join(os.path.dirname(__file__), 'gen'))

if __name__ == "__main__":
    bookname = "/home/mikasa/github_repositories/spiders/爬取在线教程转成pdf/Python_Cookbook.pdf"
    data = get_one_page(base_url)
    parse_title_and_url(data)
    # parse_html_to_pdf()
    merge_pdf(chapter_info, bookname)


