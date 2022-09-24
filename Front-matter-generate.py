# 为内容添加Front-matter

"""
功能
- 根据文件名生成标题
- 根据文件目录生成分类和标签
- 如果文章以`转载`, `zhuanzai`开头，自动加上转载标识
- 保留所有 ===分割号后的自定义分类和标签
- 不为生成过的文件重新生成 & 自定义排除文件夹or文件
"""

"""
---
title: Hello World
categories:
- Diary
tags:
- PS3
- Games
---
"""




import os
import re
def fm_dev(rpath, tname, oldf = []): # 生成Front-matter
    rpath = rpath.split(os.path.sep)
    tit = "title: " + tname + "\n"
    tmpl = ["---\n", tit, "categories:\n", "tags:\n"]
    tmpl = tmpl + oldf + ["---\n"]

    if rpath[0] == '.':
        tmpl.insert(tmpl.index("categories:\n") + 1,
                    "- Life\n")  # 根目录下所有文件处于 Life 分类
    else:
        tmpl.insert(tmpl.index("categories:\n") + 1, "- " + rpath[0] + "\n")
    flag = 0
    """路径中剩下的部分作为标签"""
    if len(rpath) > 1:
        for i in range(1, len(rpath)):
            print(rpath[i])
            flag = 0
            text = rpath[i]
            text = text.replace("年", "/").replace("月",
                                                  "/").replace("日", " ").replace("-", "/").strip()
            day = re.search(r"\d{4}/\d{1,2}(/\d{1,2})*", text)
            if day:
                if "- " + day.group() + "\n" not in tmpl:
                    tmpl.insert(tmpl.index(tit) + 1, "date: " + day.group() + "\n")
                flag = 1
                # print(tmpl)
            st = ["扫书汇总"]
            for sta in st:
                t = re.search(sta, text)
                if t:
                    flag = 1
                    if "- " + t.group() + "\n" not in tmpl:
                        tmpl.insert(tmpl.index("tags:\n") + 1, "- " + t.group() + "\n")
                    # print(tmpl)
            if flag == 0:
                if "- " + rpath[i] + "\n" not in tmpl:
                    tmpl.insert(tmpl.index("tags:\n") + 1, "- " + rpath[i] + "\n")

    if rpath[0] == 'Net-excerpt':
        tmpl.insert(len(tmpl) - 1, "reprint: true\n")  # 主题内自定义设置，转载文章标记
    print(tmpl)

    return tmpl


fapath = os.path.split(os.path.realpath(__file__))[0]

for folderName, subfolders, filenames in os.walk(fapath):
    for filename in filenames:
        # 获取前缀（文件名称）
        tname = os.path.splitext(filename)[0]
        if os.path.splitext(filename)[-1][1:] == "md":

            rpath = os.path.relpath(folderName, fapath)  # 获取相对路径
            filepath = rpath + "\\" + filename  # 获取文件的相对路径
            print(filepath)
            TFile = open(filepath, 'r', encoding='utf-8')  # 打开文件(只读)
            conntent = TFile.readlines()  # 按行读取
            TFile.close()  # 关闭文件
            try:
                conntent[0] == "---\n"
            except IndexError:
                print(filepath + " 空文件错误")  # 测试路径是否正确
                continue
            if (conntent[0] == "---\n"):  # 处理过的
                continue
            else:
                conntent = fm_dev(rpath, tname) + ["\n\n"] + conntent
                TFile = open(filepath, 'w', encoding='utf-8')
                TFile.writelines(conntent)
                TFile.close()
