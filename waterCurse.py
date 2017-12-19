from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
count = 30
while count > 0:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 8)
    time.sleep(1)
