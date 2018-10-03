#censor given words in a given text
def censor(text,word):
  words = text.split()
  for index,x in enumerate(words):
    if word == x:
      words[index] = "*" * len(x)
  return ' '.join(words) 