from sklearn.cluster import KMeans
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def rgb2hex(rgblist):
    hexlist = []
    for rgb in rgblist:
        strs = '#'
        for i in rgb:
            num = int(i)
            strs += str(hex(num))[-2:].replace('x', '0').upper()
        hexlist.append(strs)

    return hexlist


def color_cluster(pic):
    img = mpimg.imread(pic)
    if 'png' in pic:
        img *= 255
    re_img = img.reshape((img.shape[0] * img.shape[1], img.shape[2]))
    num_clus = 8
    clf = KMeans(n_clusters=num_clus)
    clf.fit(re_img)
    sub_color = clf.cluster_centers_
    sub_color = np.array(sub_color, dtype=np.int)
    labels = clf.labels_
    wgt = np.zeros(num_clus)
    for i in range(num_clus):
        tmp = np.where(labels == i)
        wgt[i] = len(tmp[0])
    wgt /= sum(wgt)
    caw = [[wgt[i], sub_color[i]] for i in range(len(wgt))]
    caw = sorted(caw, reverse=True, key=lambda x: (x[0]))
    cut_off = 0.05
    wgt = [c[0] for c in caw if c[0] > cut_off]
    wgt = [round(w, 3) for w in wgt]  # 主题色的权重
    sub_color = [c[1] for c in caw if c[0] > cut_off]  # 主题色的RGB值

    # 下面是作图
    row_num = 40
    col_num = 400
    res = []
    for c in sub_color:
        for i in range(row_num):
            res.append([c] * col_num)
    res = np.array(res, dtype=np.uint8)
    print(wgt)
    print(rgb2hex(sub_color))
    plt.figure(facecolor='#D3D3D3', figsize=(16, 5))  # 用浅灰色做背景来区分经常出现的黑白二色
    plt.subplot(1, 3, 1)
    # pie
    plt.title('Theme Color Top ' + str(num_clus))
    ax = plt.pie(wgt, colors=rgb2hex(sub_color), labels=wgt)
    plt.axis('equal')
    plt.legend()
    plt.subplot(1, 3, 2)
    plt.title('Product Image')
    plt.axis('off')  # 关闭坐标轴
    plt.imshow(img)
    plt.subplot(1, 3, 3)
    # gca
    # plt.yticks([row_num / 2 + row_num * i for i in range(len(wgt))], wgt)
    plt.title('Theme Color Top ' + str(num_clus))
    plt.yticks([row_num / 2 + row_num * i for i in range(len(wgt))], rgb2hex(sub_color))
    ax = plt.gca()
    ax.axes.get_xaxis().set_visible(False)  # x轴不可见
    ax.yaxis.set_ticks_position('right')  # y轴刻度在右侧显示
    plt.imshow(res)
    plt.savefig("test.png")
    plt.show()


color_cluster('C:/Users/renxi/Pictures/九色鹿 逐帧 jpg/1/九色鹿00000.jpg')
