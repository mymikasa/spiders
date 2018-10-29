import json
from Crypto.Cipher import AES
import base64
import requests
import binascii
import math
import codecs
import random
# from fake_useragent import UserAgent


# JSON.stringify(i9b), bnY2x(["流泪", "强"]), bnY2x(ZQ8I.md), bnY2x(["爱心", "女孩", "惊恐", "大笑"]))

def generate_random_strs(length):
    """
    返回一个长度为16的字符串，也就是第一个参数JSON.stringify(i9b)
    :param length:
    :return:
    """
    base_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return "".join(random.sample(base_str, 16))


def add_to_16(text):
    """
    如果待加密的文本长度小于16，则将其填充到16位
    :param value:要加密的文本
    :return:
    """
    pad = 16 - len(text) % 16  # 对长度不是16倍数的字符串进行补全，然后在转为bytes数据
    try:  # 如果接到bytes数据（如第一次aes加密得到的密文）要解码再进行补全
        text = text.decode()
    except:
        pass
    text = text + pad * chr(pad)
    try:
        text = text.encode()
    except:
        pass
    return text


def encrypt_oracle(data, key):
    """
    AES 加密
    :param data:
    :param key:
    :return:
    """
    iv = '0102030405060708'
    # 初始化加密器
    aes = AES.new(key, AES.MODE_CBC, iv)
    # 先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(data))
    # 用base64进行编码，返回byte字符串
    encrypt_str = base64.b64encode(encrypt_aes)
    # 对byte字符串按utf-8进行解码
    encrypt_text = encrypt_str.decode('utf-8')
    return encrypt_text


def rsa_encrypt(random_strs, key, f):
    """
    # RSA加密
    :param random_strs:
    :param key:
    :param f:
    :return:
    """
    # 随机字符串逆序排列
    string = random_strs[::-1]
    # 将随机字符串转换成byte类型数据
    text = bytes(string, 'utf-8')
    seckey = int(codecs.encode(text, encoding='hex'),
                 16)**int(key, 16) % int(f, 16)
    # 返回整数的小写十六进制形式
    return format(seckey, 'x').zfill(256)


def get_params(page, song_id):
    """
    # msg = '{"rid":"R_SO_4_461525011","offset":"0","total":"True","limit":"100","csrf_token":""}'
    :param page:
    :return:
    """
    # 偏移量
    offset = (page - 1) * 20
    # 构造offset
    msg = '{"offset":' + str(offset) + \
        ',"total":"True","limit":"20","csrf_token":""}'
    key = '0CoJUm6Qyw8W8jud'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    e = '010001'
    enc_text = encrypt_oracle(msg, key)
    i = generate_random_strs(16)

    # # 两次AES加密之后得到params的值
    enc_text = encrypt_oracle(enc_text, i)
    # # RSA加密之后得到encSecKey的值
    enc_seckey = rsa_encrypt(i, e, f)
    return enc_text, enc_seckey


def get_comments_json(url, data):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'WM_TID=36fj4OhQ7NdU9DhsEbdKFbVmy9tNk1KM; _iuqxldmzr_=32; _ntes_nnid=26fc3120577a92f179a3743269d8d0d9,1536048184013; _ntes_nuid=26fc3120577a92f179a3743269d8d0d9; __utmc=94650624; __utmz=94650624.1536199016.26.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); WM_NI=2Uy%2FbtqzhAuF6WR544z5u96yPa%2BfNHlrtTBCGhkg7oAHeZje7SJiXAoA5YNCbyP6gcJ5NYTs5IAJHQBjiFt561sfsS5Xg%2BvZx1OW9mPzJ49pU7Voono9gXq9H0RpP5HTclE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed5cb8085b2ab83ee7b87ac8c87cb60f78da2dac5439b9ca4b1d621f3e900b4b82af0fea7c3b92af28bb7d0e180b3a6a8a2f84ef6899ed6b740baebbbdab57394bfe587cd44b0aebcb5c14985b8a588b6658398abbbe96ff58d868adb4bad9ffbbacd49a2a7a0d7e6698aeb82bad779f7978fabcb5b82b6a7a7f73ff6efbd87f259f788a9ccf552bcef81b8bc6794a686d5bc7c97e99a90ee66ade7a9b9f4338cf09e91d33f8c8cad8dc837e2a3; JSESSIONID-WYYY=G%5CSvabx1X1F0JTg8HK5Z%2BIATVQdgwh77oo%2BDOXuG2CpwvoKPnNTKOGH91AkCHVdm0t6XKQEEnAFP%2BQ35cF49Y%2BAviwQKVN04%2B6ZbeKc2tNOeeC5vfTZ4Cme%2BwZVk7zGkwHJbfjgp1J9Y30o1fMKHOE5rxyhwQw%2B%5CDH6Md%5CpJZAAh2xkZ%3A1536204296617; __utma=94650624.1052021654.1536048185.1536199016.1536203113.27; __utmb=94650624.12.10.1536203113',
        'Host': 'music.163.com',
        'Referer': 'http://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/66.0.3359.181 Safari/537.36'
    }
    try:
        r = requests.post(url, headers=headers, data=data)
        r.encoding = 'utf-8'
        if r.status_code == 200:
            return r.json()

    except:
        print("抓取失败")


def hotcomments(html, song_name, i, pages, total, filepath):
    """

    :param html:
    :param song_name:
    :param i:
    :param pages:
    :param total:
    :param filepath:
    :return:
    """
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write("正在获取歌曲{}的第{}页评论,总共有{}页{}条评论！\n".format(
            song_name, i, pages, total))
    print("正在获取歌曲{}的第{}页评论,总共有{}页{}条评论！\n".format(song_name, i, pages, total))

    # 热评编号
    count = 1
    if 'hotComments' in html:
        for item in html['hotComments']:
            user = item['user']
            print("热门评论{}: {} : {}    点赞次数: {}".format(
                count, user['nickname'], item['content'], item['likedCount']))
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write("热门评论{}: {} : {}   点赞次数: {}\n".format(
                    count, user['nickname'], item['content'], item['likedCount']))
                # 回复评论
                if len(item['beReplied']) != 0:
                    for reply in item['beReplied']:
                        # 提取发表回复评论的用户名
                        replyuser = reply['user']
                        print("回复：{} : {}".format(
                            replyuser['nickname'], reply['content']))
                        f.write("回复：{} : {}\n".format(
                            replyuser['nickname'], reply['content']))
            count += 1


def comments(html, song_name, i, pages, total, filepath):
    """

    :param html:
    :param song_name:
    :param i:
    :param pages:
    :param total:
    :param filepath:
    :return:
    """
    with open(filepath, 'a', encoding='utf-8') as f:
        try:
            f.write("\n正在获取歌曲{}的第{}页评论,总共有{}页{}条评论！\n".format(
                song_name, i, pages, total))
        except:
            pass
    try:
        print("\n正在获取歌曲{}的第{}页评论,总共有{}页{}条评论！\n".format(
            song_name, i, pages, total))
    except:
        pass
    # 全部评论
    count = 1
    try:
        for item in html['comments']:
            # 提取发表评论的用户名
            user = item['user']
            print("全部评论{}: {} : {}    点赞次数: {}".format(
                count, user['nickname'], item['content'], item['likedCount']))
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write("全部评论{}: {} : {}   点赞次数: {}\n".format(
                    count, user['nickname'], item['content'], item['likedCount']))
                # 回复评论
                if len(item['beReplied']) != 0:
                    for reply in item['beReplied']:
                        # 提取发表回复评论的用户名
                        replyuser = reply['user']
                        print("回复：{} : {}".format(
                            replyuser['nickname'], reply['content']))
                        f.write("回复：{} : {}\n".format(
                            replyuser['nickname'], reply['content']))
            count += 1
    except:
        pass


def spider():
    # id
    song_id = 461525011
    song_name = '起风了'
    filepath = song_name + '.txt'
    page = 1
    params, encSecKey = get_params(page, song_id)
    # api地址
    url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_' + \
        str(song_id) + '?csrf_token='
    data = {
        'params': params,
        'encSecKey': encSecKey
    }
    # 第一页评论内容
    html = get_comments_json(url, data)
    # 评论总数
    total = html['total']
    # 总页数
    pages = math.ceil(total / 20)
    hotcomments(html, song_name, page, pages, total, filepath)
    comments(html, song_name, page, pages, total, filepath)

    # 获取歌曲的全部评论
    page = 2
    while page <= pages:
        params, encSecKey = get_params(page, song_id)
        data = {'params': params, 'encSecKey': encSecKey}
        html = get_comments_json(url, data)
        comments(html, song_name, page, pages, total, filepath)
        page += 1


if __name__ == "__main__":
    spider()
