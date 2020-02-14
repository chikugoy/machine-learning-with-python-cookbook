# -*- coding: utf-8 -*-

# ライブラリをロード
import numpy as np

# 行列を作成
matrix = np.array([[1, 1, 1],
                   [1, 1, 10],
                   [1, 1, 15]])

# 行列のランクを返す
# ランクとはベクトル空間の次元数
np.linalg.matrix_rank(matrix)
