print('这里可以查询你的成绩变化情况')
name = input('请输入你的姓名:')
s1 = float(input('你好%s,请输入去年的成绩:' % name))
s2 = float(input('请输入今年的成绩:'))
r = ((s2-s1)/s1)*100
if r > 0:
    print('恭喜你!%s,你的成绩提升了%.1f%%' % (name,r) )
else:
    print('很遗憾,%s,你的成绩下降%.1f%%,继续努力'% (name,r))
        

