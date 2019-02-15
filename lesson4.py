from pyjokes import get_joke
import random

class Chatbot:
    def __init__(self, bot_name='Bot', user='user'):
        self.name = bot_name
        self.user = user
        # Define a function in a function
        def hello():
            print('Hello, my name is {}'.format(self.name))
            print('{} says: '.format(self.user), end='')
        # Call the function we just defined
        hello()

    def decor_func(some_func):

        def wrapper_func(self):
            print('{} says: '.format(self.name), end='')
            some_func(self)
            print('{} says: '.format(self.user), end='')
        return wrapper_func

    @decor_func
    def greetings(self):
        print('Hi {}!! How may I help you?'.format(self.user))

    @decor_func
    def motivate_me(self):
        try:
            with open('quotes.txt', 'r') as file:
                quotes = file.read()
                quotes = quotes.split('\n')
                print(random.choice(quotes))
        except:
            print('Sorry, something went wrong.')

    @decor_func
    def jokes(self):
        try:
            print(get_joke())
        except:
            print('Sorry, something went wrong.')

    @decor_func
    def features(self):
        print('Currently I can only tell you jokes and motivate you.')

    def process(self, input):

        input_string = input.lower()

        # map_words_to_command
        my_dict = {
            'greeting,hello,hey,hi': self.greetings,
            'fun,bored,bore,joke': self.jokes,
            'inspire,motivate,sad,feeling down': self.motivate_me,
            # 'bye': exit()
        }

        for key,value in my_dict.items():
            words = key.split(',')            
            for word in words:
                print(word)
                if word in input_string:
                    return value     
        return self.features

    def deploy(self, run=True):
        while(run):
            cmd = input()
            exec = self.process(cmd)
            if isinstance(exec, str):
                exec()
            else:
                exec()

my_bot = Chatbot('Jarvis', 'Akshat')
my_bot.deploy()
