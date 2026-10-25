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
						do_a_flip() 	# 让无人机做一次翻转！
						do_a_flip() 	# 让无人机做一次翻转！
						do_a_flip() 	# 让无人机做一次翻转！
						harvest()
						entity_dict.remove(pos)
						break

	if can_harvest() and not entity_dict :	# 如果可以收获
		do_a_flip() 	# 让无人机做一次翻转！
		do_a_flip() 	# 让无人机做一次翻转！
		do_a_flip() 	# 让无人机做一次翻转！
		harvest()	# 收获南瓜		

	snake_traverse(plant_pumpkin)	# 蛇形遍历整个农场，逐格耕作并种植南瓜