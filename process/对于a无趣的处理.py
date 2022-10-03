"""
主要处理.origin
按照a无趣的书写习惯转义Markdown
"""

from gettext import find
import os
import re
from tkinter import font
fapath = "../.origin"
gpath = "../YY向"


replace_ = ["绿nu", "真-nu才", "自lv", "lv文", "心理BT", "基佬文", "绿文", "ying视", "后gong", "自绿"]
_replace = ["绿", "男主奴才", "绿", "绿", "心里变态", "gay", "绿", "影视", "后宫", "绿"]
_not_it = [r"^划到", r"^膈应"]

def dev(filepath):
    TFile = open(filepath, 'r', encoding='utf-8')  # 打开文件(只读)
    content = TFile.readlines()  # 按行读取
    l = 0  # 上一章的开始
    r = 0  # 本章的开始
    cnt = 0
    fcontent = '' # 新内容
    fname = '' # 文件名称
    lfpath = '' # 具体目录是推书还是排雷
    con = "\n> 内容整理自： 微信公众号-纯爱后宫小说" # 版权
    tmfm = [] # front-matter
    reg = {'序号' : r"\*\*[一二两三四五六七八九十○零百千0-9１２３４５６７８９０]+.*", '分隔符' : "[:/\\;；,，\(（\[]"}

    ts = [''] # 分类
    for i in range(len(content)):
        line = content[i] 
        if re.search(reg['序号'], line):
            r = i + 2
            if r != l:
                fcontent = ''.join(tmfm) + "# " + fname + "\n" +''.join(content[l + 2: r - 2]) + con
                # print(fcontent)
                tf = open(gpath + '/' + lfpath + '/' + fname +'.md', 'w', encoding='utf-8')
                tf.writelines(fcontent)
                tf.close()
            # 初始化
            flag = 0
            fname = content[r].strip("* \n").replace(":","：").replace("/","&")
            tmfm = ["---\n", "title: " + fname + "\n", "categories:\n", "- YY向\n", "tags:\n", "---\n"]
            ts = []
            if fname.find("排雷") != -1:
                lfpath = "排雷"
            else :
                lfpath = "扫书"
            tmfm.insert(tmfm.index("tags:\n") + 1, "- " + lfpath + "\n")
            l = r
        if re.search(r"^分类", line.strip()):
            for j in range(len(replace_)):
                line = line.replace(replace_[j], _replace[j])
            ts = re.split(reg["分隔符"], line.replace("分类", "", 1).strip(" :："))
            if type(ts) == type([]):
                for sta in ts:
                    for rega in _not_it:
                        if re.search(rega, sta): flag = 1
                    if not flag:
                        tmfm.insert(tmfm.index("tags:\n") + 1, "- " + sta.strip("\n :：（）?？+")+ "\n")
            elif type(ts) == type(""):
                for rega in _not_it:
                        if re.search(rega, ts): flag = 1
                if not flag:
                    tmfm.insert(tmfm.index("tags:\n") + 1, "- " + ts.strip("\n :：（）?？+") + "\n")
    # 单独处理最后一个
    fcontent = ''.join(tmfm) + "# " + fname + "\n" +''.join(content[r + 2:]) + con
    # print(fcontent)
    tf = open(gpath + '/' + lfpath + '/' + fname +'.md', 'w', encoding='utf-8')
    tf.writelines(fcontent)
    tf.close()
    TFile.close()  # 关闭文件


for folderName, subfolders, filenames in os.walk(fapath):
    for filename in filenames:
        # 获取前缀（文件名称）
        tname = os.path.splitext(filename)[0]
        if tname.find("a无趣") != -1 and os.path.splitext(filename)[-1][1:] == "md":
            rpath = os.path.relpath(folderName, fapath)  # 获取相对路径
            filepath = fapath + rpath + "\\" + filename  # 获取文件的相对路径
            print(filepath)
            dev(filepath)
