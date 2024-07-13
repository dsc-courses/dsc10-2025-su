test = {   'name': 'q1_12',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(invest_segment_categories, np.ndarray) and len(invest_segment_categories) == 3 # Pick 3 segment categories to invest in.\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> set(invest_segment_categories).issubset(set(chains.get('Segment_Category').values)) # Check for a spelling mistake in your segment categories.\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
