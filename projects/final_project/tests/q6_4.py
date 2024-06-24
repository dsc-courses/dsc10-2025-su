test = {   'name': 'q6_4',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> callable(find_prob_distribution) and isinstance(find_prob_distribution('The'), bpd.DataFrame)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(find_prob_distribution('The').get('prob').loc['One'], 0.9872881355932204)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(find_prob_distribution('with').get('prob').sum(), 1)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
