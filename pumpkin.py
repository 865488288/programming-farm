# 2026.08.16 11:12版本：基于集合删坐标模式的快速种大南瓜
from config import *			# 导入配置文件（包含 L = 世界大小 及常用函数等）


def plant_pumpkin():			# 定义操作：耕地 + 种南瓜
	if get_ground_type() == Grounds.Grassland:	# 若地块为草地
		till()					# 耕地
	x,y = get_pos_x(),get_pos_y()	# 获取当前位置坐标
	if get_entity_type() != Entities.Pumpkin:	# 若当前位置没有南瓜
		entity_dict.add((x,y))	# 将当前位置坐标添加到集合中
		harvest()
		plant(Entities.Pumpkin)		# 种植南瓜
		Watering()					# 浇水
entity_dict = set()	# 创建空集合储存坏南瓜位置

while True:

	while entity_dict:	# 如果集合不为空，则说明有南瓜需要收获
		for pos in list(entity_dict):	# 遍历集合中的每个坐标
			G1(pos[0], pos[1])	# 移动到集合坐标
			# 如果当前位置有南瓜、可以收获	从集合中移除该坐标
			if get_entity_type() == Entities.Pumpkin  and  can_harvest():
				entity_dict.remove(pos)

			# 如果当前位置有南瓜、不可以收获、还有别的坏南瓜  退出判断	
			elif get_entity_type() == Entities.Pumpkin  and  not can_harvest()  and  len(entity_dict) > 1:
				pass

			# 如果当前位置是死南瓜	# 种植南瓜
			elif get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)		

			# 否则	执行循环判断收获
			else:	
				while not can_harvest():
					use_item(Items.Fertilizer) 
					# do_a_flip() 	# 让无人机做一次翻转！
					if get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)
					if can_harvest():
						harvest()
						entity_dict.remove(pos)
						break

	if can_harvest() and not entity_dict :	# 如果可以收获
		harvest()	# 收获南瓜		

	snake_traverse(plant_pumpkin,6,6,5,5)	# 蛇形遍历整个农场，逐格耕作并种植南瓜





# from config import *			# 导入配置文件（包含 L = 世界大小等定义）
# clear()							# 清空农场，重置状态

# while True:	# 蛇形遍历整个农场：逐列耕作并种植南瓜
# 	L = 6
# 	for i in range(L):					# 遍历每一列（共 L 列）
# 		if get_pos_x() % 2 == 0:		# 偶数列：从下往上蛇形走

# 			for j in range(L):			# 遍历当前列中的每一行（共 L 行）
# 				if get_ground_type() == Grounds.Grassland:
# 					till()					# 耕地
# 				plant(Entities.Pumpkin)	# 种植南瓜

# 				if j < L - 1:			# 如果不是最后一行，则向北移动
# 					move(North)
# 				else:
# 					move(East)			# 如果是最后一行，则向东移动进入下一列


# 		else:							# 奇数列：从上往下蛇形走
# 			for j in range(L):			# 遍历当前列中的每一行（共 L 行）
# 				if get_ground_type() == Grounds.Grassland:
# 					till()					# 耕地
# 				plant(Entities.Pumpkin)	# 种植南瓜

# 				if j < L - 1:			# 如果不是最后一行，则向南移动
# 					move(South)
# 				else:
# 					move(East)			# 如果是最后一行，则向东移动进入下一列

# 	G1(0,0)
# 	if can_harvest():
# 		harvest()



# 2026.08.14 版本：将蛇形遍历农场的操作封装为 snake_traverse() 函数，
# 并将耕作和种植南瓜的操作封装为 plant_pumpkin() 函数，便于调用和修改。

# from config import *			# 导入配置文件（包含 L = 世界大小等定义）
# clear()							# 清空农场，重置状态

# def plant_pumpkin():			# 定义操作：耕地 + 种南瓜
# 	if get_ground_type() == Grounds.Grassland:
# 		till()					# 耕地
# 	plant(Entities.Pumpkin)		# 种植南瓜

# while True:
# 	G1(0,0)						# 回到起点
# 	if can_harvest():
# 		harvest()
# 	snake_traverse(plant_pumpkin,6)	# 蛇形遍历整个农场，逐格耕作并种植南瓜

