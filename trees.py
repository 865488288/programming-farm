from config import *			# 导入配置文件（包含 L = 世界大小等定义）
clear()							# 清空农场，重置状态

# 2026.08.16 12:16
def plant_tree():
	if can_harvest():		# 若可以收获则收获
		harvest()			
	if get_pos_x()% 2 == get_pos_y() % 2:	# 若当前位置xy都是偶数则种树
		plant(Entities.Tree)
	else:
		pass

while True:
	snake_traverse(plant_tree,8,6,4,5)







# while True:						# 无限循环，持续执行种植/收获

# 	# ---- 外层循环：按"列"遍历农场 ----
# 	for i in range(L):			# 遍历每一列（共 L 列）
# 		# ---- 内层循环：按"行"遍历一列 ----
# 		for j in range(L):		# 遍历当前列中的每一行（共 L 行）
# 			# 如果当前格子可以收获，则收获（作物成熟时会自动收获）
# 			if can_harvest():
# 				harvest()		

# 			# 根据格子的坐标奇偶性决定种植类型：
# 			# 若 (x + y) 为奇数 → 种树（Tree）
# 			if (get_pos_x() + get_pos_y()) % 2 == 1 :	
# 				plant(Entities.Tree)	
# 				#Watering(0.2)		# 若含水量小于等于 0.2，则浇水	

# 			# 若 (x + y) 为偶数 → 种灌木（Bush）	
# 			else:										
# 				plant(Entities.Bush)					

# 			move(North)			# 向北移动，进入当前列的下一个格子
# 		move(East)				# 一列扫完后，向东移动进入下一列


# #2026.08.13
# from config import *			# 导入配置文件（包含 L = 世界大小等定义）
# clear()							# 清空农场，重置状态

# def Bush_tree():		# 判断种植树木或跳过 2026.08.13
# 	if get_pos_x()% 2 == get_pos_y() % 2:	
# 		plant(Entities.Tree)
# 	else:
# 		# plant(Entities.Bush)
# 		pass	

# while True:
# # 蛇形遍历整个农场：逐列耕作并种植树木或灌木

# 	for i in range(L):					# 遍历每一列（共 L 列）
# 		if get_pos_x() % 2 == 0:		# 偶数列：从下往上蛇形走

# 			for j in range(L):			# 遍历当前列中的每一行（共 L 行）
# 				if can_harvest():		# 若可以收获则收获
# 					harvest()	
# 				Bush_tree()				# 种树或灌木

# 				if j < L - 1:			# 如果不是最后一行，则向北移动
# 					move(North)
# 				else:
# 					move(East)			# 如果是最后一行，则向东移动进入下一列


# 		else:							# 奇数列：从上往下蛇形走
# 			for j in range(L):			# 遍历当前列中的每一行（共 L 行）
# 				if can_harvest():		# 若可以收获则收获
# 					harvest()					
# 				Bush_tree()				# 种树或灌木

# 				if j < L - 1:			# 如果不是最后一行，则向南移动
# 					move(South)
# 				else:
# 					move(East)			# 如果是最后一行，则向东移动进入下一列		