from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 11
z = 12

gift = mc.getBlock(x, y, z)
if gift != 0:
    print("Here is the secret passage")
else:
    mc.postToChat("Place an offering on the pedestal.")
    
