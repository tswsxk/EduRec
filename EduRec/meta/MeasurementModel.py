# coding: utf-8
# 2021/2/13 @ tongshiwei


class MeasurementModel(object):
    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def step(self, *args, **kwargs):
        raise NotImplementedError

    def begin_episode(self, *args, **kwargs):
        raise NotImplementedError

    def end_episode(self, *args, **kwargs):
        raise NotImplementedError

    def tune(self):
        pass
