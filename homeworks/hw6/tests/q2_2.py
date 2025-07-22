test = {   'name': 'q2_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> callable(total_variation_distance) and (0 <= observed_tvd <= 1)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(total_variation_distance(np.array([0.5, 0.5]), np.array([1, 0])), 0.5) # Try again!\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> int(observed_tvd * 10 ** 7 % 8 ** 3) == 496\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
