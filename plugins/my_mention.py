import datetime

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない
@respond_to('How are you?')
def mention_func(message):
    message.reply('Awesome!') # メンション

@listen_to('bot')
def listen_func(message):
    message.send('呼んだ？') # ただの投稿

@listen_to('イカ東')
def ikatou_func(message):
    message.reply('分かる，イカ東だよね')     # メンション
    message.react('ikatou')     # リアクション

@listen_to('今何時？')
def time_func(message):
    message.send('そうね大体ね〜') # ただの投稿
    message.send(datetime.datetime.now().strftime('%Y年%m月%d日%H時%M分%S秒%f'))
    message.send('イカ東さを発揮してしまった…') # ただの投稿

