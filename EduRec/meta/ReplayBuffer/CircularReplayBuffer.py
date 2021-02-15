# coding:utf-8
# created by tongshiwei on 2018/11/8
from __future__ import absolute_import
import random

from .ReplayBuffer import FiniteReplayBuffer


class CircularReplayBuffer(FiniteReplayBuffer):
    def add(self, new_memory):
        if len(self._buffer) == self.max_size:
            self._buffer[self.top] = new_memory
            self.top = (self.top + 1) % self.max_size
        elif len(self._buffer) < self.max_size:
            self._buffer.append(new_memory)
        else:
            self.logger.warning(
                "detect the size of current size bigger than max_size, maybe existing error somewhere"
            )
            self._buffer = random.sample(self._buffer, self.max_size)
