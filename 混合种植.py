L = get_world_size()		# 定义 L = 世界长度

def G1(x , y , execute = None):	# 移动到目标位置 并执行传递函数
	if execute == None:
		def execute():
			pass

	# X 方向移动
	while get_pos_x() > x:
		execute()
		move(West)
	while get_pos_x() < x:
		execute()
		move(East)
	# Y 方向移动
	while get_pos_y() > y:
		execute()
		move(South)
	while get_pos_y() < y:
		execute()
		move(North)	
	if get_pos_x() == x and get_pos_y() == y:
		execute()		

# 蛇形遍历：每格执行函数   运行范围   起始坐标
def snake_traverse(action, width=None , height=None , start_x=None , start_y=None):
	width = width or L
	height = height or L
	start_x = start_x or 0
	start_y = start_y or 0

	G1(start_x,start_y)				# 去开始点，确保从起始点开始

	for col in range(width):		# 遍历每一列
		if col % 2 == 0:			# 设定方向：偶数列 从下往上（从南到北）
			direction = North
		else:						# 设定方向：奇数列 从上往下（从北到南）
			direction = South

		for row in range(height):	# 遍历当前列的每一行
			action()				# 执行传递的函数
			if row < height - 1:	# 不是最后一格，继续当前方向
				move(direction)
			elif col < width - 1:	# 是最后一格但不是最后一列，向东移动
				move(East)


def carrot():	# 定义胡萝卜种植函数
	if get_ground_type() == Grounds.Grassland :	# 若地块为草地
		till()					# 耕地
		plant(Entities.Carrot)	# 种植胡萝卜
	else:	# 否则(不为草地就)
		harvest()		# 收获
		plant(Entities.Carrot)	# 种植胡萝卜
			
def tree_grass():	# 定义草树混种树函数：棋盘种植
	if get_pos_x()% 2 == get_pos_y() % 2:	# 若x和y同属奇数或偶数
		harvest()				# 收获
		plant(Entities.Tree)	# 种树
	else :			
		harvest()	# 收获

def plant_pumpkin():	# 定义种植南瓜函数：耕地、种南瓜、储存南瓜坐标
	x,y = get_pos_x(),get_pos_y()	# 获取当前位置坐标
	if get_ground_type() == Grounds.Grassland:	# 若地块为草地
		harvest()	# 收获
		till()		# 耕地
		plant(Entities.Pumpkin)		# 种植南瓜
		entity_dict.add((x,y))		# 将当前位置坐标添加到集合中
	else:	# 否则(不为草地)
		plant(Entities.Pumpkin)		# 种植南瓜			
		entity_dict.add((x,y))		# 将当前位置坐标添加到集合中

def spiral_planting():	# 定义绕圈种植函数：圈起始点 + 四个坐标点 + 当前路径执行的种植函数
	# 位置参数列表
	circles = [
			(0,0,None),	(15,0,tree_grass),	(15,15,tree_grass),	(0,15,tree_grass),	(0,1,tree_grass),
			(1,1,None),	(14,1,carrot),		(14,14,carrot),		(1,14,carrot),		(1,2,carrot),
			(2,2,None),	(13,2,tree_grass),	(13,13,tree_grass),	(2,13,tree_grass),	(2,3,tree_grass),
			(3,3,None),	(12,3,carrot),		(12,12,carrot),		(3,12,carrot),		(3,4,carrot),
			(4,4,None),	(11,4,tree_grass),	(11,11,tree_grass),	(4,11,tree_grass),	(4,5,tree_grass)
			]
	for x,y,exe in circles :	# 把绕圈位置参数带入x,y,exe
		G1(x,y,exe)				# 把带入的参数传递给G1执行


entity_dict = set()	# 创建空集合储存坏南瓜位置

while True: # 循环 绕圈种植 树、草、胡萝卜、南瓜

	spiral_planting()	# 绕圈种植函数

	# 坏南瓜排查、补种并收获
	while entity_dict:	# 如果集合不为空，则说明有南瓜需要收获
		for pos in list(entity_dict):	# 遍历集合中的每个坐标
			G1(pos[0], pos[1])	# 移动到集合坐标
			# 若当前位置是活南瓜、可以收获、还有别的可疑南瓜
			if get_entity_type() == Entities.Pumpkin  and  can_harvest()  and  len(entity_dict) > 1:
				entity_dict.remove(pos)		# 从集合中移除该坐标
			# 若当前位置是活南瓜、不可以收获、还有别的可疑南瓜	
			elif get_entity_type() == Entities.Pumpkin  and  not can_harvest()  and  len(entity_dict) > 1:
				pass	# 退出当前循环
			# 若当前位置是活南瓜、可以收获、且没有别的可疑南瓜
			elif get_entity_type() == Entities.Pumpkin  and  can_harvest()  and  len(entity_dict) == 1 :
				harvest()		# 收获
				entity_dict.remove(pos)		# 从集合中移除该坐标
			# 若当前位置是死南瓜	
			elif get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)		# 种植南瓜				
			else:	# 否则	执行循环判断收获(最后一颗南瓜收获)
				while True:
					if can_harvest():	# 若可以收获
						harvest()		# 收获
						entity_dict.remove(pos)	# 从集合中移除当前坐标
						break			# 打破当前循环
					elif get_entity_type() == Entities.Dead_Pumpkin:	# 若当前位置是死南瓜
						plant(Entities.Pumpkin)		# 种植南瓜
						use_item(Items.Fertilizer) 	# 施肥
						do_a_flip() 				# 让无人机做一次翻转！
					else:		# 否则 (未成熟南瓜)
						use_item(Items.Fertilizer) 	# 施肥
						do_a_flip() 				# 让无人机做一次翻转！	

	snake_traverse(plant_pumpkin,6,6,5,5)	# 蛇形遍历逐格调用种植南瓜函数											