
""" 画像ファイルの読み込み、BGR 各チャンネルの保存 """
import numpy as np
import cv2 as cv

# 適当なカラー画像をこのコードと同じフォルダーに用意して読み込む
image = cv.imread('space-cat.jpg')
print('width', image.shape[1])
print('height', image.shape[0])
print('channel', image.shape[2])

# B チャンネルをグレースケール画像として保存
cv.imwrite('space-cat_B.png', image[:, :, 0])

# G チャンネルをグレースケール画像として保存
cv.imwrite('space-cat_G.png', image[:, :, 1])

# R チャンネルをグレースケール画像として保存
cv.imwrite('space-cat_R.png', image[:, :, 2])

"""
Note:
    var[:, :, k]の代わりに var[..., k]と書くこともできる。
    この記法に慣れていない場合は、 Numpyのndarrayの基本を要確認。

    カラー画像はビット深度が 24（8bit x 3channels）だが、
    グレースケール画像は 8 である。
    Windows ではファイルのプロパティの詳細タブで確認できる。
"""