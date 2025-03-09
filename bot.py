from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = ''

# Przechowuj dane o grze
user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Witaj! Aby zacząć grę, użyj komendy /start_game.')

async def start_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data[update.message.chat.id] = {'question_number': 0, 'correct_answers': 0}
    await ask_question(update)

async def ask_question(update: Update) -> None:
    chat_id = update.message.chat.id
    question_number = user_data[chat_id]['question_number']
    
    if question_number >= 10:  # Zakończenie gry po 10 pytaniach
        await update.message.reply_text(f'Gra zakończona! Twój wynik: {user_data[chat_id]["correct_answers"]} poprawnych odpowiedzi.')
        return
    
    # Pytania
    questions = [
        'Ile to 2 + 2?', 
        'Ile to 5 + 3?', 
        'Ile to 3 + 4?', 
        'Ile to 7 + 1?', 
        'Ile to 9 + 1?', 
        'Ile to 3 + 5?', 
        'Ile to 8 + 2?', 
        'Ile to 6 + 3?', 
        'Ile to 4 + 5?', 
        'Ile to 10 + 0?'
    ]
    
    # Odpowiedzi
    answers = [
        '4', '8', '7', '8', '10', '8', '10', '9', '9', '10'
    ]
    
    # Zadaj pytanie
    question = questions[question_number]
    await update.message.reply_text(f'{question}\n\nOdpowiedzi: 1. 1, 2. 2, 3. 3, 4. 4, 5. 5, 6. 6, 7. 7, 8. 8, 9. 9, 10. 10')

async def check_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat.id
    user_answer = update.message.text
    question_number = user_data[chat_id]['question_number']
    
    # Prawidłowe odpowiedzi
    correct_answers = [
        '4', '8', '7', '8', '10', '8', '10', '9', '9', '10'
    ]
    
    # Sprawdzanie odpowiedzi
    if user_answer == correct_answers[question_number]:
        user_data[chat_id]['correct_answers'] += 1
        await update.message.reply_text('Poprawna odpowiedź!')
    else:
        await update.message.reply_text('Niepoprawna odpowiedź! Chcesz spróbować ponownie?')

    # Przejdź do kolejnego pytania
    user_data[chat_id]['question_number'] += 1
    await ask_question(update)

def main():
    # Tworzymy aplikację
    application = Application.builder().token(TOKEN).build()

    # Komendy i obsługa wiadomości
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("start_game", start_game))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer))

    # Uruchamiamy bota
    application.run_polling()

if __name__ == '__main__':
    main()
