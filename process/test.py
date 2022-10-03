import re
reg = {'序号' : r"\*\*[一二两三四五六七八九十○零百千0-9１２３４５６７８９０]+.*", '分隔符' : "[:/\\;；,，\(（\[]"}
line = "分类:同人/种马"
ts = re.split(reg["分隔符"], line.replace("分类", "", 1).strip(" :："))
print(ts)