import os
import discord
import random
import WebScraping

token = os.environ['TOKEN']

client = discord.Client() 

ball = ["sim", "não", "talvez"]
##
wiki_url = 'https://pt.wikipedia.org/wiki/Especial:Pesquisar/'
##

#google = WebScraping.google()
#no_result_message = '''Não conseguimos encontrar nenhum relacionada a isso :-/'''

@client.event
async def on_message(message):
  if message.author == client.user:
   return  

  msg = message.content.lower() 

  #Teste de conexão
  if msg.startswith('<3ping'):
    await message.channel.send('Pong')

  #Conseguir documentação de linguagens
  if msg.startswith('<3doc'):
    await message.channel.send ('Consiga a documentação das linguagens escrevendo **"<3Doc" + o nome de cada lang**. Comandos aceitos: ```<3Doc python | <3Doc pandas```')
  if msg.startswith('<3doc python'):
    await message.channel.send('https://docs.python.org/pt-br/3/tutorial/')
  if msg.startswith('<3doc pandas'):
    await message.channel.send('https://pandas.pydata.org/docs/')

  #8Ball
  if msg.startswith('<3decida'):
    await message.channel.send(random.choice(ball))
  
  #ScrapingWeb, erro => todos os resultados são enviados gerando SPAM, desejavel que apenas o primeiro resultado seja enviado como mensagem 
  #if '<3search' in msg:
    #key_words, search_words = google.key_words_search_words(msg)
    #result_links = google.search(key_words)
    #links = google.send_link(result_links, search_words)
    
    ##if len(links) > 0:
     #for link in links:
      ##await message.channel.send(link)
    #else:
     #await message.channel.send(no_result_message)

  #Pesquisar na wikipedia
  if msg.startswith('wiki'):
    words = msg.split("wiki ", 1)[1]
    search_words = words.replace(' ','_')
    await message.channel.send(wiki_url + search_words)
    

client.run(token)

