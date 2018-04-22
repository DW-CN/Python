favorite_languages = {
	'jen': 'Python',
	'dennis': 'C',
	'sarch': 'ruby',
	'phil': 'Python',
	}

friends = ['dennis','jen']

for name in  favorite_languages.keys():
	print(name.title())

	if name in friends:
		print("    Hi " + name.title() + ",I see your favorite language is " + favorite_languages[name]+"!")