from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi💘 {message.from_user.first_name}!
\n⚜️I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!

⚜️ Do you want me to play music in your Telegram groups'voice chats? Please click the '⚜️Manual ' button below to know how you can use me.

⚜️ The Assistant must be in your group to play music in the voice chat of your group.

⚜️ More info & commands mentioned in the MANUAL 

A project by patricia's
\nTo add in your group contact us at @patricia_support.
\nHit /help list of available commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                
                [
                    InlineKeyboardButton(
                        "⚜️Support⚜️", url="https://t.me/patricia_support"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/patricia_updates"
                    )        
                     ],
                [
                    InlineKeyboardButton(
                        "⚜️ Add To Your Group ⚜️", url="https://t.me/patriciaXmusic_bot?startgroup=true"
                    ),
                      InlineKeyboardButton(
                        "⚜️mannual⚜️", url="https://telegra.ph/MANUAL-04-30-4"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥 Channel", url="https://t.me/patricia_updates"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/saavn <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/splay <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥 Channel", url="https://t.me/patricia_updates"
                    )
                ]
            ]
        )
    )    
