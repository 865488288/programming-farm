# 向日葵种植

from config import *			# 导入配置文件（包含 L = 世界大小等定义）



sunflower_size = {}		# 创建空字典 用来存储向日葵坐标和相应的大小

# 种植向日葵 并把 坐标 大小 写入字典
def plant_sunflower(): 
	
	if get_ground_type() == Grounds.Grassland:	# 若地块为草地
		harvest()   # 收获
		till()      # 耕地

	plant(Entities.Sunflower)	# 种植向日葵
	Watering(0.8)               # 浇水
	x,y = get_pos_x(),get_pos_y()	# 设定x,y为当前坐标位置
	sunflower_size[x,y] = measure()		# 把当前坐标为索引 向日葵大小为值 写入字典

while True :	# 循环执行
	# 蛇形环绕并调用执行plant_sunflower()
	snake_traverse(plant_sunflower,6,6,0,0)

	# 循环收获最大向日葵
	while sunflower_size :	# 若字典sunflower_size不为空就循环(还有向日葵)

		max_sunflower = None	# 设定最向日葵坐标为空
		max_size = 0			# 设定最大尺寸为0

		# 找出最大向日葵：
		for key in sunflower_size :	# 遍历sunflowe_size 把字典索引带入key执行
			if sunflower_size[key] >= max_size :	# 若当前索引对应的值大于最大尺寸
				max_size = sunflower_size[key]		# 把当前索引对应的值带入max_size
				max_sunflower = key					# 把当前索引带入max_sunflower

		# 定位到最大向日葵并收获：

		x,y = max_sunflower	# 把索引位置带入x,y
		G0(x,y)	# 快速定定位到向日葵位置

		if can_harvest() :	# 若可以收获
			harvest()		# 收获
			sunflower_size.pop(max_sunflower)	# 删除字典当前坐标索引
			Watering(0.8)
		else :
			use_item(Items.Fertilizer) 	# 施肥
			do_a_flip() 				# 让无人机做一次翻转！



