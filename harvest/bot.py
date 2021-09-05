import discord
from moduel import *
import data

bot = discord.Client()
call_word = [
    '!'
]

command_list = [
    '상점',
    '등록'
]

@bot.event
async def on_ready():
    print("===================================")
    print("|              START              |")
    print("===================================")

@bot.event
async def on_message(message):
    message_list = message.content.split(' ')
    if message.author == bot.user:
        return

    if Value_in_list(list = call_word, value = message_list[0][0]):
        command_part = message_list[0][1:]
        if Value_in_list(list = command_list, value = command_part):
            if len(message_list) == 1:
                if command_part == '등록':
                    pass
                if command_part == '상점':
                    embed = discord.Embed(title="상점", description = "\n", color=0xcfdd8e)
                    embed.add_field(name = "작은 작물", value = "명령어 : `!상점 작물`")
                    embed.add_field(name = "큰 작물", value = "명령어 : `!상점 나무`")
                    embed.add_field(name = "땅", value = "명령어 : `!상점 땅`")
                    await message.channel.send(embed=embed)

            if len(message_list) == 2:
                if command_part == '상점':
                    if message_list[1] == '작물':
                        embed = discord.Embed(title="작물 상점", description = "\n", color=0xcfdd8e)
                        embed.add_field(name = "감자", value = "판매 - 0G   구매 - 0G", inline=False)
                        embed.add_field(name = "당근", value = "판매 - 0G   구매 - 0G", inline=False)
                        embed.add_field(name = "밀", value = "판매 - 0G   구매 - 0G", inline=False)
                        embed.add_field(name = "쌀", value = "판매 - 0G   구매 - 0G", inline=False)
                        embed.add_field(name = "보리", value = "판매 - 0G   구매 - 0G", inline=False)
                        embed.add_field(name = "토마토", value = "판매 - 0G   구매 - 0G", inline=False)
                        embed.add_field(name = "산딸기", value = "판매 - 0G   구매 - 0G", inline=False)
                        embed.add_field(name = "블루베리", value = "판매 - 0G   구매 - 0G", inline=False)
                        await message.channel.send(embed=embed)
                    elif message_list[1] == '나무':
                        embed = discord.Embed(title="나무 상점", description = "\n", color=0xcfdd8e)
                        embed.add_field(name = "사과", value = "판매 - 0G   구매 - 0G", inline=False)
                        embed.add_field(name = "배", value = "판매 - 0G   구매 - 0G", inline=False)
                        embed.add_field(name = "포도", value = "판매 - 0G   구매 - 0G", inline=False)
                        embed.add_field(name = "복숭아", value = "판매 - 0G   구매 - 0G", inline=False)
                        await message.channel.send(embed=embed)

def run():
    bot.run(token)
run()
