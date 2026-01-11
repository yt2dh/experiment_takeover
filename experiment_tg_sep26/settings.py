from os import environ


SESSION_CONFIGS = [

    dict(name='experiment_tg_fri3',
         display_name="fri3",
         app_sequence=['rrrt_fri3'],
         num_demo_participants=4,
         ),

]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['terminal','round_payoffs','final_payoff']

SESSION_FIELDS = [] 

LANGUAGE_CODE = 'en'


REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [

    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),


    dict(
        name='experiment_tg_fri3',
        display_name='fri3',
    ),

    dict(
        name='experiment_tg_fri4',
        display_name='fri4',
    ),


]

ADMIN_USERNAME = 'experiment'

ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '6499273906912'

INSTALLED_APPS = ['otree']



