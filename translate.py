# Dicionaries

slang = {'mate':'buddy', 'knackered':'tired', 'cheeky':'offensive'}

sentence = 'Sorry, my ' + 'mate' + "'s a bit " + 'cheeky' + '!'

translation = 'Sorry, my ' + slang.get('mate') + "'s a bit " + slang.get('cheeky') + '!'

print(sentence)
print(translation)
