import requests
from lxml import html
import re

# 指定目标 URL
url = 'https://www.zzxx.org/xs/24882/16016118.html'

xpath_expression = '//div[@class="bookname"]/h1'  # 指定的 XPath 表达式

def get_novel_title_text(url):
    # 发送 GET 请求
    response = requests.get(url)
    # 检查响应状态码
    if response.status_code == 200:
        # 解析 HTML 内容
        page = html.fromstring(response.content)
        # 使用 XPath 表达式提取信息 
        
        result_tilte= page.xpath('//div[@class="bookname"]/h1')
        result_text = page.xpath('//*[@id="content"]')
        # 检查提取结果
        if result_text:
            # 通过索引 [0] 获取第一个匹配结果的文本
            # title_content=result_tilte[0]
            content = result_text[0].text_content()
            text_content=re.sub(r'\s+', '\n', content)
            re_content=result_tilte[0].text_content()+'\n'+'\n'+text_content
        else:
            print("未找到匹配的结果")
    else:
        print("请求失败，状态码：", response.status_code)
        
        # 指定文件名和文件路径
    file_name = "output.txt"

    # 将文本信息写入文件
    with open(file_name, 'a') as file:
        file.write(re_content)



start_num = 16016118
end_num = 16016125
for i in range(start_num, end_num + 1):
    new_url = url.replace(str(start_num), str(i))
    get_novel_title_text(new_url)

