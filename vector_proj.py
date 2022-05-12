import numpy as np

if __name__ == '__main__':
    # v = np.array([10, -5])
    # b1 = np.array([3, 4])
    # b2 = np.array([4, -3])

    # v = np.array([2, 2])
    # b1 = np.array([-3, 1])
    # b2 = np.array([1, 3])

    # v = np.array([1, 1, 1])
    # b1 = np.array([2, 1, 0])
    # b2 = np.array([1, -2, -1])
    # b3 = np.array([-1, 2, -5])

    v = np.array([1, 1, 2, 3])
    b1 = np.array([1, 0, 0, 0])
    b2 = np.array([0, 2, -1, 0])
    b3 = np.array([0, 1, 2, 0])
    b4 = np.array([0, 0, 0, 3])

    # vec_proj_v_onto_b1 = np.dot(v, b1) / np.linalg.norm(b1)
    # vec_proj_v_onto_b2 = np.dot(v, b2) / np.linalg.norm(b2)

    vec_proj_v_onto_b1 = np.dot(v, b1) / np.dot(b1, b1)
    vec_proj_v_onto_b2 = np.dot(v, b2) / np.dot(b2, b2)
    vec_proj_v_onto_b3 = np.dot(v, b3) / np.dot(b3, b3)
    vec_proj_v_onto_b4 = np.dot(v, b4) / np.dot(b4, b4)

    print(f'vec_proj_v_onto_b1 = {vec_proj_v_onto_b1}')
    print(f'vec_proj_v_onto_b2 = {vec_proj_v_onto_b2}')
    print(f'vec_proj_v_onto_b3 = {vec_proj_v_onto_b3}')
    print(f'vec_proj_v_onto_b4 = {vec_proj_v_onto_b4}')
