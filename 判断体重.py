print('以下可以测试你的健康状况')
name = input('请输入你的姓名:')
height = float(input('请输入你的身高(m):'))
weight = float(input('请输入你的体重(kg):'))
bmi = float(weight/(height*height))
print('你的BMI指数为%.1f,' % bmi)
if bmi < 18:
	print('%s, 你目前偏瘦' % name);
elif bmi <= 24:
	print('%s, 你目前正常' % name);
elif bmi < 28:
	print('%s, 你目前过重' % name);
elif bmi >= 28:
	print('%s, 你目前肥胖' % name);

	
