from pick import pick

title = 'Velg et rom å gå inn i:  '
rom = ['1','2','3','4','5']

option, index = pick(rom, title, indicator='=>', default_index=2)