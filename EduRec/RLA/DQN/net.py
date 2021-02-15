# coding: utf-8
# 2021/2/10 @ tongshiwei

from mxnet import gluon
from longling.ML.MxnetHelper.toolkit import loss_dict2tmt_mx_loss


def get_loss(*args, **kwargs):
    return loss_dict2tmt_mx_loss({"L2Loss": gluon.loss.L2Loss(*args, **kwargs)})


class DQNet(gluon.HybridBlock):
    def __init__(self, out, hidden_layers=None, dropout=0.0, activation="relu", prefix=None, params=None):
        super(DQNet, self).__init__(prefix=prefix, params=params)
        with self.name_scope():
            self.q_net = gluon.nn.HybridSequential()
            if hidden_layers is not None:
                for hidden_feature in hidden_layers:
                    self.q_net.add(
                        gluon.nn.Dense(hidden_feature, activation=activation),
                        gluon.nn.Dropout(dropout)
                    )
            self.q_net.add(gluon.nn.Dense(out))

    def hybrid_forward(self, F, x, *args, **kwargs):
        return self.q_net(x)
