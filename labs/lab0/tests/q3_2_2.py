test = {   'name': 'q3_2_2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> seconds_in_a_decade != seconds_in_a_day * 10 * 365 # Close, but not quite! It looks like you didn't account for leap years. See: "
                                               'https://en.wikipedia.org/wiki/Leap_year\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> seconds_in_a_decade != seconds_in_a_day * 10 * 365.25 # Close, but not quite! Remember that 365.25 is an average number of days per year over many '
                                               'years. For the given decade, consider how many days each of those years contained, which depends on whether the year is a leap year or not. See: '
                                               'https://en.wikipedia.org/wiki/Leap_year\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> seconds_in_a_decade != 315532800 # Very close! Make sure to account for leap seconds, which are different than leap years. See: '
                                               'https://en.wikipedia.org/wiki/Leap_second\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> seconds_in_a_decade == 315532802 # The correct answer is 315532802, which is not quite what you have. Try again, until you understand how to get '
                                               'to this answer!\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
