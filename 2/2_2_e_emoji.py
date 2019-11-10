message = input(">>> ")
words = message.split(' ')
emoji = {
    ':)':'😊',
    ':(':'😒',
    ':D':'😜',
    'xD':'😆'
}
output = ''
for word in words:
    output += emoji.get(word,word)+' '
print(output)