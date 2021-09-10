import os
import discord
import random
import WebScraping

token = os.environ['TOKEN']

client = discord.Client() 

ball = ["sim", "não", "talvez"]

wiki = WebScraping.wiki()

no_result_message = '''Não conseguimos encontrar nenhuma wiki relacionada a isso :-/'''

@client.event
async def on_message(message): #função que é executada quando uma mensagem é enviada

  if message.author == client.user: #se a mensagem for do proprio bot
   return  

  msg = message.content.lower()

  if msg.startswith('<3ping'):
    await message.channel.send('Pong')

  if msg.startswith('<3doc'):
    await message.channel.send ('Consiga a documentação das linguagens escrevendo **"<3Doc" + o nome de cada lang**. Comandos aceitos: ```<3Doc python | <3Doc pandas```')
  if msg.startswith('<3doc python'):
    await message.channel.send('https://docs.python.org/pt-br/3/tutorial/')
  if msg.startswith('<3doc pandas'):
    await message.channel.send('https://pandas.pydata.org/docs/')

  #8Ball
  if msg.startswith('<3decida'):
    await message.channel.send(random.choice(ball))

  if '<3search' in msg:
    key_words, search_words = wiki.key_words_search_words(msg)
    result_links = wiki.search(key_words)
    links = wiki.send_link(result_links, search_words)
    
    if len(links) > 0:
     for link in links:
      await message.channel.send(link)
    else:
     await message.channel.send(no_result_message)

client.run(token)

