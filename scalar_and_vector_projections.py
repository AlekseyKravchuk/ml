import numpy as np
import itertools
from typing import List
from typing import Iterable
from typing import Any


def check_if_pairwise_orthogonal(vectors_lst):
    for tpl in itertools.combinations(vectors_lst, 2):
        if np.dot(tpl[0], tpl[1]) != 0:
            return False
    return True


def get_vec_projections_3D(v: Iterable[Any], new_basis: List[Iterable]):
    b1, b2, b3 = new_basis
    # get vector projection of vector 'v' onto b1
    v1 = b1 * np.dot(v, b1) / np.dot(b1, b1)

    # get vector projection of vector 'v' onto b2
    v2 = b2 * np.dot(v, b2) / np.dot(b2, b2)

    # get vector projection of vector 'v' onto b3
    v3 = b3 * np.dot(v, b3) / np.dot(b3, b3)
    return v1, v2, v3


def get_scalar_projections_3D(v, new_basis):
    b1, b2, b3 = new_basis
    # get scalar projection of vector 'v' onto b1
    v1_scalar = np.dot(v, b1) / np.linalg.norm(b1)

    # get vector projection of vector 'v' onto b2
    v2_scalar = np.dot(v, b2) / np.linalg.norm(b2)

    # get vector projection of vector 'v' onto b3
    v3_scalar = np.dot(v, b3) / np.linalg.norm(b3)
    return v1_scalar, v2_scalar, v3_scalar


if __name__ == '__main__':
    v = np.array([-4, -3, 8])
    b1 = np.array([1, 2, 3])
    b2 = np.array([-2, 1, 0])
    b3 = np.array([-3, -6, 5])

    vectors_lst = [b1, b2, b3]

    if check_if_pairwise_orthogonal(vectors_lst):
        for idx, vec_proj in enumerate(get_vec_projections_3D(v, vectors_lst), start=1):
            print(f'vec_proj[{idx}] = {vec_proj}')
