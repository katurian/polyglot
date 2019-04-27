import discord
from googletrans import Translator
from discord.ext.commands import Bot
import platform

client = Bot(description="translator for non-english speakers of Mandarin, Russian, Turkish and Spanish", command_prefix="!",
             pm_help=False)
server = client.get_server(id="564205805885325332")
translator = Translator()


@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__,
                                                                               platform.python_version()))
    print('--------')
    print('made by katski')
    return await client.change_presence(game=discord.Game(name='translating'))


@client.event
async def on_message(message):
    if (message.author.bot == True):
        return

    if (str(message.channel) == "general"):
        text = str(message.content)
        translatedmandarin = translator.translate(text, dest="zh-cn")
        await client.send_message(client.get_channel('570468481494155274'),
                                  "**" + str(message.author) + "**" + ": " + translatedmandarin.text)
        translatedturkish = translator.translate(text, dest="tr")
        await client.send_message(client.get_channel('570483736437850132'),
                                  "**" + str(message.author) + "**" + ": " + translatedturkish.text)
        translatedrussian = translator.translate(text, dest="ru")
        await client.send_message(client.get_channel('570490741537767424'),
                                  "**" + str(message.author) + "**" + ": " + translatedrussian.text)
        translatedspanish = translator.translate(text, dest="es")
        await client.send_message(client.get_channel('570500627122094091'),
                                  "**" + str(message.author) + "**" + ": " + translatedspanish.text)

    if (str(message.channel) == "관화"):
        text = str(message.content)
        translated = translator.translate(text)
        await client.send_message(client.get_channel('564205806308818963'),
                                  "**" + str(message.author) + "**" + ": " + translated.text)
        await client.send_message(client.get_channel('570483736437850132'),
                                  "**" + str(message.author) + "**" + ": " + translator.translate(translated.text,
                                                                                                  dest="tr").text)
        await client.send_message(client.get_channel('570490741537767424'),
                                  "**" + str(message.author) + "**" + ": " + translator.translate(translated.text,
                                                                                                  dest="ru").text)
        await client.send_message(client.get_channel('570500627122094091'),
                                  "**" + str(message.author) + "**" + ": " + translator.translate(translated.text,
                                                                                                  dest="es").text)

    if (str(message.channel) == "türk"):
        text = str(message.content)
        translated = translator.translate(text)
        await client.send_message(client.get_channel('564205806308818963'),
                                  "**" + str(message.author) + "**" + ": " + translated.text)
        await client.send_message(client.get_channel('570468481494155274'),
                                  "**" + str(message.author) + "**" + ": " + translator.translate(translated.text,
                                                                                                  dest="zh-cn").text)
        await client.send_message(client.get_channel('570490741537767424'),
                                  "**" + str(message.author) + "**" + ": " + translator.translate(translated.text,
                                                                                                  dest="ru").text)
        await client.send_message(client.get_channel('570500627122094091'),
                                  "**" + str(message.author) + "**" + ": " + translator.translate(translated.text,
                                                                                                  dest="es").text)

    if (str(message.channel) == "русский"):
        text = str(message.content)
        translated = translator.translate(text)
        await client.send_message(client.get_channel('564205806308818963'),
                                  "**" + str(message.author) + "**" + ": " + translated.text)
        await client.send_message(client.get_channel('570468481494155274'),
                                  "**" + str(message.author) + "**" + ": " + translator.translate(translated.text,
                                                                                                  dest="zh-cn").text)
        await client.send_message(client.get_channel('570483736437850132'),
                                  "**" + str(message.author) + "**" + ": " + translator.translate(translated.text,
                                                                                                  dest="tr").text)
        await client.send_message(client.get_channel('570500627122094091'),
                                  "**" + str(message.author) + "**" + ": " + translator.translate(translated.text,
                                                                                                  dest="es").text)

    if (str(message.channel) == "español"):
        text = str(message.content)
        translated = translator.translate(text)
        await client.send_message(client.get_channel('564205806308818963'),
                                  "**" + str(message.author) + "**" + ": " + translated.text)
        await client.send_message(client.get_channel('570468481494155274'),
                                  "**" + str(message.author) + "**" + ": " + translator.translate(translated.text,
                                                                                                  dest="zh-cn").text)
        await client.send_message(client.get_channel('570483736437850132'),
                                  "**" + str(message.author) + "**" + ": " + translator.translate(translated.text,
                                                                                                  dest="tr").text)
        await client.send_message(client.get_channel('570490741537767424'),
                                  "**" + str(message.author) + "**" + ": " + translator.translate(translated.text,
                                                                                                  dest="ru").text)


client.run('CLIENT-TOKEN')
