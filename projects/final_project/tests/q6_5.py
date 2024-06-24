test = {   'name': 'q6_5',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> callable(generate_title) and isinstance(generate_title(), str)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> generate_title()[:4] == 'The '\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> pilot = 0\n'
                                               '>>> for i in range(100):\n'
                                               "...     if generate_title() == 'The Pilot':\n"
                                               '...         pilot += 1\n'
                                               '...         \n'
                                               ">>> pilot < 3 # 'The Pilot' should occur rarely if you are doing this correctly.\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
