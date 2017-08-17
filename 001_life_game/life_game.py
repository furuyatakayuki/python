# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

def img_show(img : np.ndarray, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none') -> None:
    # np.arrayを引き数とし、画像を表示する。
    # dtypeをuint8にする
    img = np.clip(img, vmin, vmax).astype(np.uint8)
    # 画像を表示
    plt.imshow(img, cmap = cmap, vmin = vmin, vmax = vmax, interpolation = interpolation)

def update(i, str_1, str_2):
    global world
    global area
    next_gen()

    plt.cla()
    x, y = np.mgrid[:area, :area]

    plt.title(str_1 + str_2 + str('%04d' % i))
    img_show(world*255)

def next_gen():
    global world
    global area
    dead_or_alive = np.zeros((area, area))

    for i in range(area):
        for j in range(area):
            count = 0
            if (i-1 >= 0 and j-1 >= 0 and i+1 < area and j+1 < area):
                # i-1から3要素、j-1から3要素の3×3の行列を抜き出して0以外の数を数える
                count = np.count_nonzero(world[i-1:i+2, j-1:j+2])

            if world[i][j] == 1:
                # この状態のcountは自身のセルも含まれているため-1する
                if 2 <= count-1 and count-1 <= 3:
                    dead_or_alive[i][j] = 1
                else:
                    dead_or_alive[i][j] = 0
            elif count == 3:
                dead_or_alive[i][j] = 1

    world = dead_or_alive

if __name__ == '__main__':
    global world
    global area
    area = 200
    n = 4000
    world = np.zeros((area, area))

    # 初期値
    for i in range(n):
        world[np.random.randint(area), np.random.randint(area)] = 1

    fig = plt.figure()
    ani = ani.FuncAnimation(fig, update, fargs=('gen', ':'), interval=50)
    plt.show()
