def obscene_adder(string):
    obscene_words = {'г****': 'говно',
                     'п******': 'пидарас',
                     'х**': 'хуй',
                     'п****': 'пизда',
                     'з*****': 'залупа',
                     'д******': 'давалка'}
    parse_string = string.split(' ')
    for i in range(len(parse_string)):
        if '*' in parse_string[i]:
            parse_string[i] = obscene_words[parse_string[i]]

    return parse_string
