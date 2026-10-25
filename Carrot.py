# clear()


from config import *	# 导入配置文件（包含 L = 世界大小等定义）

def Carrot():
	if get_ground_type() == Grounds.Grassland:
		till()					# 耕地
	if can_harvest():
		harvest()	
	plant(Entities.Carrot)	# 种植胡萝卜
while True:
	# 蛇形遍历：每格执行函数   运行范围   起始坐标
	snake_traverse(Carrot, 8 , 8 , 4 , 4)



# # 耕地
# for i in range(get_world_size()):
# 	for i in range(get_world_size()):
# 		till()
# 		plant(Entities.Carrot)	# 首次种植
# 		move(North)
# 	move(East)

# # 种植
# while True:
# 	for i in range(get_world_size()):
# 		if can_harvest():
# 			harvest()
# 			plant(Entities.Carrot)
# 		move(North)
# 	move(East)



# from config import *			# 导入配置文件（包含 L = 世界大小等定义）

# G1(0,0)
# while True:

# # 蛇形遍历整个农场：逐列耕作并种植南瓜

# 	for i in range(L):					# 遍历每一列（共 L 列）
# 		if get_pos_x() % 2 == 0:		# 偶数列：从下往上蛇形走

# 			for j in range(L):			# 遍历当前列中的每一行（共 L 行）
# 				if get_ground_type() == Grounds.Grassland:
# 					till()					# 耕地
# 				if can_harvest():
# 					harvest()	
# 				plant(Entities.Carrot)	# 种植胡萝卜

# 				if j < L - 1:			# 如果不是最后一行，则向北移动
# 					move(North)
# 				else:
# 					move(East)			# 如果是最后一行，则向东移动进入下一列


# 		else:							# 奇数列：从上往下蛇形走
# 			for j in range(L):			# 遍历当前列中的每一行（共 L 行）
# 				if get_ground_type() == Grounds.Grassland:
# 					till()					# 耕地
# 				if can_harvest():
# 					harvest()						
# 				plant(Entities.Carrot)	# 种植胡萝卜

# 				if j < L - 1:			# 如果不是最后一行，则向南移动
# 					move(South)
# 				else:
# 					move(East)			# 如果是最后一行，则向东移动进入下一列

