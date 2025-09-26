from os import environ


SESSION_CONFIGS = [

    dict(name='experiment_tg_fri3',
         display_name="fri3",
         app_sequence=['rrrt_fri3'],
         num_demo_participants=4,
         ),

    dict(name='experiment_tg_fri4',
         display_name="fri4",
         app_sequence=['rrrt_fri4'],
         num_demo_participants=4,
         ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['terminal','round_payoffs','final_payoff'
                     ] #names of fields to store a participant's data so that you can access the data from a previous app

SESSION_FIELDS = [] #global variables that are the same for all participants in the session

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),

    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),


    dict(
        name='experiment_tg_fri3',
        display_name='fri3',
        # participant_label_file='_rooms/your_study.txt',
        # use_secure_urls=True,
    ),

    dict(
        name='experiment_tg_fri4',
        display_name='fri4',
        # participant_label_file='_rooms/your_study.txt',
        # use_secure_urls=True,
    ),


    #dict(
        #name='experiment_uncertainty_two',
        #display_name='experiment_uncertainty_two',
        # participant_label_file='_rooms/your_study.txt',
        # use_secure_urls=True,
    #),

]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '6499273906912'

INSTALLED_APPS = ['otree']
