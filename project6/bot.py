import os
import random
import telebot

TOKEN = "7253372948:AAFbT5XuNgdGhPeorbIRsAWFUoKD9G217e0"
bot = telebot.TeleBot(TOKEN)  

class DataBase:
    def __init__(self, questions_file='questions.txt'):
        self.questions_file = questions_file
        self.load_questions()
        self.users = {}  

    def load_questions(self):
        self.questions = []
        if os.path.exists(self.questions_file):
            with open(self.questions_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            current_question = None
            for line in lines:
                line = line.strip()
                if line:
                    if line.startswith("q"):  
                        if current_question: 
                            self.questions.append(current_question)
                        current_question = {'text': line[2:], 'answers': [], 'correct': None}
                    elif current_question and line.endswith("\\\\"): 
                        line = line[:-2]
                        current_question['correct'] = len(current_question['answers'])
                        current_question['answers'].append(line)
                    elif current_question:  
                        current_question['answers'].append(line)

            if current_question: 
                self.questions.append(current_question)

            if not self.questions:  
                print("Error: No valid questions found in the file.")
        else:
            print(f"Error: File '{self.questions_file}' not found.")

        random.shuffle(self.questions)
        self.questions_count = len(self.questions)

    def get_user(self, chat_id):
        if chat_id not in self.users:
            self.users[chat_id] = {
                "chat_id": chat_id,
                "is_passing": False,
                "is_passed": False,
                "question_index": 0,
                "answers": []
                }
        return self.users[chat_id]

    def set_user(self, chat_id, update):
        if chat_id in self.users:
            self.users[chat_id].update(update)

    def get_question(self, index):
        return self.questions[index] if index < len(self.questions) else None

db = DataBase()

@bot.message_handler(commands=["start"])
def start(message):
    user = db.get_user(message.chat.id)

    if user["is_passed"]:
        bot.send_message(message.from_user.id, "You have already completed the quiz. Type /restart to start again.")
        return

    if user["is_passing"]:
        return

    db.set_user(message.chat.id, {"question_index": 0, "is_passing": True})

    user = db.get_user(message.chat.id)
    send_question_poll(user, message.chat.id)

@bot.message_handler(commands=["restart"])
def restart(message):
    db.set_user(message.chat.id, {"question_index": 0, "is_passing": True, "is_passed": False, "answers": []})
    start(message)

def send_question_poll(user, chat_id):
    question = db.get_question(user["question_index"])

    if question is None:
        count = 0
        for question_index, question in enumerate(db.questions):
            if question["correct"] == user["answers"][question_index]:
                count += 1
        percents = round(100 * count / db.questions_count)

        bot.send_message(chat_id, f"Quiz completed! You answered {percents}% correctly. Type /restart to play again or /finish to end.")

        db.set_user(chat_id, {"is_passed": True, "is_passing": False})
        return

    bot.send_poll(
        chat_id,
        question["text"],
        question["answers"],
        is_anonymous=False,
        allows_multiple_answers=False,
        type="quiz", 
        correct_option_id=question["correct"]  
    )
# таймер 
    threading.Timer(60, handle_next_question, args=(user, chat_id)).start()
def handle_next_question(user, chat_id):
    if not user["is_passing"]:
        return 
    user["question_index"] += 1
    db.set_user(chat_id, {"question_index": user["question_index"]})
    send_question_poll(user, chat_id) 
     
@bot.poll_answer_handler()
def handle_poll_answer(poll_answer):
    user = db.get_user(poll_answer.user.id)

    if user["is_passed"] or not user["is_passing"]:
        return

    selected_option = poll_answer.option_ids[0] if poll_answer.option_ids else -1
    user["answers"].append(selected_option)
    db.set_user(poll_answer.user.id, {"answers": user["answers"]})
    handle_next_question(user, poll_answer.user.id)
    
@bot.message_handler(commands=["start"])
def start(message):
    user= db.get_user(message.chat)
    if user["is_passed"]:
        bot.send_message(message.chat.id,"вы уже закончили квиз.Нажмите на рестарт чтобы начать снова!")
        return
    if user["is_passing"]:
        return
    db.set_user(message.chat.id,{"questions_index": 0,"is_passing":True})
    send_question_poll(user,message.chat.id)
@bot.message_handler(commands=['restart'])
def restart(message):
    db.set_user(message.chat.id,{'questions_index':0,"is_passing":True,'is_passed': False,'answers':[]})
@bot.message_handler(commands=['reset'])
def reset(message):
    db.reset_all_users()
    bot.send_message(message.chat.id,"Викторина сбросился для всех.Введите /start, чтобы начать снова")
    
if __name__ == "__main__":
    bot.polling(none_stop=True) 