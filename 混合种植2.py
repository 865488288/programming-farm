from config import *

clear()	

def tree_grass():	# 定义草树混种树函数：棋盘种植
	if get_pos_x()% 2 == get_pos_y() % 2:	# 若x和y同属奇数或偶数
		harvest()				# 收获
		plant(Entities.Tree)	# 种树
	else :			
		harvest()	# 收获

def carrot():	# 定义胡萝卜种植函数
	if get_ground_type() == Grounds.Grassland :	# 若地块为草地
		till()					# 耕地
		plant(Entities.Carrot)	# 种植胡萝卜
	else:	# 否则(不为草地就)
		harvest()		# 收获
		plant(Entities.Carrot)	# 种植胡萝卜


# 种植南瓜
entity_dict = set()	# 创建空集合储存坏南瓜位置
def plant_pumpkin():			# 定义操作：南瓜
	# 若有 x范围 * y范围 个南瓜的坐标点 就收获
	if len(entity_dict) == (i[1][0] - i[0][0] + 1) *(i[1][1] - i[0][1] + 1) :
		while entity_dict:	# 如果集合不为空，则说明有南瓜需要收获 循环执行到最后一个不确定南瓜
			for pos in list(entity_dict):	# 遍历集合中的每个坐标
				G1(pos[0], pos[1])	# 移动到当前坐标

				# 如果  当前位置有南瓜可以收获（成熟南瓜）、还有别的坏南瓜	从集合中移除该坐标
				if get_entity_type() == Entities.Pumpkin  and  can_harvest()  and  len(entity_dict) > 1:
					entity_dict.remove(pos)	# 删除当前坐标	

				# 如果  当前位置有南瓜不可以收获（未成熟南瓜）、还有别的坏南瓜  退出当前for循环	
				elif get_entity_type() == Entities.Pumpkin  and  not can_harvest()  and  len(entity_dict) > 1:
					pass	# 跳过

				# 如果当前位置是死南瓜	# 种植南瓜
				elif get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)	
					Watering(0.5)				# 浇水
					use_item(Items.Fertilizer) 	# 施肥	


				# 否则	执行循环判断收获
				else:	
					if can_harvest() and entity_dict :	# 如果可以收获
						harvest()	# 收获南瓜
						entity_dict.remove(pos)	# 删除当前坐标	
					else:	
						while not can_harvest():	# 若不可以收获 则循环
							Watering(0.5)				# 浇水
							use_item(Items.Fertilizer) 	# 施肥
							if can_harvest() and not entity_dict :	# 如果可以收获
								harvest()	# 收获南瓜
								entity_dict.remove(pos)	# 删除当前坐标
							elif get_entity_type() == Entities.Dead_Pumpkin:	# 否则如果是死南瓜则
								plant(Entities.Pumpkin)	# 种植南瓜
		G0(i[0][0],i[0][1]) # 回到起始位置
	# 种植南瓜	
	x,y = get_pos_x(),get_pos_y()	# 获取当前位置坐标
	if get_ground_type() == Grounds.Grassland:	# 若地块为草地
		harvest()	# 收获
		till()		# 耕地
		plant(Entities.Pumpkin)		# 种植南瓜
		entity_dict.add((x,y))		# 将当前位置坐标添加到集合中
	else:
		harvest()
		plant(Entities.Pumpkin)		# 种植南瓜
		entity_dict.add((x,y))	# 将当前位置坐标添加到集合中




# 定义绕圈种植函数：起始点 + 终止点 + 当前路径执行的种植函数
circles = [
		((0,0),(5,5),tree_grass),((6,0),(11,5),carrot),((12,0),(17,5),plant_pumpkin)
		]						

while True :	
	for i in circles:
		snake_traverse_scope(i[0],i[1],i[2])  # 把带入的参数传递给 蛇形范围 执行			