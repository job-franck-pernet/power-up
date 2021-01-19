# -*- coding: iso-8859-15 -*-

__author__ = "Franck Pernet"
__license__ = ""
__version__ = "2021-01-18"
__email__ = "job.franck.pernet@gmail.com"

import os.path

class anki():

  def __init__(self, file):
    self._session_filename = file
    self._boxes_start = {'red':[],'orange':[],'green':[]}
    self._boxes_result = {'red':[],'orange':[],'green':[]}

  def session(self):    
    try:
      self.__load_session()
    except:
      return

    print(f"Hello and welcome to this new anki session.")

    for box, cards in self._boxes_start.items():
      for card in cards:
        self._boxes_result[self.__question (card)].append(card)
    
    if (0 == len(self._boxes_result['red']) and 0 == len(self._boxes_result['orange'])):
      print("Congratulation, you have cleared all the cards.") 
    else:
      print("Good by, see you next session.")
      self.__prepare_next_sesion()
    
    self.__save_session()

  def __question(self, card):
    print(f"\nQuestion: {card[0]}")
    answer = input("Answer: ")
    if answer == card[1] or answer.lower() == card[1].lower():
      print("--> correct")
      return 'green'
    else:
      almost = False
      
      answer_words = answer.split(' ')
      # card_words = card[1].split(' ')
      card_words = [word.lower() for word in card[1].split(' ')]
      for word in answer_words:
        if word.lower().strip() in card_words:
          almost = True
          break

      if True == almost:
        print("--> almost, the exact answer is:")
        print(f"    {card[1]}")
        return 'orange'
      else:
        print("--> wrong, the correct answer is:")
        print(f"    {card[1]}")
        return 'red'
        
  def __prepare_next_sesion(self):
    self._boxes_result['red'].extend(self._boxes_result['orange'])
    self._boxes_result['orange'] = self._boxes_result['green']
    self._boxes_result['green'] = []

  def __load_session(self):
    line_index = 0
    if not os.path.isfile(self._session_filename):
      print(f"ERROR, deck filename \"{self._session_filename}\" doesn't exist.")
      raise FileNotFoundError()

    with open(self._session_filename, "r") as src_file:
       for line in src_file:
          line = line.strip()
          box_color = 'red'
          fields = line.split('|')
          if 0 != line_index:
            if len(fields) > 1:
              if len(fields) > 2:
                if fields[2] in ['red', 'orange']:
                  box_color = fields[2]
              card = (fields[0], fields[1])
              self._boxes_start[box_color].append(card)
            else:
              print(f"ERROR: session file error line {line_index}")
          line_index += 1

  def __save_session(self):
    with open(self._session_filename, 'w') as dst_file:
      dst_file.write("card question|card answer|box\n") 
      for box, cards in self._boxes_result.items():
        for card in cards:
          dst_file.write(f"{card[0]}|{card[1]}|{box}\n")
