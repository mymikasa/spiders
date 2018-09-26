# -*- coding: utf-8 -*-

"""

"""
import scrapy
from fake_useragent import UserAgent
import time
from douban_spider.items import DoubanSpiderItem
ua = UserAgent()

class MovieReviewSpider(scrapy.Spider):
    name = 'movie_review'
    allowed_domains = ['douban.com', 'account.douban.com', 'movie.douban.com']
    start_urls = ['http://www.douban.com/']


    #请求头信息
    # headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    #     'Connection': 'keep-alive',
    #     'Host': 'accounts.douban.com',
    #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",    
    #     }
    formdata = {
        'form_email':'2592528761@qq.com',
        'form_password':'951224@zang',
        'login':'登录',
        'redir': 'https://movie.douban.com/',
        'source': 'None'
    }

    def start_requests(self):
        yield scrapy.Request(url='https://www.douban.com/accounts/login',
                            # headers = self.headers,
                            meta = {'cookiejar' : 1},
                            callback = self.parse_login)
        

    def parse_login(self, response):
        """
        填写表单参数,网页中直接从网页中提取即可
        """
        if 'captcha_image' in str(response.body):
            print('Copy the link')
            link = response.xpath('//img[@class="captcha_image"]/@src').extract()[0]
            print(link)

            captcha_solution = input('captcha-solution:')
            captcha_id = response.xpath("//input[@name='captcha-id']/@value").extract()[0]
            self.formdata['captcha-solution'] = captcha_solution
            self.formdata['captcha-id'] = captcha_id

        
        yield scrapy.FormRequest.from_response(response,
                                                formdata = self.formdata,
                                                # headers = self.headers,
                                                meta = {'cookiejar':response.meta['cookiejar']},
                                                callback = self.after_login
                                                )

    def after_login(self, response):
        print(response.status)
        time.sleep(3)
        # self.headers['Host'] = "www.douban.com"
        for i in range(0, 25):
            time.sleep(5)
            yield scrapy.Request(
                                url = 'https://movie.douban.com/subject/26985127/comments?start={}&limit=20&sort=new_score&status=P'.format(i * 20),
                                meta = {'cookiejar':response.meta['cookiejar']},
                                # headers= self.headers,
                                dont_filter=True,
                                callback = self.parse,
            )

    def parse(self, response):
        print(response.status)
        data = response.xpath('//*[@id="comments"]/div/div[2]/p/span/text()').extract()
        print(data)
        comments = DoubanSpiderItem()
        comments['data'] = data
        yield comments
