from slackbot.bot import respond_to
from slackbot.bot import listen_to

@respond_to('test')
def res_test(message):
  message.reply('test ok!')

@listen_to('.*疲れ.*')
@respond_to('.*疲れ.*')
@listen_to('.*つかれ.*')
@respond_to('.*つかれ.*')
def cheer(message):
  message.reply('おつかれさまー')
