from multiprocessing.connection import answer_challenge


def translate(word_or_phrase):
  vowel_list = ['a', 'e', 'i', 'o', 'u']
  answer = ""
  word_list = word_or_phrase.split()
  if len(word_list) == 1:
    one_word = ''.join(word_list)
    if one_word[0] in vowel_list:
      answer = one_word + 'ay'
    else:
      wor_list = list(one_word)
      while wor_list[0] not in vowel_list:
        if wor_list[0] == 'q' and wor_list[1] == 'u':
          temp = wor_list
          wor_list.append(temp[0])
          wor_list.append(temp[1])
          wor_list.pop(0)
          wor_list.pop(0)
        else:
          temp = wor_list
          wor_list.append(temp[0])
          wor_list.pop(0)
      answer = ''.join(wor_list) + 'ay'

      
  else:
    ans = []
    for key in word_list:
      if key[0] in vowel_list:
        ans.append(key + 'ay')
      elif key[0] not in vowel_list:
        work_list = list(key)
        while work_list[0] not in vowel_list:
          if work_list[0] == 'q' and work_list[1] == 'u':
            temp = work_list
            work_list.append(temp[0])
            work_list.append(temp[1])
            work_list.pop(0)
            work_list.pop(0)
          else:
            temp = work_list
            work_list.append(temp[0])
            work_list.pop(0)
        ans.append(''.join(work_list) + 'ay')
        answer = ' '.join(ans)

  return answer

