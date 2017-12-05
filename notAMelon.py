from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 36
y = 0
z = 103
melon= 103
block = mc.getBlock(x, y, z)

noMelon = block ==0

    

mc.postToChat("You need to get some food: " + str(noMelon))
