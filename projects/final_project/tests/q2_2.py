test = {   'name': 'q2_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure you are storing the words in a list.\n'
                                               ">>> len(signatures.columns) == 6 and 'words' in signatures.columns and type(signatures.get('words').iloc[0]) == list\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # Make sure your lists include all lowercase words.\n>>> signatures.get('signature').iloc[0].lower()==signatures.get('signature').iloc[0]\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
