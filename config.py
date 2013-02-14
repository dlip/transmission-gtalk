# NOTICE : adapt this file and rename it to config.py

import logging,os

# the verbosity of the log, they are the standard python ones : DEBUG, INFO, ERROR ...
BOT_LOG_LEVEL = logging.DEBUG
BOT_BASE_DIR = os.path.split(os.path.realpath(__file__))[0]


# set the log file, None = console only, be sure the user of the bot can write there
BOT_LOG_FILE = os.path.join(BOT_BASE_DIR, "gtalk.log")

# Base configuration
BOT_IDENTITY = {
    'username' : 'something@gmail.com', # JID of the user you have created for the bot
    'password' : 'somepassword' # password of the bot user
}

BOT_ASYNC = True

BOT_ADMINS = ('someadmin@gmail.com',) # only those JIDs will have access to admin commands
BOT_DATA_DIR = os.path.join(BOT_BASE_DIR, "data") # Point this to a writeable directory by the system user running the bot

if not os.path.isdir(BOT_DATA_DIR):
  os.mkdir(BOT_DATA_DIR)

BOT_EXTRA_PLUGIN_DIR = os.path.join(BOT_BASE_DIR, "plugin") # Add this directory to the plugin discovery (useful to develop a new plugin locally)

# ---- Chatrooms configuration (used by the chatroom plugin)
# it is a standard python file so you can reuse variables...
# For example: _TEST_ROOM = 'test@conference.localhost'

# CHATROOM_ PRESENCE
# it must be an iterable of names of rooms you want the bot to join at startup
# for example : CHATROOM_PRESENCE = (_TEST_ROOM,)
CHATROOM_PRESENCE = ()

# CHATROOM_RELAY
# can be used to relay one to one message from specific users to the bot to MUCs
# it can be useful when XMPP notifiers like the standard Altassian Jira one doesn't support MUC
# for example : CHATROOM_RELAY = {'gbin@localhost' : (_TEST_ROOM,)}
CHATROOM_RELAY = {}

# REVERSE_CHATROOM_RELAY
# this feature forward whatever is said to a specific JID
# it can be useful if you client like gtalk doesn't support MUC correctly !
# for example REVERSE_CHATROOM_RELAY = {_TEST_ROOM : ('gbin@localhost',)}
REVERSE_CHATROOM_RELAY = {}

# CHATROOM_FN
# Some XMPP implementations like HipChat are super picky on the fullname you join with for a MUC
# If you use HipChat, make sure to exactly match the fullname you set for the bot user
CHATROOM_FN = 'bot'

HIPCHAT_MODE = False

TORRENT_USER="user"
TORRENT_PASSWORD="password"
GTALK_ANNOUNCEMENT_LIST = ('someadmin@gmail.com', )
TRANSMISSION_SERVER="dockstar"
TRANSMISSION_SERVER_PORT=9091
TRANSMISSION_SERVER_RPC="transmission/rpc/"
TRANSMISSION_LOG_FILE = os.path.join(BOT_BASE_DIR, "transmission.log")

BOT_PREFIX = '.'
BOT_LOG_SENTRY = False
SENTRY_DSN = ''
SENTRY_LOGLEVEL = BOT_LOG_LEVEL
ACCESS_CONTROLS = {}
DIVERT_TO_PRIVATE = ()
