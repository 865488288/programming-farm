# import                从另一个文件导入函数和全局变量。
# quick_print()         快速打印到输出页面


### 命令 ###
# clear()  #清除 重置
# harvest()     收获
# do_a_flip()   翻转
# pet_the_piggy()   摸摸猪头

# move(North)   行走
#   North   北
#   South   南
#   West    西
#   East    东


### 函数 ###
# 使用 def 关键字来自定义一个新的函数：
# def f(arg1, arg2 = False):
# 	#函数代码

# 使用 () 来调用某个函数：
# f(42)

# 你已经见过像 harvest() 这样的内置函数。
# 你也可以自定义函数，从而以模块化的方式组织你的代码。
# 简单来说，你可以给一个代码块命名，之后可以从任何地方调用该代码块。


# 如果想写入一个全局变量，则必须使用 global 关键字来明确表示。

# x = 0

# def f():
#     global x
#     x = 1
# f()
# print(x)

# 添加global x      #将 x 绑定到上面定义的全局变量 x。现在打印的会是 1
# 不加global x      #打印的会是 0



###   游戏定义的函数   ###
# get_world_size()          获取田地长度
# get_pos_x()               返回无人机当前的 x 坐标

# can_harvest()             判断是否可以收获
# get_entity_type()         判断无人机下方实体的类型。
# get_ground_type()         判断无人机下方地块的类型。
# get_water()               获取含水量
# num_items(item)           获取物品栏中当前 item 的数量

# plant(Entities.Bush)      种植：灌木
# use_item(Items.Water)     给地块浇水
# use_item(Items.Fertilizer) 施肥 将下方植物的剩余生长时间缩短 2 秒。

# measure(direction = None) 可以测量某些实体的一些值。效果取决于实体。




### 物品 ###
# Grass     草
# Bush      灌木
# Tree      树
# Carrot    胡萝卜
# Pumpkin   南瓜
# Sunflower 向日葵

# Hay       干草
# Wood      木材

# Items.Weird_Substance   奇异物质

# Grassland 草原
# Soil      土地


#############    If 语句  ##################
# 使用 if、elif 和 else 来选择性地运行代码

# if condition1:    判断
# 	do_a_flip()
# elif condition2:  上面判断不过则执行此判断(可以多个)
# 	harvest() 
# else:             所有判断都不通过则执行此代码
# 	do_a_flip()
# 	harvest()



#############    while循环  ##################
# while 条件:
# 	#循环体
# 	#循环体
# 	#...
#     条件 是 1 个布尔值，#循环体 则是你想要在满足 True 条件的情况下



#############    for循环  ##################
# for variable_name in sequence:
# 	#代码块

# variable_name 是你自定义变量的名称，它是存储序列中的某个元素。
# sequence 是存储序列，存放多个元素，比如一个数字范围。
# 每当 1 个元素被存储序列遍历 1 次，循环体就会运行 1 次。


# 示列：
# for i in range(5):
#     harvest()

# 这个循环会固定次数地执行循环体，基本上等同于如下代码：

# i = 0
# harvest()
# i = 1
# harvest()
# i = 2
# harvest()
# i = 3
# harvest()
# i = 4
# harvest()


# 			列表 list		字典 dict		集合 set
# 符号		[]				{k:v}			{元素1,元素2}
# 空对象	[]	{}	set()
# 内容		有序，允许重复	key 唯一，key:value     键值对	无序，元素不重复
# 查找in	慢	快（查 key）	快
# 添加	append()	dict[key]=value	.add()
# 删除	remove()	.pop(key)	.remove()




# 更换帽子的代码如下：
# change_hat(hat)
# change_hat(Hats.Gray_Hat)
# change_hat(Hats.Purple_Hat)
# change_hat(Hats.Green_Hat)
# change_hat(Hats.Brown_Hat)
# change_hat(Hats.Wizard_Hat)
# change_hat(Hats.Dinosaur_Hat)
