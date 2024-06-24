test = {   'name': 'q1_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> isinstance(avg_age,bpd.DataFrame) and avg_age.shape == (466, 3) and 'Average_Age' in avg_age.columns and baby.shape == (296491, 5) # Don't change "
                                               'the original baby DataFrame.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.isclose(avg_age[(avg_age.get('Name') == 'Charles') & (avg_age.get('Gender') == 'F')].get('Average_Age').iloc[0], 74.65128739395743)\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
