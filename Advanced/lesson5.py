from pyjokes import get_joke
import random
import os

class Chatbot:
    
    
    def __init__(self, bot_name='Bot', user='user'):
        self.name = bot_name
        self.user = user
        # Define a function in a function
        def hello():
            print('Hello, my name is {}'.format(self.name))
        # Call the function we just defined
        hello()

    def decor_func(some_func):
        '''
            Decorator to print 
            'bot_name says:' and 
            'user says:' when executing a feature
        '''
        def wrapper_func(self):
            print('{} says: '.format(self.name), end='')
            some_func(self)
            print('{} says: '.format(self.user), end='')
        return wrapper_func

    @decor_func
    def greetings(self):
        ''' Feature : bot says "Hi" '''
        print('Hi {}!! How may I help you?'.format(self.user))

    @decor_func
    def motivate_me(self):
        ''' Feature : bot tells you a motivational quote '''
        try:
            with open('quotes.txt', 'r') as file:
                quotes = file.read()
                quotes = quotes.split('\n')
                print(random.choice(quotes))
        except:
            print('Sorry, something went wrong.')

    @decor_func
    def jokes(self):
        ''' Feature : bot tells you a joke '''
        try:
            print(get_joke())
        except:
            print('Sorry, something went wrong.')

    @decor_func
    def features(self):
        ''' Feature: lists features of bot '''
        print('Currently I can only tell you jokes, motivate you and tell you about my features.')
    
    # COMMAND DICTIONARY
    ## map_words_to_command
    my_dict = {
        'greeting,hello,hey,hi': greetings,
        'fun,bored,bore,joke': jokes,
        'inspire,motivate,sad,feeling down': motivate_me,
        'do, feature': features,
        'bye, goodbye, night, sleep, get lost': 'lets exit!'
    }
        
    def process(self, input):
        '''
            Takes input and uses my_dict to map it to feature(function) for output
        '''
        input_string = input.lower()

        for key,value in Chatbot.my_dict.items():
            words = key.split(',')            
            for word in words:
                if word in input_string:
                    return value     
        return Chatbot.features

    def deploy(self, run=True):
        '''
            Input => Process => Output => Repeat
        '''
        while(run):
            print('{} says: '.format(self.user), end='')
            cmd = input()
            exec = self.process(cmd)
            if isinstance(exec, str):
                print('Good Bye!')
                os._exit(1)
            else:
                exec(self)

my_bot = Chatbot('Jarvis', 'Akshat')
my_bot.deploy()
