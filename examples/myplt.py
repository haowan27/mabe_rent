import matplotlib.pyplot as plt

# 准备数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 绘制图表
plt.plot(x, y, marker='o', linestyle='-')

# 添加标题和坐标轴标签
plt.title('Prime Numbers')
plt.xlabel('Index')
plt.ylabel('Value')

# 展示图表
plt.show()