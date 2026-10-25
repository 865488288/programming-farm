# clear()
# harvest()
# while True:
#     move(North)
# 	if can_harvest():
# 		harvest()




from config import *	
clear()		
while True:						# 无限循环，持续执行种植/收获

	# ---- 外层循环：按"列"遍历农场 ----
	for i in range(L):			# 遍历每一列（共 L 列）
		# ---- 内层循环：按"行"遍历一列 ----
		for j in range(L):		# 遍历当前列中的每一行（共 L 行）
			# 如果当前格子可以收获，则收获（作物成熟时会自动收获）
			if can_harvest():
				harvest()		
		move(North)			# 向北移动，进入当前列的下一个格子
	move(East)				# 一列扫完后，向东移动进入下一列