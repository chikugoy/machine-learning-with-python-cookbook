# -*- coding: utf-8 -*-

# ライブラリをロード
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# 特徴量行列を作成
features = np.array([[2, 3],
                     [2, 3],
                     [2, 3]])

# PolynomialFeatures オブジェクトを作成
# degree=2 で2乗
# interaction_only=True とする事で交互作用特微量を省く事ができる
polynomial_interaction = PolynomialFeatures(degree=2, include_bias=False)

# 多項式特徴量を作成
polynomial_interaction.fit_transform(features)

##########

# 交互作用特微量
interaction = PolynomialFeatures(degree=2,
              interaction_only=True, include_bias=False)
interaction.fit_transform(features)


