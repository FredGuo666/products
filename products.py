#读取档案
#strip 除掉换行符(/n)
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,价格' in line:
			continue  # 跳到下一个回圈
		name, price = line.strip().split(',')
		products.append([name, price])

print(products)

# 请使用者输入
while True:
	name = input('请输入商品名称:')
	if name == 'q':
		break
	price = input('请输入商品价格:')
	price = int(price)
	# p = []
	# p.append(name)
	# p.append(price)
	# p = [name, price]
	products.append([name, price])
print(products)

# 印出所有购买记录
for p in products:
	print(p[0], '的价格是', p[1])

# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# 写入档案
with open('products.csv', 'w', encoding='utf-8') as f:    # with 自动close
	f.write('商品,价格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')   # ','换格， '\n'换行
