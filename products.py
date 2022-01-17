import os # operating system

#读取档案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue  # 跳到下一个回圈
			name, price = line.strip().split(',')
			products.append([name, price])
	return(products)

# 请使用者输入
def user_input(products):
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
	return products

# 印出所有购买记录
def print_products(products):
	for p in products:
		print(p[0], '的价格是', p[1])

# 写入档案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:    # with 自动close
		f.write('商品,价格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')   # ','换格， '\n'换行


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 检查文件是否存在
		print('找到文件!')
		products = read_file(filename)
	else:
		print('找不到文件')

	products = user_input(products)  
	print_products(products)
	write_file('products.csv', products)

main()

# 理想的function应该只做一件事。
# refactor 重构



