# coding: utf-8
# 2021/2/15 @ tongshiwei
import mxnet.ndarray as nd
from longling.ML.MxnetHelper import fit_wrapper


@fit_wrapper
def fit_f(net, batch_data, loss_function, *args, **kwargs):
    state, action, reward = batch_data
    loss = []
    pred = nd.pick(net(state), action)
    for _, loss_f in loss_function.items():
        loss.append(loss_f(pred, reward))
    return sum(loss)
