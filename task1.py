def country_descrip(name, **kwargs):
    print(f'{name}')
    for i in kwargs:
        print(f'{i} - {kwargs[i]}')


country_descrip(name='USA',
                population='330m',
                democratic=True)
country_descrip(name='Kyrgyzstan',
                area='200 km2',
                bordersWith=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])
