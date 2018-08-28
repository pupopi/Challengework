#第二章　チャレンジ

print("Hello, GC!")


#第三章　チャレンジ

#1 3つの異なる文字列

True
1.11111
"GC"

#2 変数が10以上と10未満でメッセージ

x=10
if x>=10:
    print("xは10以上です。")
else
    print("xは10未満です。")

#3 変数が10以下、10より大きく25以下、25より大きいときにメッセージ

x=24
if x<=10:
    print("xは10以下です。")
elif x<25:
    print("xは10より大きく25以下です。")
else:
    print("xは25より大きいです。")

#4 2つの値の割り算のあまり

15 % 2

#5 2つの値の割り算の商

16//3

#6 ageを用いた何かしらの条件分岐メッセージ

age=5
if age<20:
    print("あなたは未成年です。")
else:
    print("あなたは成人です。")



#第四章　チャレンジ

#1 二乗した値を返す関数

def f(x):
    return x*x

result=f(4)
print(result)


#2 引数を文字列にし、その文字列を出力する関数

#分からなくて答え見た

def print_string(string):
    print(string)

print_string("Testing: 1, 2, 3.")


#3 3つの必須引数と2つのオプション引数のある関数

def f(x,y,z,a=4,b=2):
    return a*x+b*y+z

result = f(2,3,5)
print(result)


#4 1つめの関数で整数を2で割って得られる整数を出力
#2つめの関数でこれを受け取り、4をかけて返す

def fir(x):
    return x/2

def sec(x):
    return x*4

y=fir(4)
result=sec(y)
print(result)


#5 文字列をfloat型に変更する関数。例外処理も含める。
#答え見た。

def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c)


#6　docstring書こう
#下記答え写し

def squared(x):
    """ Takes an int and returns it multiplied by 2.
    :param x: int.
    :return: x multiplied by 2.
    """
    return x ** 2


def print_string(string):
    """ Prints the string passed in.
    :param string: str.
    """
    print(string)

print_string("Testing: 1, 2, 3.")


def add_mult(a,b,c,x=100,z=1000):
    """ Returns the result of two optional params
    multiplied by the addition of 3 required params.
    :param a: int.
    :param b: int.
    :param c: int.
    :param x: int.
    :param z: int.
    :return: int.
    """
    return a + b + c * x * z


def convert(string):
    """ Converts passed in str to int.
    :param string: str.
    :return: string converted to int.
    """
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")



#第五章　チャレンジ

#1　好きなアーティストのリスト作成
artists=["C_ute", "magnoria_factory", "morning_musume."]
artists

#2　タプルのリスト作成。いったことのある場所の緯度と経度。
places=("Carlow", "52.836507", "-6.934136")
places

#3 辞書で自己紹介
my_index={"height":"167cm", "author":"James Tiptory jr.", "fav colour":"gray"}
my_index

#4 自己紹介辞書のキーを用いたバリュー取得
answer=input("What do you ask?:")
if answer in my_index:
    ans=my_index[answer]
    print(ans)

#5 好きなアーティスト辞書に曲リストを持たせる
songs={
    "C_ute":[
        "the Power", "夢幻クライマックス", "ファイナルスコール"
    ],
    "magnoria_factory":[
        "今夜だけ浮かれたかった", "笑って", "ハナモヨウ"
    ],
    "morning_musume.":[
        "A gonna", "しょうがない 夢追い人", "リゾナントブルー"
    ]
}
songs

#6 Pythonのset（コンテナ型）って？

#要素が順番を持たないコンテナ
#重複した要素は自動的に取り除かれる
#要素の総和や積などの計算や、要素数の取得も可能