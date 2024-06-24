test = {   'name': 'q5_5',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> isinstance(relationship, bpd.DataFrame) and 'couple' in relationship.columns and all(relationship.columns[:-1] == episodes.columns)\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> all(relationship[(relationship.get('season') == 3) & (relationship.get('episode') == 15)].get('couple')) # checking S3, E15 is marked as having a "
                                               'couple\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
