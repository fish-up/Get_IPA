# coding=UTF-8
# Enter a sentence, return all the pronunciations with pos of each word

import requests
import lxml
from bs4 import BeautifulSoup
from colorama import init,Fore

init(autoreset=True)
root_url = 'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/'

while True:
    sentence = input('Type in words you want to search in cambridge dict (or "q" to leave): ')
    if sentence == 'q':
        break
    else:
        word_list = sentence.split()
        for raw_word in word_list:
            try:
                url = root_url + raw_word
                headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
                res = requests.get(url, headers=headers)
                soup = BeautifulSoup(res.text, 'lxml')
                tag_soup = soup.find_all(class_='pos-header dpos-h')  # get every definition block

                word = soup.find(class_='hw dhw').get_text()
                print(Fore.YELLOW + word)
                for def_block in tag_soup:
                    pos = def_block.find(class_= 'pos dpos')
                    # get the part of speech of the word followed by : if exists
                    pos = pos.get_text() + ':' if pos != None else ''
                    pos = pos.capitalize()
                    # get every uk pronunciation in the block
                    all_pron = def_block.find_all(class_='uk dpron-i')
                    ipa = ''
                    # concatenate the pronunciations
                    for pron in all_pron:
                        ipa += pron.find(class_= 'pron dpron').get_text() + ' '
                    print(Fore.WHITE + pos + Fore.WHITE + ipa)
                print(Fore.YELLOW + '='*30)
            except:
                print(Fore.GREEN + 'Could not find the word ' + Fore.BLUE + raw_word)
                print(Fore.YELLOW + '=' * 30)
