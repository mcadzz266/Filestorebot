#(©)Codexbotz

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL1, FORCE_SUB_GROUP1, FORCE_SUB_CHANNEL2, CHANNEL_ID, PORT

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/moviecomplexofficialgroup for movies")
                sys.exit()
        if FORCE_SUB_GROUP:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_GROUP)
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_GROUP!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_GROUP dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Group Saat Ini: {FORCE_SUB_GROUP}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()
        if FORCE_SUB_CHANNEL1:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL1)
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_CHANNEL1!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL1 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_CHANNEL}"
     
                )
                sys.exit()
        if FORCE_SUB_CHANNEL2:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                self.invitelink5 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_CHANNEL2!"            
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()
        if FORCE_SUB_GROUP1:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_GROUP1)
                self.invitelink4 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_GROUP1!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_GROUP1 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Group Saat Ini: {FORCE_SUB_GROUP}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/moviecomplexofficialgroup for movies")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/Viruzss")
        self.LOGGER(__name__).info(f""" \n\n       
░█████╗░░█████╗░██████╗░███████╗██╗░░██╗██████╗░░█████╗░████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝╚════██║
██║░░╚═╝██║░░██║██║░░██║█████╗░░░╚███╔╝░██████╦╝██║░░██║░░░██║░░░░░███╔═╝
██║░░██╗██║░░██║██║░░██║██╔══╝░░░██╔██╗░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝███████╗██╔╝╚██╗██████╦╝╚█████╔╝░░░██║░░░███████╗
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝
                                          """)
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
