import telebot,colorama
from telebot import types
from colorama import Fore, Back, Style
from datetime import datetime
from pytz import timezone
from time import sleep
from threading import Thread
from subprocess import Popen
from fake_useragent import UserAgent
from os import system
import math as A, time as U, os as V, sys as W, json as C
import random as R, string as S, json as C, requests as T, re

# Variables
Q = 'utf-8'
P = False
O = 'https://bard.google.com/'
N = print
M = True
B = Exception
L = 'content'
K = 'A Ai girl'
J = 'choice_id'
I = 'SNlM0e'
H = ''
G = None
F = '_reqid'
E = 'response_id'
D = 'conversation_id'
##cookies and api


V = V.getenv('__Secure-1PSID') #bard cookies
W = V.getenv('__Secure-1PSIDTS') #bard cookies
api = V.getenv('api') #tg bot api


# banner
print(Fore.RED + '''
   ___   ___  ____   __        
  / _ | / _ \/  _/__/ /__ _  __
 / __ |/ // // // _  / -_) |/ /
/_/ |_/____/___/\_,_/\__/|___/ 
@ad1zxt
                               
''')

####
class color:
  def red(*args):
    return print("\033[0;31m" + ' '.join(args) + '\033[0m')
  def cyan(*args):
    return print("\033[0;36m" + ' '.join(args) + '\033[0m')
#bardbot
class BardBot:
  __slots__ = [
      'headers', F, I, D, E, J, 'proxy', 'secure_1psidts', 'secure_1psid',
      'session', 'timeout'
  ]
  def __init__(A, secure_1psid, secure_1psidts, proxy=G, timeout=20):
    D = proxy
    C = secure_1psid
    B = secure_1psidts
    E = {
        'Host': 'bard.google.com',
        'X-Same-Domain': '1',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'https://bard.google.com',
        'Referer': O
    }
    A._reqid = int(H.join(R.choices(S.digits, k=4)))
    A.proxy = D
    A.conversation_id = H
    A.response_id = H
    A.choice_id = H
    A.secure_1psid = C
    A.secure_1psidts = B
    A.session = T.session()
    A.session.headers = E
    A.session.proxies = D
    A.session.cookies.set('__Secure-1PSID', C)
    if B: A.session.cookies.set('__Secure-1PSIDTS', B)
    A.timeout = timeout

  def __m0e(A):
    if not (A.secure_1psid and A.secure_1psidts) or A.secure_1psid[-1] != '.':
      raise B('cookieError: Invalid cookies provided')
    C = A.session.get(O, timeout=10, allow_redirects=M)
    if C.status_code != 200:
      raise B(f"Invalid response: {C.status_code}")
    D = re.search('SNlM0e\\":\\"(.*?)\\"', C.text)
    if not D:
      raise B(
          'cookieError: Get cookies from: bard.google.com (Must logged In)')
    return D.group(1)

  def ask(A, message):
    N = 'choices'
    O = {
        'bl': 'boq_assistant-bard-web-server_20230713.13_p0',
        F: str(A._reqid),
        'rt': 'c'
    }
    P = [[message], G, [A.conversation_id, A.response_id, A.choice_id]]
    Q = {'f.req': C.dumps([G, C.dumps(P)]), 'at': A.__m0e()}
    J = A.session.post(
        'https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate',
        params=O,
        data=Q,
        timeout=A.timeout)
    K = C.loads(J.content.splitlines()[3])[0][2]
    if not K: return {L: f"Unknown error: {J.text}."}
    B = C.loads(K)
    M = []
    if len(B) >= 3:
      if len(B[4][0]) >= 4:
        if B[4][0][4]:
          for R in B[4][0][4]:
            M.append(R[0][0][0])
    I = {
        L: B[4][0][1][0],
        D: B[1][0],
        E: B[1][1],
        'factualityQueries': B[3],
        'textQuery': B[2][0] if B[2] is not G else H,
        N: [{
            'id': A[0],
            L: A[1]
        } for A in B[4]],
        'images': M
    }
    A.conversation_id = I[D]
    A.response_id = I[E]
    A.choice_id = I[N][0]['id']
    A._reqid += 100000
    return I
#######
def chatgpt(chat):
    try:
        response = T.get('https://chatgpt.ai/')
        matches = re.findall(
            r'data-nonce="(.*)"\n     data-post-id="(.*)"\n     data-url="(.*)"\n     data-bot-id="(.*)"\n     data-width',
            response.text)
        if not matches:
            return "Error: No matches found in response."

        nonce, post_id, _, bot_id = matches[0]

        headers = {
            'authority': 'chatgpt.ai',
            'origin': 'https://chatgpt.ai',
            'pragma': 'no-cache',
            'referer': 'https://chatgpt.ai/gpt-4/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }
        data = {
            '_wpnonce': nonce,
            'post_id': post_id,
            'url': 'https://chatgpt.ai/gpt-4',
            'action': 'wpaicg_chat_shortcode_message',
            'message': chat,
            'bot_id': bot_id
        }

        response = T.post('https://chatgpt.ai/wp-admin/admin-ajax.php',
                            headers=headers,
                            data=data)

        return response.json()['data']
    except Exception as e:
        return f"Error: {str(e)}"


bot = telebot.TeleBot(api)
bard = BardBot(V, W)
#start
@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.send_message(
      message.chat.id,
      f'🎀 Hi {message.chat.username}, I am chatbot! I can answer your questions.\n☎️ YourId: {message.chat.id}\n\n/help - open menu'
)
#help
@bot.message_handler(commands=['help'])
def help_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    btn_start = types.KeyboardButton('/start')
    btn_stop = types.KeyboardButton('/stop')
    btn_resume = types.KeyboardButton('/resume')
    btn_help = types.KeyboardButton('/help')
    markup.add(btn_start, btn_stop, btn_resume, btn_help)

    response = "Here are some commands you can use:\n\n"
    response += "🎀 /start - Start the bot\n"
    response += "🧹 /stop - Pause the bot\n"
    response += "✅ /resume - Resume the bot\n"
    response += "💌 /help - Show this help menu\n"
    response += "☎️ /about - About me\n"
    response += "🌹/ask - Ask me anything with gpt\n"

    bot.send_message(message.chat.id, response, reply_markup=markup)
##about
@bot.message_handler(commands=['about'])
def send_welcome(message):
  about = f"""
🙏 hello {message.chat.username}
🎀 I am BardBot! I can answer your any questions.
🎀 Type /stop to stop me.
🎀 YourId: {message.chat.id}
----------------------------
😋 My Developer Is: @ad1zxt
🐍 written in python
    """
  bot.send_message(message.chat.id, about)
#stop
bot_paused = False
@bot.message_handler(commands=['stop'])
def stop(message):
    global bot_paused
    bot_paused = True
    bot.reply_to(message, '⚠️ Bot paused. Use /resume to resume.')
#resume
@bot.message_handler(commands=['resume'])
def start(message):
    global bot_paused
    bot_paused = False
    bot.reply_to(message, '🎀 Bot resumed.')
##gpt
@bot.message_handler(commands=['ask'])
def handle_ask_command(message):
    try:
        query = message.text.replace('/ask', '').strip()
        response = chatgpt(query)
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

#bard bot
@bot.message_handler(func=lambda message: not bot_paused, content_types=['text'])

def handle_all_messages(message):
    user_input = message.text

    if not user_input.isdigit():
        try:
            response = bard.ask(user_input)
            bot.send_message(message.chat.id, response[L])
        except Exception as e:
            bot.send_message(message.chat.id, str(e))
    else:
        bot.send_message(message.chat.id, "Please send a text message.")
#run
try:
    bot.polling()
except KeyboardInterrupt:
        print("Bot stopped.")
        bot.stop_polling(non_stop=True)
