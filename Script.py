class script(object):
    START_TXT = """đˇđ´đťđťđž {}đ,
đźđ đ˝đ°đźđ´ đ¸đ <a href=https://t.me/{}>{}</a>, đ¸ đ˛đ°đ˝ đżđđžđđ¸đłđ´ đ°đťđť đ˝đ´đ đźđžđđ¸đ´đ, đšđđđ đ°đłđł đźđ´ đđž đđžđđ đśđđžđđż đ°đ˝đł đ´đ˝đšđžđ """
    HELP_TXT = """đˇđ´đ {}
đˇđ´đđ´ đ¸đ đđˇđ´ đˇđ´đťđż đľđžđ đźđ đ˛đžđźđźđ°đ˝đłđ."""
    ABOUT_TXT = """đđđ˘đ¨đ§ đ đŚđ đđ đđđđđđ
âľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľ
ââââââ° áŚđłęŞá§ęŞŽęŞ âąâââąâŰŞŰŞ
ââ­ââââââââââââââââŁ 
ââŁâŞź đđ đđŞđśđŽ - đłđđ°đśđžđ˝
ââŁâŞź đđťđŽđŞđ˝đ¸đť - <a href=https://t.me/Hari_OP>đˇđ°đđ¸</a>
ââŁâŞź đđ˛đŤđťđŞđťđťđ - đżđđđžđśđđ°đź
ââŁâŞź đđŞđˇđ°đžđŞđ°đŽ - đżđđđˇđžđ˝ đš
ââŁâŞź đđŞđ˝đŞ đđŞđźđŽ - đźđžđ˝đśđž đłđą
ââŁâŞź đđ¸đ˝ đźđŽđťđżđŽđť -  đˇđ´đđžđşđ
ââŁâŞź đđžđ˛đľđ­ đ˘đ˝đŞđ˝đžđź - v1.0.1 [ đąđ´đđ° ]
ââ°ââââââââââââââââŁ
âââââââââââââââââââââąâ"""
    SOURCE_TXT = """đđđ đđđđ
âľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľâľ
ââââââ° áŚđłęŞá§ęŞŽęŞ âąâââąâŰŞŰŞ
ââ­ââââââââââââââââŁ
ââŁđŻâ¨á´Ąá´Ęá´á´á´á´ á´á´ ę°ĘÉŞá´ęą Ęá´ á´ę°ę°ÉŞá´ÉŞá´ĘâŁ
ââŁâĄď¸đŹá´á´ÉŞÉ´ á´á´Ę á´á´á´ ÉŞá´ęą á´Ęá´É´É´á´Ęęą đŚâ¨
ââŁ
ââŁ<a href=https://t.me/TAMIL_FLIMS_HD>đ°âĽ âˇ á´á´ÉŞÉ´ á´Ęá´É´É´á´Ę â</a>
ââŁ<a href=https://t.me/+lp5mOR6wSMIyMzY1>đ°âĽ âˇ ę°ĘÉŞá´ęą Ęá´ á´ę°ę°ÉŞá´ÉŞá´Ę ę°ÉŞĘá´ 1 â</a>
ââŁ<a href=https://t.me/+VyuE_q8JC9UzZTll>đ°âĽ âˇ ę°ĘÉŞá´ęą Ęá´ á´ę°ę°ÉŞá´ÉŞá´Ę ę°ÉŞĘá´ 2 â</a>
ââŁ<a href=https://t.me/+TJzbQrEhZBg3ZGRl>đ°âĽ âˇ ę°ĘÉŞá´ęą Ęá´ á´ę°ę°ÉŞá´ÉŞá´Ę ę°ÉŞĘá´ 3 â</a>
ââŁ
ââŁđŚ á´Ę Ęá´sá´ ŇĘÉŞá´É´á´ :<a href=tg://settings>á´ĘÉŞs á´á´Ęsá´É´ đ</a>
ââ°ââââââââââââââââŁ
âââââââââââââââââââââąâ"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and DRAGON will respond whenever a keyword is found the message

<b>NOTE:</b>
1. DRAGON should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â˘ /filter - <code>add a filter in chat</code>
â˘ /filters - <code>list all the filters of a chat</code>
â˘ /del - <code>delete a specific filter in chat</code>
â˘ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """<b>Help: Buttons</b>

- <b>THOR Supports both url and alert inline buttons.</b>

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. DRAGON supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/TAMILHB)</code>

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
â˘ /connect  - <code>connect a particular chat to your PM</code>
â˘ /disconnect  - <code>disconnect from a chat</code>
â˘ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
â˘ /id - <code>get id of a specifed user.</code>
â˘ /info  - <code>get information about a user.</code>
â˘ /imdb  - <code>get the film information from IMDb source.</code>
â˘ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â˘ /logs - <code>to get the rescent errors</code>
â˘ /stats - <code>to get status of files in db.</code>
â˘ /delete - <code>to delete a specific file from db.</code>
â˘ /users - <code>to get list of my users and ids.</code>
â˘ /chats - <code>to get list of the my chats and ids </code>
â˘ /leave  - <code>to leave from a chat.</code>
â˘ /disable  -  <code>do disable a chat.</code>
â˘ /ban  - <code>to ban a user.</code>
â˘ /unban  - <code>to unban a user.</code>
â˘ /channel - <code>to get list of total connected channels</code>
â˘ /broadcast - <code>to broadcast a message to all users</code>
â˘ /donate - <code>to donate any gifts for my owner</code>"""
    STATUS_TXT = """ââââââ° áŚđłęŞá§ęŞŽęŞ âąâââąâŰŞŰŞ
ââ­ââââââââââââââââŁ 
ââŁâŞź đđžđđ°đť đľđ¸đťđ´đ: <code>{}</code>
ââŁâŞź đđžđđ°đť đđđ´đđ: <code>{}</code>
ââŁâŞź đđžđđ°đť đ˛đˇđ°đđ: <code>{}</code>
ââŁâŞź đđđ´đł đđđžđđ°đśđ´: <code>{}</code> đźđđą
ââŁâŞź đľđđ´đ´ đđđžđđ°đśđ´: <code>{}</code> đźđđą
ââŁ
ââŁâŞźđłđ´đđ:âŞź <a href=https://t.me/TAMIL_FLIMS_HD>đłđđ°đśđžđ˝</a>
ââ°ââââââââââââââââŁ
âââââââââââââââââââââąâ"""
    DONATE_TXT = """<Hey {}
[Here is the Donation Link](https://t.me/TAMIL_FLIMS_HD) â¤"""
    LOG_TEXT_G = """#đ˝đđ  đśđđđđ
đśđđđđ = {}(<code>{}</code>)
đđđđđ đźđđđđđđ = <code>{}</code>
đ°đđđđ đąđ- {}
"""
    LOG_TEXT_P = """#đ˝đđ  đđđđ
đ¸đł - <code>{}</code>
đ˝đ°đźđ´ - {}
"""
