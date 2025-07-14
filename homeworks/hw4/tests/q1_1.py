test = {   'name': 'q1_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> callable(simulate_one_ticket) and isinstance(simulate_one_ticket(), np.ndarray) # Make sure simulate_one_ticket is a function that returns an '
                                               'array.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> len(simulate_one_ticket()) == 6 # Make sure the returned array has 6 numbers in it.\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> a = simulate_one_ticket()\n'
                                               '>>> np.array([True if 1 <= i <= 29 else False for i in a[:5]]).all() and 1 <= a[-1] <= 12 # Your array has some incorrect values in it!\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
