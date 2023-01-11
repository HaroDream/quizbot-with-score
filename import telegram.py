import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Define a dictionary of questions and answers
quiz = {
    'What is the capital of France?': 'Paris',
    'What is the largest planet in the Solar System?': 'Jupiter',
    'What is the smallest country in the world?': 'Vatican City',
}

# Store the scores of the users
scores = {}

def start_quiz(update, context):
    message = update.message
    chat_id = message.chat_id
    context.bot.send_message(chat_id=chat_id, text='Welcome to the Quiz! Type /answer followed by your answer to answer the question')
    scores[chat_id] = 0
    context.bot.send_message(chat_id=chat_id, text=list(quiz.keys())[0])

def check_answer(update, context):
    message = update.message
    chat_id = message.chat_id
    user_answer = message.text.split()[1]
    if user_answer.lower() == quiz[list(quiz.keys())[0]].lower():
        scores[chat_id] += 1
        context.bot.send_message(chat_id=chat_id, text='Correct!')
    else:
        context.bot.send_message(chat_id=chat_id, text='Incorrect.')
    context.bot.send_message(chat_id=chat_id, text=f'Your score is {scores[chat_id]}')
    #change the question
    # logic to check if all questions are answered

def message_handler(update, context):
    message = update.message
    text = message.text
    chat_id = message.chat_id
    context.bot.send_message(chat_id=chat_id, text='I am sorry I am not sure what you mean by that.')

def main():
    token = 'YOUR_TOKEN_HERE'
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    start_quiz_handler = CommandHandler('start', start_quiz)
    answer_handler = MessageHandler(Filters.text & (~Filters.command), check_answer)
    fallback_handler = MessageHandler(Filters.text, message_handler)
    dispatcher.add_handler(start_quiz_handler)
    dispatcher.add_handler(answer_handler)
    dispatcher.add_handler(fallback_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    """_summary_
    """