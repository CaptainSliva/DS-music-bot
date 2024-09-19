import discord
from discord.ext import commands
from discord.utils import get
import Functions as fs

# from dotenv import load_dotenvE
from config import settings


# intents = discord.Intents.all() # or .all() if you ticked all, that is easier
# intents.members = True # If you ticked the SERVER MEMBERS INTENT
bot = commands.Bot(command_prefix = settings['prefix'], intents = discord.Intents.all())
# client = discord.Client(intents=intents)


# Начало бота

@bot.event
async def hello():
    print('Hello, I`m there')

@bot.command()
async def test(ctx):
    await ctx.send('я тут')
    guild = ctx.message.guild
    await guild.create_text_channel('cool-channel')


@bot.command(name = 'connect') # Подключение бота к голосовому каналу
async def connect(ctx):
    global vc
    channel = ctx.message.author.voice.channel
    vc = get(bot.voice_clients, guild = ctx.guild)

    if vc and vc.is_connected():
        await vc.move_to(channel)
        await ctx.send(f'Бот присоединился к каналу: {channel}')
    else:
        await channel.connect()
        await ctx.send(f'Бот уже присоединился к каналу: {channel}')



@bot.command(name = 'disconnect') # Отключение бота от голосового канала
async def disconnect(ctx):
    channel = ctx.message.author.voice.channel
    vc = get(bot.voice_clients, guild = ctx.guild)

    if vc and vc.is_connected():
        await vc.disconnect()
        await ctx.send(f'Бот отключился от канала: {channel}')
    else:
        # await channel.connect()
        await ctx.send('Бот не подключен к каналу')


@bot.command(name = 'play')
async def music_play(ctx, url):
    global voice_channel
    
    # try :
    server = ctx.message.guild
    vc = get(bot.voice_clients, guild = ctx.guild)

    if 'watch?' not in url and 'https://www.youtube.com' in url:
        idvideo = url.split('/')[-1]
        print(idvideo)
        url = f'https://www.youtube.com/watch?v={idvideo}'

    voice_channel = server.voice_client
    if vc and vc.is_connected(): await ctx.send('Обрабатываю запрос ... ... ..')
    else:
        await ctx.send('Подождите, ДОРАДУРА!?')
        await ctx.message.author.voice.channel.connect()
    async with ctx.typing():
        print('\n-'*3,url,'\n-'*3)
        
        music_name = fs.find_video(url)
        # try:
        filename = fs.get_audio(music_name).replace(' .mp3', '#.mp3')

        # filename = 'C:/Users/Дима/Documents/VSCode/Мелкопроекты/DS_music_bot/Рей - Мимо Поста ГИБДД.mp3'
        print('\n-'*3,filename,'\n-'*3)
        # await 

        # await ctx.send(filename.split('/')[-1].split('.')[0]+'  '+(music_name))
        await ctx.send(music_name[0].split('.mp3')[0] + '   ' + music_name[1])
        server.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))

        # except:

        #     await ctx.send("Да пошел ты!")
        #     with open('Баги.txt', 'a', encoding='utf-8') as f:
        #         f.write(str(music_name)[1:-1].replace("'", '')+'\n')

            

    # except:
    #     await ctx.send("Баг произошел")
    #     # pass
    #     # fs.get_audio(url)
 


    # return await bot.say("I am not connected to any voice channel on this server!")
bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена
