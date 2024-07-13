test = {   'name': 'q1_9',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> isinstance(chains_growth, bpd.DataFrame) and list(chains_YOY.columns)  == ['Rank', 'Restaurant', 'Sales', 'YOY_Sales', 'Segment_Category', "
                                               "'Sales_2019'] # Make sure chains_YOY remains unchanged.\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(chains_growth.get('Growth_Category').take(np.arange(10)) == np.array([3, 1, 5, 3, 4, 2, 2, 1, 5, 4]))\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
