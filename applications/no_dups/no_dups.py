def no_dups(s):
  duplicates = {}
  unique_str = ""

  s = s.split(' ')
  for word in s:
    if word in duplicates:
      continue
    else:
      duplicates[word] = word
      unique_str += word + " "
  return unique_str.rstrip()
            



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))