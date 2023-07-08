from telegram import Update
from telegram.ext import MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, filters, StringRegexHandler, StringCommandHandler, BaseHandler
from RegexpCommandHandler import RegexpCommandHandler

from help import help_message
from option import options

import re

import os
import openai



async def inference(update: Update, context):
    user_text = update.message.text
    user_id = update.effective_user.name
    

    if user_id not in availableUsers:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="사용가능 유저 목록에 없습니다. 봇 관리자에게 문의하세요.")
        return
    try:
        option.addMessage(role='user', message=user_text)
        
        response = openai.ChatCompletion.create(
            model=option.options['model'],
            messages=option.options["messages"]
        )

        answer = response['choices'][0]['message']['content']

        option.addMessage(role='assistant', message=answer)

        await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=e)
    

async def reset(update: Update, context, *other_args):
    ss = update.message.text.split('_', maxsplit=1)
    ss = ss[1].split(' ', maxsplit=1)
    if(ss[0] == 'messages'):
        option.resetOption('messages')
        await context.bot.send_message(chat_id=update.effective_chat.id, text="messages가 초기화 되었습니다.")
    elif(ss[0] == 'model'):
        option.resetOption('model')
        await context.bot.send_message(chat_id=update.effective_chat.id, text="사용 모델이 초기화 되었습니다.")
    elif(ss[0] == 'all'):
        option.resetOptionAll()
        await context.bot.send_message(chat_id=update.effective_chat.id, text="모든 옵션이 초기화 되었습니다.")

async def get(update: Update, context, *other_args):
    ss = update.message.text.split('_', maxsplit=1)
    ss = ss[1].split(' ', maxsplit=1)

    if(ss[0] == 'model'):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=option.options["model"])
    elif(ss[0] == 'modellist'):
        modelList = openai.Model.list()
        modelLisStr = ''

        for model in modelList['data']:
            modelLisStr += str(model['id']) + "\n"

        await context.bot.send_message(chat_id=update.effective_chat.id, text=modelLisStr)
    elif(ss[0] == 'messages'):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=option.options["messages"])
    elif(ss[0] == 'temperature'):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="명령어 준비중")

async def set(update: Update, context, *other_args):
    ss = update.message.text.split('_', maxsplit=1)
    ss = ss[1].split(' ', maxsplit=1)

    if(ss[0] == 'model'):
        #await context.bot.send_message(chat_id=update.effective_chat.id, text="비활성화된 옵션입니다. 업데이트를 기다리던지 말던지")
        #return
        preModel = option.options["model"]
        option.setModel(ss[1])
        curModel = option.options["model"]
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                       text="사용할 모델이 " + preModel + " 모델에서 " + curModel + "모델로 변경 되었습니다.")
    if(ss[0] == 'assistant'):
        option.addMessage(role='assistant', message=ss[1])
        await context.bot.send_message(chat_id=update.effective_chat.id, text="assistant가 초기화 되었습니다.")

if __name__ == "__main__":

    availableUsers = [
        '@a1009mys',
        '@Zaevis1'
    ]

    option = options()

    openai.api_key = option.my_openAI_api_key

    app = ApplicationBuilder().token(option.my_token).build()



    app.add_handler(CommandHandler("help", help_message))


    app.add_handler(RegexpCommandHandler(r'get_.+', get, separator='_'))
    app.add_handler(RegexpCommandHandler(r'set_.+', set, separator='_'))
    app.add_handler(RegexpCommandHandler(r'reset_.+', reset, separator='_'))

    # app.add_handler(RegexpCommandHandler(r'inference.+', reset, separator='ce'))

    app.add_handler(MessageHandler(filters = filters.TEXT & (~filters.COMMAND), callback=inference, block=True))



    app.run_polling()