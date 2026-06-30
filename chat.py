{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Following coding best practices: Added comments explaining functionality\
from django.core.management.base import BaseCommand\
from chatterbot import ChatBot\
from chatterbot.trainers import ChatterBotCorpusTrainer\
\
class Command(BaseCommand):\
    help = 'Runs a terminal-based chatbot client using Django and ChatterBot'\
\
    def handle(self, *args, **options):\
        self.stdout.write(self.style.SUCCESS('Initializing ChatBot... Please wait.'))\
        \
        # Initialize the chatterbot instance\
        chatbot = ChatBot(\
            'TerminalBot',\
            storage_adapter='chatterbot.storage.SQLStorageAdapter',\
            database_uri='sqlite:///db.sqlite3'\
        )\
        \
        # Train the chatbot with standard English greetings and conversations\
        trainer = ChatterBotCorpusTrainer(chatbot)\
        trainer.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.conversations")\
        \
        self.stdout.write(self.style.SUCCESS('\\nBot is ready! Type "exit" or "quit" to stop.'))\
        self.stdout.write("--------------------------------------------------\\n")\
        \
        # Main conversational loop\
        while True:\
            try:\
                # Read user input from terminal\
                user_input = input('user: ')\
                \
                # Check for exit commands\
                if user_input.lower() in ['exit', 'quit']:\
                    self.stdout.write('bot: Goodbye!')\
                    break\
                \
                # Generate and print response from the bot\
                bot_response = chatbot.get_response(user_input)\
                print(f'bot: \{bot_response\}')\
                \
            except (KeyboardInterrupt, EOFError):\
                self.stdout.write('\\nbot: Goodbye!')\
                break}