import sys, csv, math
import numpy as np
import matplotlib.pyplot as plt

#a(v) = g - (-1.34775015)v - (1.32303275)v^2

#constants
g = 9.8
#c1 = -1.34775015
#c2 = 1.32303275
c1 = 1.90637392
c2 = 0.12870873
delta_t = 0.000001


#input initial launch conditions
height = float(sys.argv[1])
speed = float(sys.argv[2])
angle = float(sys.argv[3]) * math.pi / 180

vx, vy = speed * math.cos(angle), speed * math.sin(angle)
ypos = height
positions = [[0, ypos]]

while ypos >= 0:
    angle  = math.atan(vy/vx)
    ad = c1 * abs(speed) + c2 * abs(speed) ** 2

    ax = -1 * ad * math.cos(angle)
    ay = -1 * ad * math.sin(angle) - g

    vx = vx + ax * delta_t
    vy = vy + ay * delta_t
    speed = math.sqrt(vx**2 + vy**2)

    delta_rx = vx  * delta_t + 0.5 * ax * delta_t ** 2
    delta_ry = vy  * delta_t + 0.5 * ay * delta_t ** 2

    xpos = positions[-1][0] + delta_rx
    ypos = positions[-1][1] + delta_ry
    positions.append([xpos, ypos])

print('Final X Position:', xpos, '| Final Y Position:', ypos)
plt.plot(list(i[0] for i in positions), list(i[1] for i in positions))
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.show()
