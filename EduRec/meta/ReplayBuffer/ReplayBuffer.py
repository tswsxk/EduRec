# coding: utf-8
# 2021/2/13 @ tongshiwei

import logging
import numpy as np


class ReplayBuffer(object):
    def __init__(self, logger=logging, seed=None):
        self._buffer = []
        self.logger = logger
        self._random_state = np.random.RandomState(seed)

    def add(self, *args, **kwargs):
        raise NotImplementedError

    def __len__(self):
        return len(self._buffer)

    def __getitem__(self, item):
        return self._buffer[item]

    def reset(self):
        self._buffer = []

    @property
    def size(self):
        return len(self._buffer)

    def sample(self, size):
        if size > len(self._buffer):
            self.logger.warning("requiring size bigger than the buffered, only return %s" % len(self._buffer))
            return self._buffer
        else:
            idx = self._random_state.randint(0, len(self) - 1, size)
            return [self._buffer[i] for i in idx]


class InfinityReplayBuffer(ReplayBuffer):
    def __init__(self, logger=logging, seed=None, *args, **kwargs):
        super(InfinityReplayBuffer, self).__init__(logger, seed)

    def add(self, item):
        self._buffer.append(item)


class FiniteReplayBuffer(ReplayBuffer):
    def __init__(self, max_size=1000000, logger=logging, seed=None, *args, **kwargs):
        super(FiniteReplayBuffer, self).__init__(logger, seed)
        self.max_size = max_size
        self.top = 0

    def add(self, *args, **kwargs):
        raise NotImplementedError
