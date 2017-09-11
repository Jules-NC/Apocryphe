# -*- coding: utf-8 -*-
import numpy as np

def levenshtein(source, tg):    # UTSUKUSHI DESU DESU MOTTO MOTTO NOTICE ME SEMPAI
    if len(source) < len(tg):
        return levenshtein(tg, source)
    if len(tg) == 0:
        return len(source)
    source = np.array(tuple(source))
    tg = np.array(tuple(tg))
    p_r = np.arange(tg.size + 1)
    for s in source:
        c_r = p_r + 1
        c_r[1:] = np.minimum(c_r[1:], np.add(p_r[:-1], tg != s))
        c_r[1:] = np.minimum(c_r[1:], c_r[0:-1] + 1)
        p_r = c_r
    return p_r[-1]


def levenshtein_list(l, tg):
    try:
        return min([levenshtein(e, tg) for e in l])
    except ValueError:
        return 100