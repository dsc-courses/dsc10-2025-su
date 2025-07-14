test = {   'name': 'q3_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(boot_matcha_proportions, np.ndarray) and len(boot_matcha_proportions) == 1000\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.all(np.isclose(boot_matcha_proportions, matcha_proportion)) == False # It looks like all of your resamples have the same mean – take a closer '
                                               "look at how you're resampling!\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
