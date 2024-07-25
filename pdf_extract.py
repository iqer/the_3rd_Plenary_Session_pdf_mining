import pathlib

import pdfplumber

dir_path = pathlib.Path(__file__).parent
file_name = 'china_gov_decision.pdf'
file_path = dir_path.joinpath(file_name)

text_list = []

with pdfplumber.open(file_path) as pdf:
    for i in range(len(pdf.pages)):
        cur_page = pdf.pages[i]
        cur_text = cur_page.extract_text()
        if i == 0:
            index = cur_text.find("要要求求")
            cur_text = cur_text[index + 5:]
        cur_text = cur_text.removeprefix(
            '7/24/24, 12:13 PM 中共中央关于进⼀步全⾯深化改⾰ 推进中国式现代化的决定_中央有关⽂件_中国政府⽹\n')
        index = cur_text.find('https://www.gov.cn/zhengce/202407/content_6963770.htm')
        cur_text = cur_text[:index]
        text_list.append(cur_text)

article = ''.join(text_list)

with open('article.text', 'w') as f:
    f.write(article)
