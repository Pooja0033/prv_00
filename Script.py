class script(object):
    START_TXT = """ð·ðīðŧðū {},
ðžð ð―ð°ðžðī ðļð <a href=https://t.me/{}>{}</a>, ð ðð ð ðððððð ððð ðð ððð ððð ððð ðð ðð ðððð ððððð ððððð ððð ðððð ðð ðð ððððð..."""
    HELP_TXT = """ð·ðīð {}
ð·ðīððī ðļð ðð·ðī ð·ðīðŧðŋ ðĩðūð ðžð ðēðūðžðžð°ð―ðģð."""
    ABOUT_TXT = """áīÉīáīáīy áīáī áīĘy áīáīáīáīÉīáī Ęáīáīáīáīęąáī áīáīáīáīĘ ÉŠęą áīÉīáīxáīĐáīáīáīáīáī

âĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩ

ââââââ° PRANAV âąâââąâÛŠÛŠ
â
ââ­ââââââââââââââââĢ 
ââĢâŠž âáīĘ Éīáīáīáī    - {}
ââĢâŠž ðð ððð ððĄ   - <a href="https://t.me/KL_2335"> Prv </a>
ââĢâŠž ðēððīð°ððūð     - <a href="https://t.me/Prv_35"> KMTZ </a>
ââĢâŠž ððĨðĒðĻðĢ      âū <a href="https://t.me/kmtz_v3"> KMTZ GP1ïļâĢ </a>
ââĢâŠž ððĨðĒðĻðĢ      âū <a href="https://t.me/kmtz_v4"> KMTZ GP2ïļâĢ </a>
ââĢâŠž ððĨðĒðĻðĢ      âū <a href="https://t.me/kmtz_v5"> KMTZ GP3ïļâĢ </a>
ââĢâŠž ððĩðŪðŧðŧðēðđ      - <a href="https://t.me/kmtz_channel_v3"> ðð ð§ð­ ððĩðŪðŧðŧðēðđ </a>
ââĢâŠž âðŧðļðąðð°ðð    - ðð ð§ð­ ððððĨððĨðŽ
ââĢâŠž âðŧð°ð―ðķðð°ðķðī   - ð ððĄððððĶð
ââĢâŠž âðģð°ðð° ðąð°ððī  - āīļāĩāīāī°āĩāīŊāīŪāīŋāīēāĩāīē āīāīūāīĢāīŋāīāĩāīāīūāĩŧ
ââĢâŠž âðąðūð ððīðððīð - ðĻð
ââĢâŠž âððððð      - āīāī°āĩāī āīŠāĩāīāīŋāīāĩāīāīĢāĩāī āīāīēāĩāīēāīūāīĩāĩžāīāĩāīāĩāī āīāīŋāīāĩāīāĩāī
"""

    SOURCE_TXT = """<b>ðŋððļðð°ððī ðąðūð ðĩðūð ððūð</b>

<b>âšâš ðģðū ððūð ðð°ð―ð ð° ðąðūð ðð°ðžðī ðŧðļðšðī ðð·ðļð</b>

<b>âšâš ððļðð· ð°ðŧðŧ ððūðð ðēððīðģðļðð</b>

<b>âšâš ððļðð· ððūðð ðūðð―ðīððð·ðļðŋ</b>

<b>âšâš ðēðūð―ðð°ðēð ðžðī <a href=https://t.me/KL_2335> ððð </a></b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Prv should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âĒ /filter - <code>add a filter in chat</code>
âĒ /filters - <code>list all the filters of a chat</code>
âĒ /del - <code>delete a specific filter in chat</code>
âĒ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Prv Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Prv supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Prv_35)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âĒ /connect  - <code>connect a particular chat to your PM</code>
âĒ /disconnect  - <code>disconnect from a chat</code>
âĒ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Prv

<b>Commands and Usage:</b>
âĒ /id - <code>get id of a specified user.</code>
âĒ /info  - <code>get information about a user.</code>
âĒ /imdb  - <code>get the film information from IMDb source.</code>
âĒ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âĒ /logs - <code>to get the rescent errors</code>
âĒ /stats - <code>to get status of files in db.</code>
âĒ /delete - <code>to delete a specific file from db.</code>
âĒ /users - <code>to get list of my users and ids.</code>
âĒ /chats - <code>to get list of the my chats and ids </code>
âĒ /leave  - <code>to leave from a chat.</code>
âĒ /disable  -  <code>do disable a chat.</code>
âĒ /ban  - <code>to ban a user.</code>
âĒ /unban  - <code>to unban a user.</code>
âĒ /channel - <code>to get list of total connected channels</code>
âĒ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â ððūðð°ðŧ ðĩðļðŧðīð: <code>{}</code>
â ððūðð°ðŧ ðððīðð: <code>{}</code>
â ððūðð°ðŧ ðēð·ð°ðð: <code>{}</code>
â ðððīðģ ðððūðð°ðķðī: <code>{}</code> ðžððą
â ðĩððīðī ðððūðð°ðķðī: <code>{}</code> ðžððą"""
    LOG_TEXT_G = """#NewGroup
âŪ Group = {}(<code>{}</code>)
âŪ Total Members = <code>{}</code>
âū Added By - {}
"""
    LOG_TEXT_P = """#NewUser
âŪ ID - <code>{}</code>
âŪ Name - {}
"""
