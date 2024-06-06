import sys
import csv
import openai
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon
import qtawesome as qta
from dotenv import load_dotenv
import os

# Cargar las variables de entorno y configurar la API de OpenAI
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

class ChatbotInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.faq_responses = self.load_faq_responses("faq_responses.csv")
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ChatBot Campus Virtual Usta Tunja')
        self.setWindowIcon(QIcon(qta.icon('fa5s.brain')))
        self.setGeometry(300, 300, 480, 320)

        layout = QVBoxLayout()

        self.conversationArea = QTextEdit(self)
        self.conversationArea.setReadOnly(True)
        self.initial_greeting()
        layout.addWidget(self.conversationArea)

        self.inputField = QLineEdit(self)
        self.inputField.setPlaceholderText("Escribe tu mensaje aquí...")
        self.inputField.returnPressed.connect(self.send_message)
        layout.addWidget(self.inputField)
        
        self.sendButton = QPushButton(self)
        self.sendButton.setIcon(qta.icon('fa5.paper-plane'))
        self.sendButton.setText('Enviar')
        self.sendButton.clicked.connect(self.send_message)
        layout.addWidget(self.sendButton)

        self.setLayout(layout)

    def initial_greeting(self):
        greeting_message = "¡Hola! Soy el ChatBot del Campus Virtual de la Usta Tunja. Puedes preguntarme sobre horarios de clases, fechas de exámenes, eventos universitarios y mucho más."
        self.update_conversation("bot", greeting_message)

    def send_message(self):
        user_message = self.inputField.text().strip()
        if user_message:
            self.update_conversation("user", user_message)
            self.inputField.clear()
            response_message = self.simulated_or_openai_response(user_message.lower())
            self.update_conversation("bot", response_message)

    def update_conversation(self, sender, message):
        if sender == "user":
            message_html = f'<div style="text-align: right; color: blue; padding: 5px; margin: 5px; background-color: #D0E4FE;">Tú: {message}</div>'
        else:  # sender == "bot"
            message_html = f'<div style="text-align: left; color: green; padding: 5px; margin: 5px; background-color: #E8F5E9;">Bot: {message}</div>'
        self.conversationArea.append(message_html)

    def simulated_or_openai_response(self, user_message):
        simulated_response = self.simulated_response(user_message)
        if simulated_response != "Lo siento, no tengo información sobre eso. Por favor, verifica en el portal del estudiante.":
            return simulated_response
        return self.get_response_from_openai(user_message)

    def simulated_response(self, user_message):
        return self.faq_responses.get(user_message, "Lo siento, no tengo información sobre eso. Por favor, verifica en el portal del estudiante.")

    def load_faq_responses(self, filepath):
        responses = {}
        with open(filepath, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                if len(row) == 2:
                    question, answer = row
                    responses[question.strip().lower()] = answer.strip()
        return responses

    def get_response_from_openai(self, user_message):
        model = "gpt-3.5-turbo-0125"
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": user_message}],
                max_tokens=150
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            return f"Error al obtener respuesta: {str(e)}"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = ChatbotInterface()
    ex.show()
    sys.exit(app.exec())
