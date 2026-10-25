
for i in range(get_world_size()):
	for i in range(get_world_size()):
		plant(Entities.Bush)	# 首次种植
		move(North)
	move(East)

# 种植
while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(Entities.Bush)
		move(North)
	move(East)