test = {   'name': 'q4_7',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> joey_emotions = emotions_by_speaker('Joey Tribbiani')\n"
                                               ">>> joey_emotions.shape == (7, 1) and set(joey_emotions.columns) == {'probability'} and np.isclose(joey_emotions.get('probability').sum(), 1)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> phoebe_emotions = emotions_by_speaker('Phoebe Buffay')\n"
                                               ">>> np.all(phoebe_emotions.index == ['Joyful', 'Mad', 'Neutral', 'Peaceful', 'Powerful', 'Sad', 'Scared']) # Check row order.\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
