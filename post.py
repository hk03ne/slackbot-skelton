import os
import sys
from slacker import Slacker

if __name__ == '__main__':
  slack = Slacker(os.environ['SLACKBOT_API_TOKEN'])
  slack.chat.post_message(
    sys.argv[1],
    sys.argv[2],
    as_user=True
    )
