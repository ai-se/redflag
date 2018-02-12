import os

names = ['timm', 'wfu', 'rahlk', 'vivekaxl','george', 'jf', 'zhe', 'jack', 'amrit', 'patrick', 'ken', 'junjie']

for name in names:
	os.system('mkdir ' + name)
	os.system('mkdir ' + name + '/Journal')
	os.system('touch ' + name + '/Journal/.keep')
	os.system('mkdir ' + name + '/Conference')
	os.system('touch ' + name + '/Conference/.keep')


print 'Done'
