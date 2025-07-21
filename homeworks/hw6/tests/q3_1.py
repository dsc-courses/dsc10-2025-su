test = {   'name': 'q3_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> anime_labeled.shape == (11440, 7)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> list(anime_labeled.columns) == ['Name', 'English name', 'Episodes', 'Aired', 'Genres', 'Score', 'Award_Status'] # Name the new column "
                                               "'Award_Status'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(anime_labeled.get('Award_Status').unique() == np.array(['Award-Winning', 'No Award']))  # Make sure the new column's values are either "
                                               '`Award-Winning` or `No Award`\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
