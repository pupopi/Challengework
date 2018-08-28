#チャレンジ６

#6-1 「カミュ」の文字を一文字ずつ出力
word="カミュ"
word[0]
word[1]
word[2]

#6-2 2つの文字列を入力させ、指定の文章を出力
word1=input("何を？:")
word2=input("誰に？:")
print("私は昨日"+word1+"を書いて"+word2+"に送った！")

#6-3 先頭を大文字に
letters="aldous Huxley was born in 1894."
letters.capitalize()

#6-4 文字列を分割
mozi="どこで? 誰が? いつ?"
mozi.split(" ")

#6-5 要素を連結
fox=["The", "fox", "jumped", "over", "the", "fence", "."]
fox=" ".join(fox)
fox = fox[0: -2] + "."
print(fox)

#6-6 sを＄に置換
sky="A screaming comes across the sky."
sky=sky.replace("s","$")
sky

#6-7 mのインデックス
hem="Hemingway"
"hem".index("m")

#6-8 好きな名セリフを出力（””処理）
print("You've got to ask yourself one question:'Do I feel lucky?'Well,do ya,pank?")

#6-9 "three three three"を作ろう
th1="three"+" three"+" three"
th1
th2=" three"*3
th2

#6-10 、でスライス
april="四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
april.index("、")
april[0:11]
april[11:]


#チャレンジ７

#7-1 リストの要素を出力
cinema=["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for show in cinema:
    print(show)

#7-2 25から50までを出力
for i in range(25, 51):
    print(i)

#7-3 1のリスト要素をインデックスとともに出力
for index, show in enumerate(cinema):
    print(index)
    print(show)

#7-4 qで終了する数字あて問題
#答え見た
numbers = [11, 32, 33, 15, 1]
while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")

#7-5 2つのリストの掛け算結果を新しいリストに保管
#途中から答え見た
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        mult = i * j
        list3.append(i * j)
print(list3)


#チャレンジ8

#8-1 statistics関数の別モジュール呼び出し
import statistics
nums=[11,15,65,98,25,23,21,45,75,65,325,25]
statistics.stdev(nums) #標本標準偏差

#8-2 
import cubed

result = cubed.cube_it(3)
print(result)


#チャレンジ9

#9-1 ほかのファイルを読み取ってコンテンツ出力
import os
os.path.join("Users", "tanabe", "Desktop", "独学プログラマー")
no=open("test.txt", "r", encoding="UTF-8")
string=no.read()
print(string)

#9-2 質問をして、入力された回答をファイルに出力しよう
answer = input("What is your favorite color?")
with open("fav_color.txt", "w") as f:
    f.write(answer)

#9-3 リストをcsvに書き出そう
film=[["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on fire", "Flight"]]

import csv
with open("film.csv", "w", newline="") as f:
    w=csv.writer(f, delimiter=",")
    w.writerow(["Top Gun", "Risky Business", "Minority Report"])
    w.writerow(["Titanic", "The Revenant", "Inception"])
    w.writerow(["Training Day", "Man on fire", "Flight"])

#9-4 3を日本語で
with open("j_film.csv", "w", newline="") as f:
    w=csv.writer(f, delimiter=",")
    w.writerow(["トップガン", "リスキー・ビジネス", "マイノリティーリポート"])
    w.writerow(["タイタニック", "ザ・レベナント", "インセプション"])
    w.writerow(["トレーニング・デイ", "マン・オブ・ファイア", "フライト"])


#チャレンジ10
#答え見た

import random


def hangman():
    word_list = ["Python", "Java", "computer", "hacker", "painter"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))

hangman()