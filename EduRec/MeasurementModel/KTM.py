# coding: utf-8
# 2021/2/13 @ tongshiwei

from EduRec.meta.MeasurementModel import MeasurementModel


class KTM(MeasurementModel):
    def __init__(self):
        self.m = None
        self._state = None

    def __call__(self, *args, **kwargs):
        pass

    def step(self, response):
        pass

    def begin_episode(self, response_logs):
        pass

    def end_episode(self):
        self._state = None
