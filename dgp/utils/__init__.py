# Copyright 2021 Toyota Research Institute.  All rights reserved.
import os

from tqdm import tqdm as _tqdm
from .cpu_count import get_cpu_count

DGP_DISABLE_TQDM = bool(int(os.getenv('DGP_DISABLE_TQDM', default='0')))


def tqdm(*args, **kwargs):
    kwargs['disable'] = DGP_DISABLE_TQDM
    return _tqdm(*args, **kwargs)
