test = {   'name': 'q1_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> 1 <= roll_result <= 20\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 12 <= modified_result <= 31\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> action_succeeded in [True, False]\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.isclose(np.std(possible_rolls) * 2578 % 13, 6.473184530655999) # Check how you've defined possible_rolls. What values are possible when you "
                                               'roll a 20-sided die?\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
