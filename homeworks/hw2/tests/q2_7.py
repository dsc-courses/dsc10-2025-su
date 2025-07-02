test = {   'name': 'q2_7',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> callable(most_played) and isinstance(most_played('Pinball', 5), bpd.DataFrame)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> most_played('Pinball', 5).shape == (1, 8) and most_played('Arcade', 5).shape == (5, 8)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> sum(most_played('Card & Board Game', 9).index) == 5366 # Try again!\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
