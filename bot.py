import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_bot():
    TOKEN = 'MTA1NTk1NzM0Njk4NTE4OTUyOA.GI4dRf.-66bhksZGj5qrzUMQE32Rudo1WBiEU6I6OaNuk'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        print(discord.Intents.message_content in discord.Intents.default())
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        m_channel = str(message.channel)

        print('{} said: {} in {}'.format(username,user_message,m_channel))


        if user_message[0] == ".":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
