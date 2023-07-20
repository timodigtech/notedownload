from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://xyq.cbg.163.com/cgi-bin/login.py?next_url=%2Fequip%3Fs%3D378%26eid%3D202306032200113-378-J7F8CEKEQWBH%26equip_refer%3D29%26view_loc%3Dmy_collect%26from_shareid%3D2307171900128-6FF2DWP0VHWHXFBC&server_id=378&act=do_anon_auth")
    page.goto("https://xyq.cbg.163.com/cgi-bin/show_login.py?area_id=55&server_name=%E7%81%B5%E9%9A%90%E5%AF%BA&area_name=%E6%B5%99%E6%B1%9F2%E5%8C%BA&server_id=378&act=show_login&return_url=https%3A%2F%2Fxyq.cbg.163.com%2Fcgi-bin%2Fequip_detail.py%3Fs%3D378%26eid%3D202306032200113-378-J7F8CEKEQWBH%26equip_refer%3D29%26view_loc%3Dmy_collect%26from_shareid%3D2307171900128-6FF2DWP0VHWHXFBC%26s%3D378%26eid%3D202306032200113-378-J7F8CEKEQWBH%26equip_refer%3D29%26view_loc%3Dmy_collect%26from_shareid%3D2307171900128-6FF2DWP0VHWHXFBC")
    page.goto("https://xyq.cbg.163.com/cgi-bin/login.py?act=do_fake_role_login")
    page.goto("https://xyq.cbg.163.com/cgi-bin/login.py?act=show_role_select_page")
    page.get_by_role("link", name="我知道了").click()
    page.get_by_role("link", name="进 入").click()
    page.get_by_role("link", name="我的藏宝阁").click()
    page.get_by_role("link", name="我的收藏").click()
    page.get_by_role("row", name="物品 4737260 173 ￥4300.00 上架中 本服 --- 提醒设置 取消收藏").get_by_role("link", name="物品").click()
    page.get_by_role("cell", name="气血：2532").click()
    page.get_by_role("cell", name="气血：2532").click()
    page.get_by_text("技能").click()
    page.get_by_role("cell", name="140 冥想").get_by_text("140").click()
    page.get_by_text("坐骑").click()
    page.get_by_role("cell", name="云魅仙鹿").click()
    page.get_by_role("cell", name="魔力").click()
    page.get_by_role("cell", name="祥瑞总数").click()
    page.get_by_role("cell", name="流云玉佩").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
