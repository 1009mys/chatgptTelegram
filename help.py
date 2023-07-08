async def help_message(update, context):
    helpMassage = """
<도움말>

옵션 설명

model
 ㄴ AI 모델
messages
 ㄴ AI 모델에 inference할 input값이다.
temperature
 ㄴ What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
top_p
 ㄴ An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
We generally recommend altering top_p or temperature but not both.
n 
 ㄴ How many chat completion choices to generate for each input message.
stream
 ㄴ If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a data: [DONE] message. See the OpenAI Cookbook for example code.
stop
 ㄴ Up to 4 sequences where the API will stop generating further tokens.
max_tokens
 ㄴ The maximum number of tokens to generate in the chat completion. The total length of input tokens and generated tokens is limited by the model's context length.
presence_penalty
 ㄴ Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
frequency_penalty
 ㄴ Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

/help
 ㄴ 도움말을 출력합니다.

/get_modellist
 ㄴ 사용가능한 모델 목록을 출력합니다.

/inference <text>
 ㄴ <text> 내용을 messages에 추가하고 모델을 inference합니다. 명령어 없이 채팅 입력만으로도 사용 가능. 만들기 너무너무 귀찮아서 나중에 구현 예정임

다음 명령어는 현재 옵션을 출력합니다.
/get_model
/get_messages
/get_temperature

다음 명령어는 옵션을 설정합니다.
/set_model <모델 이름>
/set_assistant <설정할 assistant>
/reset_messages
/reset_model
/reset_all

"""
    await update.message.reply_text(helpMassage)