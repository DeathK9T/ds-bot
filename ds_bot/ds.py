import discord
from discord.ext import commands
import os
import youtube_dl
from discord.utils import get
from Cybernator import Paginator

PREFIX = '.'

statement = True
start_role = ''

games = ['дота','доту','dota','doty','кс','кс го','кс:го','ксго','контру','контра','cs',
				'cs go','cs:go','csgo','counter-strike','counter strike','apex','арех']

asking_words = ['go','го','будете','будешь','пойдете','пойдешь']

games_icons_urls = {'dota':'https://i.pinimg.com/originals/c1/ec/da/c1ecda477bc92b6ecfc533b64d4a0337.png',
					'cs:go':'https://www.freeiconspng.com/uploads/csgo-icon-12.png',
					'apex':'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/563aee18-d547-4bdc-bdbf-23056bc595bb/dczo00v-fc29c0d0-4cdd-4ee9-b95d-64258677d53e.png'}

client = commands.Bot(command_prefix = PREFIX)
client.remove_command('help')

token = open('token.txt','r').readline()

#Bot_connected
@client.event
async def on_connect():
	mute_text = None
	mute_voice = None
	for guild in client.guilds:
		for role in guild.roles:
			if str(role) == 'Text muted':
				mute_text = role
			elif str(role) == 'Voice muted':
				mute_voice = role
		if not mute_text:
			perms = discord.Permissions(
				create_instant_invite = True,
				kick_members = False,
				ban_members = False,
				administrator = False,
				manage_channels = False,
				manage_guild = False,
				add_reactions = False,
				view_audit_log = False,
				priority_speaker = False,
				stream = True,
				read_messages = True,
				view_channel = True,
				send_messages = False,
				send_tts_messages = False,
				manage_messages = False,
				embed_links = False,
				attach_files = False,
				read_message_history = True,
				mention_everyone = False,
				external_emojis = False,
				use_external_emojis = False,
				#view_guild_insights = False,
				connect = True,
				speak = True,
				mute_members = False,
				deafen_members = False,
				move_members = False,
				use_voice_activation = True,
				change_nickname = True,
				manage_nicknames = False,
				manage_roles = False,
				manage_permissions = False,
				manage_webhooks = False,
				manage_emojis = False
			)
			await guild.create_role(
				name = 'Text muted',
				permissions = perms,
				colour = discord.Colour.purple()
			)
		if not mute_voice:
			perms = discord.Permissions(
				create_instant_invite = True,
				kick_members = False,
				ban_members = False,
				administrator = False,
				manage_channels = False,
				manage_guild = False,
				add_reactions = True,
				view_audit_log = False,
				priority_speaker = False,
				stream = True,
				read_messages = True,
				view_channel = True,
				send_messages = True,
				send_tts_messages = True,
				manage_messages = False,
				embed_links = True,
				attach_files = True,
				read_message_history = True,
				mention_everyone = True,
				external_emojis = True,
				use_external_emojis = True,
				#view_guild_insights = False,
				connect = True,
				speak = False,
				mute_members = False,
				deafen_members = False,
				move_members = False,
				use_voice_activation = False,
				change_nickname = True,
				manage_nicknames = False,
				manage_roles = False,
				manage_permissions = False,
				manage_webhooks = False,
				manage_emojis = False
			)
			await guild.create_role(
				name = 'Voice muted',
				permissions = perms,
				colour = discord.Colour.dark_purple()
			)
	print('Bot have logged in as {0.user}'.format(client))
	await client.change_presence(status = discord.Status.online, activity = discord.Game('.help'))

@client.event
async def on_ready():
	'''mute_text = None
	mute_voice = None
	for guild in client.guilds:
		for role in guild.roles:
			if str(role) == 'Text muted':
				mute_text = role
			elif str(role) == 'Voice muted':
				mute_voice = role
		if not mute_text:
			perms = discord.Permissions(
				create_instant_invite = True,
				kick_members = False,
				ban_members = False,
				administrator = False,
				manage_channels = False,
				manage_guild = False,
				add_reactions = False,
				view_audit_log = False,
				priority_speaker = False,
				stream = True,
				read_messages = True,
				view_channel = True,
				send_messages = False,
				send_tts_messages = False,
				manage_messages = False,
				embed_links = False,
				attach_files = False,
				read_message_history = True,
				mention_everyone = False,
				external_emojis = False,
				use_external_emojis = False,
				#view_guild_insights = False,
				connect = True,
				speak = True,
				mute_members = False,
				deafen_members = False,
				move_members = False,
				use_voice_activation = True,
				change_nickname = True,
				manage_nicknames = False,
				manage_roles = False,
				manage_permissions = False,
				manage_webhooks = False,
				manage_emojis = False
			)
			await guild.create_role(
				name = 'Text muted',
				permissions = perms,
				colour = discord.Colour.purple()
			)
		if not mute_voice:
			perms = discord.Permissions(
				create_instant_invite = True,
				kick_members = False,
				ban_members = False,
				administrator = False,
				manage_channels = False,
				manage_guild = False,
				add_reactions = True,
				view_audit_log = False,
				priority_speaker = False,
				stream = True,
				read_messages = True,
				view_channel = True,
				send_messages = True,
				send_tts_messages = True,
				manage_messages = False,
				embed_links = True,
				attach_files = True,
				read_message_history = True,
				mention_everyone = True,
				external_emojis = True,
				use_external_emojis = True,
				#view_guild_insights = False,
				connect = True,
				speak = False,
				mute_members = False,
				deafen_members = False,
				move_members = False,
				use_voice_activation = False,
				change_nickname = True,
				manage_nicknames = False,
				manage_roles = False,
				manage_permissions = False,
				manage_webhooks = False,
				manage_emojis = False
			)
			await guild.create_role(
				name = 'Voice muted',
				permissions = perms,
				colour = discord.Colour.dark_purple()
			)
	print('Bot have logged in as {0.user}'.format(client))
	await client.change_presence(status = discord.Status.online, activity = discord.Game('.help'))'''

#Bot_disconnected
@client.event
async def on_disconnect():
	try:
		if voice.is_playing() or voice.is_paused():
			voice.stop()
		if voice.is_connected():
			await voice.disconnect()
	except NameError:
		pass

#Chat_searching_teamates
user_names = []
searching = False
unknown_game = False
game_name = None
chnl = None
@client.event
async def on_message(message):
	global game_name, user_names, searching, chnl, unknown_game
	bot_name = client.user
	await client.process_commands(message)
	msg = message.content.lower()
	msg = msg.split()
	if str(message.author) != str(bot_name):
		if searching:
			if 'забей' in msg:
				searching = False
				game_name = None
				chnl = None
				user_names.clear()
		if not searching:
			#Searching asking words
			for word in asking_words:
				if word in msg:
					searching = True
					for game in games:
						if game in msg:
							game_name = game
							break
					for guild in client.guilds:
						for member in guild.members:
							if str(member.mention) in msg:
								user_names.append(member)
						break
					try:
						if chnl == None:
							chnl = message.author.voice.channel
					except AttributeError:
						chnl = None
			if not searching:
				return
		#Searching game
		if not game_name:
			for game in games:
				if game in msg:
					game_name = game
					unknown_game = False
		#Searching names
		if len(user_names) == 0:
			for guild in client.guilds:
				for member in guild.members:
					if '<@!' + str(member.id)+'>' in msg:
						if not (member in user_names):
							user_names.append(member)
		#Searching channel
		if not chnl:
			for guild in client.guilds:
				for channel in guild.channels:
					if str(channel).lower() in msg:
						chnl = channel
		if unknown_game:
			game_name = ''
			for name in msg:
				game_name += name + ' '
			unknown_game = False
		if game_name == None and len(user_names) == 0:
			await message.channel.send('Во что?')
			unknown_game = True
		elif game_name == None and len(user_names) > 0:
			await message.channel.send('Во что?')
			unknown_game = True
		elif game_name and len(user_names) == 0:
			await message.channel.send('Кто?')
		elif not chnl:
			await message.channel.send('В какой канал заходить?')
		elif game_name and len(user_names) > 0 and chnl:
			invite = await chnl.create_invite(max_age = 1800, max_uses = len(user_names))
			embed = discord.Embed(
				title = f'Го {game_name}?',
				description = 'Click "Join Voice"',
				colour = discord.Colour.teal()
			)
			embed.set_author(name = f'{message.author.name} приглашает:', icon_url = message.author.avatar_url)
			for member in user_names:
				await member.send(embed = embed)
				await member.send(invite)
			searching = False
			game_name = None
			chnl = None
			user_names.clear()

#Error
@client.event
async def on_command_error(ctx, error):
	#print(error)
	if isinstance(error, commands.CommandNotFound):
		await ctx.send('Неизвестная команда. Попробуйте написать ".help", чтобы проверить.')

#Join_member_add_role
@client.event
async def on_member_join(member):
	for guild in client.guilds:
		for role in guild.roles:
			if str(role) == str(start_role):
				await member.add_roles(role)

#Help
@client.command()
async def help(ctx):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	emb_evr = discord.Embed(
		title = 'Команды бота для всех.',
		colour = discord.Colour.blue()
	)
	#everyone_commands
	emb_evr.add_field(
		name = '{}hello [участник с упоминанием]'.format(PREFIX),
		value = 'Приветсвие.',
		inline = False
	)
	emb_evr.add_field(
		name = '{}join'.format(PREFIX),
		value = 'Присоединить бота к голосовому каналу.',
		inline = False
	)
	emb_evr.add_field(
		name = '{}move_to [название канала]'.format(PREFIX),
		value = 'Переместить бота в указаный голосовой канал.',
		inline = False
	)
	emb_evr.add_field(
		name = '{}leave'.format(PREFIX),
		value = 'Отсоединить бота от голосового канала.',
		inline = False
	)
	emb_evr.add_field(
		name = '{}play_test [url]'.format(PREFIX),
		value = 'Проигрывание музыки ботом с очередью(WIP).',
		inline = False
	)
	emb_evr.add_field(
		name = '{}next'.format(PREFIX),
		value = 'Проиграть следующую музыку в очереди(WIP).',
		inline = False
	)
	emb_evr.add_field(
		name = '{}play [url]'.format(PREFIX),
		value = 'Проигрывание музыки ботом.',
		inline = False
	)
	emb_evr.add_field(
		name = '{}pause'.format(PREFIX),
		value = 'Поставить на паузу проигрывание музыки.',
		inline = False
	)
	emb_evr.add_field(
		name = '{}resume'.format(PREFIX),
		value = 'Возобновить проигрывание музыки.',
		inline = False
	)
	emb_evr.add_field(
		name = '{}stop'.format(PREFIX),
		value = 'Остановить проигрывание музыки.',
		inline = False
	)
	emb_evr.add_field(
		name = '{}dota [название канала(если не в нем)] [участники с упоминанием]'.format(PREFIX),
		value = 'Предложить поиграть в доту.',
		inline = False
	)
	emb_evr.add_field(
		name = '{}cs [название канала(если не в нем)] [участники с упоминанием]'.format(PREFIX),
		value = 'Предложить поиграть в cs.',
		inline = False
	)
	emb_evr.add_field(
		name = '{}apex [название канала(если не в нем)] [участники с упоминанием]'.format(PREFIX),
		value = 'Предложить поиграть в apex.',
		inline = False
	)
	emb_evr.add_field(
		name = '{}game_invite [название игры] [название канала(если не в нем)] [участники с упоминанием]'.format(PREFIX),
		value = 'Предложить поиграть в указаную игру.',
		inline = False
	)
	if ctx.author.guild_permissions.administrator:
		emb_admn = discord.Embed(
			title = 'Команды бота для администратора.',
			colour = discord.Colour.gold()
		)
		#admins_commands
		emb_admn.add_field(
			name = '{}default_role [Название роли]'.format(PREFIX),
			value = 'Указать роль по умолчанию.',
			inline = False
		)
		emb_admn.add_field(
			name = '{}clear_commands [True/False]'.format(PREFIX),
			value = 'Убирать отправленные команды.',
			inline = False
		)
		emb_admn.add_field(
			name = '{}clear [количество строк]'.format(PREFIX),
			value = 'Очистка чата.',
			inline = False
		)
		emb_admn.add_field(
			name = '{}kick [участник с упоминанием]'.format(PREFIX),
			value = 'Кик участника.',
			inline = False
		)
		emb_admn.add_field(
			name = '{}ban [участник с упоминанием]'.format(PREFIX),
			value = 'Бан участника.',
			inline = False
		)
		emb_admn.add_field(
			name = '{}unban [участник с упоминанием]'.format(PREFIX),
			value = 'Разбан участника.',
			inline = False
		)
		emb_admn.add_field(
			name = '{}text_mute [участник с упоминанием]'.format(PREFIX),
			value = 'Ограничение участника в отправке сообщений.',
			inline = False
		)
		emb_admn.add_field(
			name = '{}voice_mute [участник с упоминанием]'.format(PREFIX),
			value = 'Ограничение участника в голосовом общении.',
			inline = False
		)
		emb_admn.add_field(
			name = '{}text_unmute [участник с упоминанием]'.format(PREFIX),
			value = 'Разрешение участнику отправлять сообщения.',
			inline = False
		)
		emb_admn.add_field(
			name = '{}voice_unmute [участник с упоминанием]'.format(PREFIX),
			value = 'Разрешение участнику общасться.',
			inline = False
		)
		emb_admn.add_field(
			name = '{}move [название канала(если не в нем)] [участник(и) с упоминанием]'.format(PREFIX),
			value = 'Переместить участника(ов) в ваш текущий канал или в указаный.',
			inline = False
		)
		embeds = [emb_admn, emb_evr]
		message = await ctx.send(embed = emb_admn)
		page = Paginator(client, message, only = ctx.author, use_more = False, embeds = embeds)
		await page.start()
	else:
		await ctx.send(embed = emb_evr)

@client.command()
@commands.has_permissions(administrator = True)
async def clear_commands(ctx, state: bool):
	global statement
	statement = state
	if statement:
		await ctx.channel.purge(limit = 1)

#Clear_command_error
@clear_commands.error
async def clear_commands_error(ctx, error):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('В доступе отказано.')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Нужно указать значение.')

#Default_role
@client.command()
@commands.has_permissions(administrator = True)
async def default_role(ctx, role):
	global start_role
	start_role = role

#Default_role_error
@clear_commands.error
async def default_role_error(ctx, error):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('В доступе отказано.')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Нужно указать название роли.')

#Hello
@client.command()
async def hello(ctx, member: discord.Member):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	await ctx.send(f'Hello {member.mention}.')

#Hello_error
@hello.error
async def hello_error(ctx, error):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Нужно указать участника с упоминанием.')

#Clear
@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, amount: int):
	await ctx.channel.purge(limit = amount+1)

#Clear_error
@clear.error
async def clear_error(ctx, error):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('В доступе отказано.')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Нужно указать количество строк.')

#Kick
@client.command()
@commands.has_permissions(administrator = True)
async def kick(ctx, member: discord.Member, *, reason = None):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	await member.kick(reason = reason)
	await ctx.send(f'{member.mention} кикнут.')

#Kick_error
@kick.error
async def kick_error(ctx, error):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('В доступе отказано.')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Нужно указать участника с упоминанием.')

#Ban
@client.command()
@commands.has_permissions(administrator = True)
async def ban(ctx, member: discord.Member, *, reason = None):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	await member.ban(reason = reason)
	await ctx.send(f'{member.mention} забанен.')

#Ban_error
@ban.error
async def ban_error(ctx, error):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('В доступе отказано.')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Нужно указать участника с упоминанием.')

#Unban
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	banned_users = await ctx.guild.bans()
	for ban_entry in banned_users:
		user = ban_entry.user
		if str(user) == str(member):
			await ctx.guild.unban(user)
			await ctx.send(f'{user.mention} разбанен.')
			return

#Unban_error
@unban.error
async def unban_error(ctx, error):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('В доступе отказано.')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Нужно указать участника с упоминанием.')

#Text_mute
@client.command()
@commands.has_permissions(administrator = True)
async def text_mute(ctx, member: discord.Member):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Text muted')
	await member.add_roles(mute_role)
	await ctx.send(f'{member.mention} не может печатать.')

#Text_mute_error
@text_mute.error
async def text_mute_error(ctx, error):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('В доступе отказано.')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Нужно указать участника с упоминанием.')

#Voice_mute
@client.command()
@commands.has_permissions(administrator = True)
async def voice_mute(ctx, member: discord.Member):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Voice muted')
	await member.add_roles(mute_role)
	await ctx.send(f'{member.mention} приглушен.')

#Voice_mute_error
@voice_mute.error
async def voice_mute_error(ctx, error):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('В доступе отказано.')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Нужно указать участника с упоминанием.')

#Text_unmute
@client.command()
@commands.has_permissions(administrator = True)
async def text_unmute(ctx, member: discord.Member):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Text muted')
	await member.remove_roles(mute_role)
	await ctx.send(f'{member.mention} снова может печатать.')

#Text_unmute_error
@text_unmute.error
async def text_unmute_error(ctx, error):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('В доступе отказано.')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Нужно указать участника с упоминанием.')

#Voice_unmute
@client.command()
@commands.has_permissions(administrator = True)
async def voice_unmute(ctx, member: discord.Member):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Voice muted')
	await member.remove_roles(mute_role)
	await ctx.send(f'{member.mention} снова может разговаривать.')

#Voice_unmute_error
@voice_unmute.error
async def voice_unmute_error(ctx, error):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('В доступе отказано.')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Нужно указать участника с упоминанием.')

#Move
@client.command()
@commands.has_permissions(administrator = True)
async def move(ctx, *args):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	channel = None
	users = []
	if len(args) == 0:
		await ctx.send('Укажите название канала (если вы не в нем) и участников с упоминанием.')
		return
	elif not '@' in args[0]:
		for chnnl in client.get_all_channels():
			if str(args[0]) == str(chnnl):
				channel = chnnl
				break
		if channel == None:
			await ctx.send('Укажите существующее название канала.')
			return
	try:
		if channel == None:
			channel = ctx.message.author.voice.channel
	except AttributeError:
		await ctx.send('Войдите в голосовой канал или укажите его название.')
		return
	for arg in args:
		for guild in client.guilds:
			for member in guild.members:
				if str(member.id) in arg:
					users.append(member)
	if len(users) == 0:
		await ctx.send('Укажите участника(ов) с упоминанием.')
		return
	for user in users:
		try:
			await user.move_to(channel)
		except:
			await ctx.send('Участника нет в голосовых каналах.')

#Join
@client.command()
async def join(ctx):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	global voice
	try:
		channel = ctx.message.author.voice.channel
		if voice.is_connected() and voice.channel == channel:
			await ctx.send(f'Бот уже в {voice.channel}.')
		elif voice.is_connected():
			await ctx.send('Попробуйте использовать ".move_to".')
		else:
			await ctx.send(f'Подключен к {channel}.')
			voice = await channel.connect()
	except NameError:
		await ctx.send(f'Подключен к {channel}.')
		voice = await channel.connect()
	except AttributeError:
		await ctx.send('Пожалуйста, подсоединитесь к голосовому каналу.')

#Move_to
@client.command()
async def move_to(ctx, chnnl):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	try:
		if str(voice.channel) == str(chnnl):
			await ctx.send(f'Бот уже в {voice.channel} или имя канала указано неправильно.')
		else:
			for channel in client.get_all_channels():
				if str(channel.name) == str(chnnl):
					await voice.move_to(channel)
					await ctx.send(f'Подключен к {channel}.')
	except NameError:
		await ctx.send('Бот никогда не подсоединялся.')

#Leave
@client.command()
async def leave(ctx):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	try:
		if voice.is_connected():
			await voice.disconnect()
			await ctx.send(f'Бот покинул {voice.channel}.')
		else:
			await ctx.send(f'Бот уже покинул {voice.channel}.')
	except NameError:
		await ctx.send('Бот никогда не подсоединялся.')

#Play_song_WIP
songs = []
def play_song():
	if voice.is_playing() or voice.is_paused():
		pass
	elif not (voice.is_playing() and voice.is_paused()):
		voice.play(discord.FFmpegPCMAudio(songs[0]), after = song_end)
		voice.source = discord.PCMVolumeTransformer(voice.source)
		voice.source.volume = 1

#Stop_song_WIP
def stop_song():
	if voice.is_playing():
		voice.stop()
	else:
		if voice.is_paused():
			voice.stop()
		else:
			pass

#Song_end_WIP
def song_end(error):
	global name
	print(f'[log]{name} is end.')
	for file in os.listdir('./'):
		if str(file) == str(songs[0]):
			os.remove(songs.pop(0))
			break
		else:
			continue
	if len(songs) > 0:
		print('111111111111111111111111111111')
		for i in range(len(songs)):
			os.rename(songs[i],'song{}.mp3'.format(i))
		#WIP#play_song()

#Play_test_WIP
@client.command()
async def play_test(ctx, url):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	await ctx.send('This is unstable function.[WIP]')
	return
	try:
		if voice.is_connected():
			ydl_opts = {
				'format':'bestaudio/best',
				'postprocessors':[{
					'key':'FFmpegExtractAudio',
					'preferredcodec':'mp3',
					'preferredquality':'192'
				}]
			}
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				print('[log]Downloading music...')
				ydl.download([url])
			songs.append('song{}.mp3'.format(len(songs)))
			global name
			for file in os.listdir('./'):
				if file.endswith('.mp3') and not file in songs:
					name = file
					print(f'[log]Renaming file {file}...')
					os.rename(file, songs[len(songs)-1])
			if voice.is_playing() or voice.is_paused():
				song_name = name.rsplit('-', 2)
				await ctx.send(f'{(len(songs))}) {song_name} added to queue.')
			elif not (voice.is_paused() and voice.is_playing()):
				voice.play(discord.FFmpegPCMAudio(songs[0]), after = song_end)
				voice.source = discord.PCMVolumeTransformer(voice.source)
				voice.source.volume = 1
				song_name = name.rsplit('-', 2)
				await ctx.send(f'Now playing {song_name[0]}.')
		else:
			await ctx.send('Bot isn\'t connected.')
	except NameError:
		await ctx.send('Bot was never joined.')

#Next_WIP
@client.command()
async def next(ctx):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	await ctx.send('This is unstable function.[WIP]')
	return
	try:
		if voice.is_connected():
			stop_song()
		else:
			await ctx.send('Bot isn\'t connected.')
	except NameError:
		await ctx.send('Bot was never joined.')

#Play
@client.command()
async def play(ctx, url):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	try:
		if voice.is_connected():
			await ctx.send('Пожалуйста, подождите.')
		else:
			await ctx.send('Бот не подключен.')
			return
	except NameError:
		await ctx.send('Бот никогда не подсоединялся.')
		return
	song_there = os.path.exists('song.mp3')
	try:
		if song_there:
			os.remove('song.mp3')
	except PermissionError:
		print('[log]File not found.')
	ydl_opts = {
		'format':'bestaudio/best',
		'postprocessors':[{
			'key':'FFmpegExtractAudio',
			'preferredcodec':'mp3',
			'preferredquality':'192'
		}]
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		print('[log]Downloading music...')
		ydl.download([url])
	for file in os.listdir('./'):
		if file.endswith('.mp3'):
			name = file
			print(f'[log]Renaming file: {file}...')
			os.rename(file, 'song.mp3')
	voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[log]{name} is end.'))
	voice.source = discord.PCMVolumeTransformer(voice.source)
	voice.source.volume = 0.6
	song_name = name.rsplit('-', 2)
	await ctx.send(f'Сейчас проигрывается {song_name[0]}.')

#Pause
@client.command()
async def pause(ctx):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	try:
		if voice.is_playing():
			voice.pause()
		else:
			if voice.is_paused():
				await ctx.send('Музыка уже на паузе.')
			else:
				await ctx.send('Музыка не указана.')
	except NameError:
		await ctx.send('Бот никогда не подсоединялся.')
		return

#Resume
@client.command()
async def resume(ctx):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	try:
		if voice.is_paused():
			voice.resume()
		else:
			if voice.is_playing():
				await ctx.send('Музыка уже проигрывается.')
			else:
				await ctx.send('Музыка не указана.')
	except NameError:
		await ctx.send('Бот никогда не подсоединялся.')
		return

#Stop
@client.command()
async def stop(ctx):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	try:
		if voice.is_playing():
			voice.stop()
			await ctx.send('Музыка остановлена.')
		else:
			if voice.is_paused():
				voice.stop()
				await ctx.send('Музыка была на паузе, а сейчас остановлена.')
			else:
				await ctx.send('Музыка уже остановлена или не указана.')
	except NameError:
		await ctx.send('Бот никогда не подсоединялся.')
		return

#Dota
@client.command()
async def dota(ctx, *args):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	channel = None
	users = []
	if len(args) == 0:
		await ctx.send('Укажите название канала (если вы не в нем) и участников с упоминанием.')
		return
	elif not '@' in args[0]:
		for chnnl in client.get_all_channels():
			if str(args[0]) == str(chnnl):
				channel = chnnl
				break
			else:
				continue
		if channel == None:
			await ctx.send('Укажите существующее название канала.')
			return
	try:
		if channel == None:
			channel = ctx.message.author.voice.channel
	except AttributeError:
		await ctx.send('Войдите в голосовой канал или укажите его название.')
		return
	for arg in args:
		if '@' in arg:
			users.append(arg)
	if len(users) == 0:
		await ctx.send('Укажите участника(ов) с упоминанием.')
		return
	invite = await channel.create_invite(max_age = 1800, max_uses = len(users))
	embed = discord.Embed(
		title = 'Пойдешь в доту?',
		description = 'Нажми на "Join Voice"',
		colour = discord.Colour.orange()
	)
	embed.set_author(name = f'{ctx.message.author.name} приглашает:', icon_url = ctx.message.author.avatar_url)
	embed.set_thumbnail(url = games_icons_urls['dota'])
	for guild in client.guilds:
		for member in guild.members:
			if str(member.id) in str(users):
				await member.send(embed = embed)
				await member.send(invite)

#Cs
@client.command()
async def cs(ctx, *args):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	channel = None
	users = []
	if len(args) == 0:
		await ctx.send('Укажите название канала (если вы не в нем) и участников с упоминанием.')
		return
	elif not '@' in args[0]:
		for chnnl in client.get_all_channels():
			if str(args[0]) == str(chnnl):
				channel = chnnl
				break
			else:
				continue
		if channel == None:
			await ctx.send('Укажите существующее название канала.')
			return
	try:
		if channel == None:
			channel = ctx.message.author.voice.channel
	except AttributeError:
		await ctx.send('Войдите в голосовой канал или укажите его название.')
		return
	for arg in args:
		if '@' in arg:
			users.append(arg)
	if len(users) == 0:
		await ctx.send('Укажите участника(ов) с упоминанием.')
		return
	invite = await channel.create_invite(max_age = 1800, max_uses = len(users))
	embed = discord.Embed(
		title = 'Пойдешь в cs?',
		description = 'Нажми на "Join Voice"',
		colour = discord.Colour.orange()
	)
	embed.set_author(name = f'{ctx.message.author.name} приглашает:', icon_url = ctx.message.author.avatar_url)
	embed.set_thumbnail(url = games_icons_urls['cs:go'])
	for guild in client.guilds:
		for member in guild.members:
			if str(member.id) in str(users):
				await member.send(embed = embed)
				await member.send(invite)

#Apex
@client.command()
async def apex(ctx, *args):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	channel = None
	users = []
	if len(args) == 0:
		await ctx.send('Укажите название канала (если вы не в нем) и участников с упоминанием.')
		return
	elif not '@' in args[0]:
		for chnnl in client.get_all_channels():
			if str(args[0]) == str(chnnl):
				channel = chnnl
				break
			else:
				continue
		if channel == None:
			await ctx.send('Укажите существующее название канала.')
			return
	try:
		if channel == None:
			channel = ctx.message.author.voice.channel
	except AttributeError:
		await ctx.send('Войдите в голосовой канал или укажите его название.')
		return
	for arg in args:
		if '@' in arg:
			users.append(arg)
	if len(users) == 0:
		await ctx.send('Укажите участника(ов) с упоминанием.')
		return
	invite = await channel.create_invite(max_age = 1800, max_uses = len(users))
	embed = discord.Embed(
		title = 'Пойдешь в apex?',
		description = 'Нажми на "Join Voice"',
		colour = discord.Colour.orange()
	)
	embed.set_author(name = f'{ctx.message.author.name} приглашает:', icon_url = ctx.message.author.avatar_url)
	embed.set_thumbnail(url = games_icons_urls['apex'])
	for guild in client.guilds:
		for member in guild.members:
			if str(member.id) in str(users):
				await member.send(embed = embed)
				await member.send(invite)

#Game_invite
@client.command()
async def game_invite(ctx, game = None, *args):
	global statement
	if statement:
		await ctx.channel.purge(limit = 1)
	if game == None:
		await ctx.send('Укажите название игры.')
		return
	channel = None
	users = []
	if len(args) == 0:
		await ctx.send('Укажите название канала (если вы не в нем) и участников с упоминанием.')
		return
	elif not '@' in args[0]:
		for chnnl in client.get_all_channels():
			if str(args[0]) == str(chnnl):
				channel = chnnl
				break
			else:
				continue
		if channel == None:
			await ctx.send('Укажите существующее название канала.')
			return
	try:
		if channel == None:
			channel = ctx.message.author.voice.channel
	except AttributeError:
		await ctx.send('Войдите в голосовой канал или укажите его название.')
		return
	for arg in args:
		if '@' in arg:
			users.append(arg)
	if len(users) == 0:
		await ctx.send('Укажите участника(ов) с упоминанием.')
		return
	invite = await channel.create_invite(max_age = 1800, max_uses = len(users))
	embed = discord.Embed(
		title = f'Пойдешь в {game}?',
		description = 'Нажми на "Join Voice"',
		colour = discord.Colour.teal()
	)
	embed.set_author(name = f'{ctx.message.author.name} приглашает:', icon_url = ctx.message.author.avatar_url)
	for guild in client.guilds:
		for member in guild.members:
			if str(member.id) in str(users):
				await member.send(embed = embed)
				await member.send(invite)

client.run(token)