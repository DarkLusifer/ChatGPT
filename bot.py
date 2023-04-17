import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up the bot and OpenAI API key
bot = telegram.Bot(token='6258527792:AAGfokeXCdxbRKph1jWdkggzHtH6ya_xy4g')
updater = Updater(token='6258527792:AAGfokeXCdxbRKph1jWdkggzHtH6ya_xy4g', use_context=True)
dispatcher = updater.dispatcher
openai.api_key = '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'

# Define a function to generate a response
def generate_response(text):
    prompt = f"User: {text}\nAI:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Define a message handler
def handle_message(update, context):
    message = update.message.text
    response = generate_response(message)
    context.bot.send_message(chat_id=update.message.chat_id, text=response)

message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
updater.idle()
