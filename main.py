import os
import discord
import random
import WebScraping

token = os.environ['TOKEN']

client = discord.Client() 

book = WebScraping.book()

wiki_url = 'https://pt.wikipedia.org/wiki/Especial:Pesquisar/'
dicio_url = 'https://www.dicio.com.br/'

coinflip = ['coroa', 'cara']

decisao = ["sim", "não", "talvez"]

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

  #Decisão aleatoria
  if msg.startswith('<3decida'):
    await message.channel.send(random.choice(decisao))
  
  #Coinflip
  if msg.startswith('<3coinflip'):
    await message.channel.send(random.choice(coinflip))

  #ScrapingWeb para conseguir ebooks da libgen
  if '<3book' in msg:
    key_words, search_words = book.key_words_search_words(msg)
    result_links = book.search(key_words)
    links = book.send_link(result_links, search_words)
    
    if len(links) > 0 and len(links) < 5:
     for link in links:
      await message.channel.send('https://libgen.is/' + link)
    elif len(links) > 0 and len(links) > 5:
      await message.channel.send('Achamos tantos resultados que seria melhor você selecionar o que deseja em: https://libgen.is/search.php?req=' + search_words.replace(' ','+'))
    else:
     await message.channel.send('Não conseguimos encontrar o livro que você deseja :-/')

  #Pesquisar na wikipedia
  if msg.startswith('<3wiki'):
    word = msg.split("<3wiki ", 1)[1]
    search_word = word.replace(' ','_')
    await message.channel.send(wiki_url + search_word)

  #Dicionario
  if msg.startswith('<3dicio'):
    word = msg.split("<3dicio ", 1)[1]
    search_word = word.replace(' ','_')
    await message.channel.send(dicio_url + search_word)
    
client.run(token)

