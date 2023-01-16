# k存储名称，v存储符号
k8=['乾', '兑', '离', '震', '巽', '坎', '艮', '坤']
k64=['乾', '坤', '屯', '蒙', '需', '讼', '师', '比', '小畜', '履', '泰', '否',
     '同人', '大有', '谦', '豫', '随', '蛊', '临', '观', '噬嗑', '贲',  '剥', 
     '复', '无妄', '大畜', '颐', '大过', '坎', '离','咸', '恒', '遁', '大壮', 
     '晋', '明夷', '家人', '睽','蹇', '解', '损', '益', '夬', '姤', '萃', 
     '升', '困', '井','革', '鼎', '震','艮', '渐', '归妹','丰', '旅', '巽', '兑',
     '涣', '节', '中孚','小过', '既济', '未济']
v8=[]
for i in range(2630,2638):
    expression = "u'\\u" + str(i) + "'"
    v8.append(eval(expression))
v64=[]
for i in range(19904,19968):
    expression = "u'\\u" + str(hex(i))[2:] + "'"
    v64.append(eval(expression))
print('八卦')
print("\t".join(["".join([v,k]) for k,v in zip(k8[:4],v8[:4])]))
print("\t".join(["".join([v,k]) for k,v in zip(k8[4:],v8[4:])]))
print('六十四卦')
for i in range(0,64,8):
    print("\t".join(["".join([v,k]) for k,v in zip(k64[i:i+8],v64[i:i+8])]))
