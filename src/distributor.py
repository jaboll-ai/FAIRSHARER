def fair_sharer(values: list, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """
    values_new = values.copy()
    for i in range(num_iterations):
        max_idx = values_new.index(max(values_new))
        values_new[max_idx-1] += values_new[max_idx] * share
        values_new[max_idx+1] += values_new[max_idx] * share
        values_new[max_idx] -= 2 * values_new[max_idx] * share
    return values_new