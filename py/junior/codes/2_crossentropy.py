import numpy as np


N_cls = input('')
N_cls = int(N_cls)

a = input('')
pred_l = a.split(' ')

b = input('')
real_l = b.split(' ')


def softmax(X):
    # exps = np.exp(X - np.max(X))
    exps = np.exp(X)
    return exps / np.expand_dims(np.sum(exps, axis=1), axis=1)


def onehot(a, C):
    e = np.zeros([len(a), C])
    e[range(len(a)), a] = 1
    return e


def crossentropy(X, y):
    """
    X: [[0, 0, 0, 1], [1, 0, 0, 0]], y: [3, 0]
    """
    b = len(y)
    C = X.shape[1]
    p_pred = softmax(X)
    log_p_pred = -np.log(p_pred)

    # log_ll = -(np.log(p_pred)*p_real)
    # return np.sum(log_ll)
    y_onehot = onehot(y, C)
    # 点乘
    s = log_p_pred * y_onehot
    return np.sum(s)/b



pred_l = [int(m) for m in pred_l]
real_l = [int(m) for m in real_l]

pred_l_onehot = onehot(pred_l, N_cls)
print(crossentropy(pred_l_onehot, real_l))


# import torch
# import torch.nn as nn


# criterion = nn.CrossEntropyLoss()
# t_pred = torch.Tensor([
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1]
# ])
# t_real = torch.LongTensor([3, 2])
# loss = criterion(t_pred, t_real)
# print(loss)

# 3,0 3,0 0.7437 1,2 3,0 1.74