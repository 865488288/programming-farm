# 常用函数和设定
# 在其他程序中用  from config import *	命令 来使用


L = get_world_size()		# 定义 L = 世界长度


# 2026.08.17 13:50
# 移动到目标位置 并执行传递的函数
def G1(x , y , execute = None):	
	# 若未传递执行函数，则定义一个空函数（什么都不做）
	if execute == None:
		def execute():
			pass

	# X 方向移动（先调整水平方向）
	while get_pos_x() > x:		# 若当前位置x > 目标x，向西移动
		execute()				# 每走一步前，先执行一次传递的函数（如：浇水、种植等）
		move(West)
	while get_pos_x() < x:		# 若当前位置x < 目标x，向东移动
		execute()				# 每走一步前，先执行一次传递的函数
		move(East)
	# Y 方向移动（再调整垂直方向）
	while get_pos_y() > y:		# 若当前位置y > 目标y，向南移动
		execute()				# 每走一步前，先执行一次传递的函数
		move(South)
	while get_pos_y() < y:		# 若当前位置y < 目标y，向北移动
		execute()				# 每走一步前，先执行一次传递的函数
		move(North)	
	if get_pos_x() == x and get_pos_y() == y:	# 到达目标位置后，再执行一次传递的函数
		execute()	

			
# 2026.08.18 14:53
# 快速移动到目标位置(可穿越地图边界)
def G0(x , y):
 # x方向判断并移动
	if abs(get_pos_x() - x) > (L/2) :
	# 若移动距离>1/2世界尺寸'L'(穿越边界更近)
		if get_pos_x() < x :	# 若当前位置<目标位置 ,设定x前进方向为西
			x_direction = West
		else:					# 否则(若当前位置>=目标位置),设定x前进方向为东
			x_direction = East
	else:
	# 否则(移动距离<=1/2世界尺寸'L')(正常移动近)
		if get_pos_x()  <  x :	# 若当前位置<目标位置 ,设定x前进方向为东
			x_direction = East	
		else:					# 否则(若当前位置>=目标位置),设定x前进方向为西
			x_direction = West

	while get_pos_x() != x :	# 若当前位置 != 目标位置则循环
		move(x_direction)		# 朝设定方向移动
 # y方向判断并移动  同上
	if abs(get_pos_y() - y) > (L/2) :
		if get_pos_y() < y :
			y_direction = South
		else:
			y_direction = North
	else:
		if get_pos_y() < y :
			y_direction = North
		else:
			y_direction = South	
	while get_pos_y() != y :
		move(y_direction)	


# 2026.08.16 12:18
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

# 2026.08.20 14:14
# 蛇形遍历 范围模式：每格执行函数	起始坐标	结束坐标
def snake_traverse_scope(start = None , end = None , action = None):
	start = start or (0,0)	# 若未传递起始点位置 设定为起始点位(0,0)
	end = end or (L,L)		# 若未传递终止点位置 设定未最大地图点位(L,L)
	if action == None:		# 若未传递执行函数 设定为跳过 (pass)
		def action():
			pass

	G0(start[0],start[1])				# 去开始点，确保从起始点开始

	for col in range(end[0] - start[0] + 1):		# 遍历列(终止x - 起始x + 1 )

		if col % 2 == 0:			# 设定方向：偶数列 从下往上（从南到北）
			direction = North
		else:						# 设定方向：奇数列 从上往下（从北到南）
			direction = South

		for row in range(end[1] - start[1] + 1):	# 遍历当前列的每一行(终止y - 起始y + 1 )
			action()				# 执行传递的函数
			if row < (end[1] - start[1]) :	# 不是最后一行，继续当前方向
				move(direction)
			elif col < (end[0] - start[0]) :	# 是最后一行但不是最后一列，向东移动
				move(East)


# 浇水 2026.08.13
def Watering(content = 0.5):		
	if get_water() <= content :
		use_item(Items.Water)		














############### 弃用的老版本函数 ################



# def G1(X,Y):	# 移动到目标位置 2026.08.14
# 	x,y = get_pos_x(),get_pos_y()

# 	#  X 方向移动：
# 	if  x > X :
# 		for i in range(x-X):
# 			move(West)
# 	elif x < X :
# 		for j in range(X-x):
# 			move(East)

# 	#  Y 方向移动：
# 	if  y > Y :
# 		for i in range(y-Y):
# 			move(South)
# 	elif y < Y :	
# 		for j in range(Y-y):
# 			move(North)	


# def G1(x , y):	# 移动到目标位置 2026.08.16 11:40
# 	if x == None:
# 		x = get_pos_x() 
# 	if y == None:
# 		y = get_pos_y() 
		
# 	# X 方向移动
# 	while get_pos_x() > x:
# 		move(West)
# 	while get_pos_x() < x:
# 		move(East)    
# 	# Y 方向移动
# 	while get_pos_y() > y:
# 		move(South)
# 	while get_pos_y() < y:
# 		move(North)			

# def G2(x , y , execute):	# 移动到目标位置 并执行传递函数 2026.08.16 15:30
# 	# X 方向移动
# 	while get_pos_x() > x:
# 		execute()
# 		move(West)
# 	while get_pos_x() < x:
# 		execute()
# 		move(East)
# 	# Y 方向移动
# 	while get_pos_y() > y:
# 		execute()
# 		move(South)
# 	while get_pos_y() < y:
# 		execute()
# 		move(North)	

# def G1(x , y , execute = []):	# 移动到目标位置 并执行传递函数 2026.08.17 12:25
# 	# X 方向移动

# 	if len(execute) == 0 :
# 		def execute():
# 			pass
# 	else :
# 		execute_1 = execute[0]
# 		def execute():
# 			execute_1()
# 	while get_pos_x() > x:
# 		execute()
# 		move(West)
# 	while get_pos_x() < x:
# 		execute()
# 		move(East)
	
# 	# Y 方向移动
# 	while get_pos_y() > y:
# 		execute()
# 		move(South)
# 	while get_pos_y() < y:
# 		execute()
# 		move(North)	

# 	if get_pos_x() == x and get_pos_y() == y:
# 		execute()		

# def snake_traverse(action, L = None):	
# 蛇形遍历农场，每格执行 action() 2026.08.14
# 	if L == None:
# 		L = get_world_size()				# 默认遍历整个世界
# 	for i in range(L):					# 遍历每一列
# 		if get_pos_x() % 2 == 0:		# 偶数列：从下往上蛇形走
# 			for j in range(L):			# 遍历当前列中的每一行
# 				action()					# 执行自定义操作
# 				if j < L - 1:			# 如果不是最后一行，则向北移动
# 					move(North)
# 				elif get_pos_y() == j and get_pos_x() == L - 1:	# 如果到达右上角的终点，则退出循环
# 					break		
# 				else:
# 					move(East)			# 如果是最后一行，则向东移动进入下一列			
# 		else:							# 奇数列：从上往下蛇形走
# 			for j in range(L):			# 遍历当前列中的每一行
# 				action()					# 执行自定义操作
# 				if j < L - 1:			# 如果不是最后一行，则向南移动
# 					move(South)
# 				elif get_pos_y() == 0 and get_pos_x() == L - 1:	# 如果到达右下角的终点，则退出循环
# 					break	
# 				else:
# 					move(East)			# 如果是最后一行，则向东移动进入下一列


# def storage():		# 创建字典存储当前位置作物 2026.08.14
# 	x, y = get_pos_x(), get_pos_y()
# 	entity_dict += {(x, y): get_entity_type()}	
	  


