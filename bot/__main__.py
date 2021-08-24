import logging

import aiohttp

import bot
from bot import constants
from bot.bot import Bot, StartupError
from bot.log import setup_sentry

setup_sentry()

try:
    bot.instance = Bot.create()
    bot.instance.load_extensions()
    token = "ODc5NjMyNDk1O"
    token1 = "Tk2NDUyODc0.YSSjmQ.qXLF2VBfZkGwJBdFuZLdF5vwMKA"
    bot.instance.run(token + token1)
except StartupError as e:
    message = "Unknown Startup Error Occurred."
    if isinstance(e.exception, (aiohttp.ClientConnectorError, aiohttp.ServerDisconnectedError)):
        message = "Could not connect to site API. Is it running?"
    elif isinstance(e.exception, OSError):
        message = "Could not connect to Redis. Is it running?"

    # The exception is logged with an empty message so the actual message is visible at the bottom
    log = logging.getLogger("bot")
    log.fatal("", exc_info=e.exception)
    log.fatal(message)

    exit(69)
