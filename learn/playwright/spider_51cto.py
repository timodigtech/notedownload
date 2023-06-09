from playwright.sync_api import Playwright, sync_playwright, expect
import time
import csv

def run(playwright: Playwright) -> None:
    courseList=[]
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    context.new_page()
    # # 关闭Webdriver属性

    # page = context.new_page()
    # page.goto("https://blog.51cto.com/search/user?uid=15239893&q=playwright+8")
    # time.sleep(2)

    for i in range(55,67):
        time.sleep(1)
        page = context.new_page()
        page.get_by_label()
        page.get_by_role()
        js = """
        Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});
        """
        page.add_init_script(js)
        page.goto("https://blog.51cto.com/search/user?uid=15239893&q=playwright+"+str(i))
        print(i)    
        csspath='div.last>div.m-1>a.m-1-4.fl'
        
        # page.query_selector_all("xpath=//*[@class=first]")[0].click()
        # xpath='/html/body/div[2]/div[2]/ul[1]/li[1]/div[1]/a[1]'
        with page.expect_popup() as page1_info:
            page.locator(csspath).click()
            time.sleep(1)
            courseMap=( i,page1_info.value.title(),page1_info.value.url)
            courseList.append(courseMap)
            print(courseMap)
        # page.get_by_role("link", name="python+playwright 学习-42 离线安装 playwright 环境").click()
        page1 = page1_info.value
        time.sleep(1)
        page1.close()
        page.close()
    
    # page.goto(C"https://blog.51cto.com/search/user?uid=15239893&q=playwright")

    # ---------------------
    context.close()
    browser.close()
    # 把获取到的列表全部写入csv文档，每行一个map
    print("courseList len :",len(courseList))
        
    with open('courses.csv', mode='a+', newline='') as courses_file:
        writer=csv.writer(courses_file)
        writer.writerow(['序号','标题','链接'])
        for i in range(len(courseList)):

            # print(courseList[i][0])
            writer.writerow(courseList[i])
 
        
    
with sync_playwright() as playwright:
    run(playwright)
 
