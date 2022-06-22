message = input("> ")
words = message.split( " ")
emojis = {
   ":)" : "🙂", # Win + . 
   ":(" : "🙁",
   "lol" : "😂",
   "sick":"😨",
   "happy": "😀",
   "mermaid": "🧜‍"
}
outcome = " "
for word in words: # => ['hi', ':)', 'bi', ':(']
   outcome += emojis.get(word, word) + " "
print(outcome)