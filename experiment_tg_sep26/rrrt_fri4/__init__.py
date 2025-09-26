from otree.api import *
import random
import numpy as np
import itertools

doc = """
Your app description
"""

BOOL_Choice = ((False, "rejected"),(True, "accepted"))

QList = ["Question1Pair1",
         "Question1Pair2",
         "Question1Pair3",
         "Question1Pair4",
         "Question1Pair5",
         "Question1Pair6",
         "Question1Pair7",
         "Question1Pair8",
         "Question1Pair9",
         "Question1Pair10"
         ]
BOOL_Choice_HL = [(0, "Option ONE"), (1, "Option TWO")]

Q1_Choice = [(0, "$1"),
                 (1, "$1.50"),
                 (2, "$2"),
                 (3, "$3")]

Q2_Choice = [(0, "$1"),
                 (1, "$1.50"),
                 (2, "$2"),
                 (3, "$3")]

Q3_Choice = [(0, "$1"),
                 (1, "$1.50"),
                 (2, "$2"),
                 (3, "$3")]

#Fixed_Float_Values = [[f'{0.80:.2f}', f'{1.00:.2f}', f'{1.25:.2f}'],# Round 1
                      #[f'{0.80:.2f}', f'{1.00:.2f}', f'{4.00:.2f}'], # Round 2
                      #[f'{0.20:.2f}', f'{1.00:.2f}', f'{4.00:.2f}']
                      #]

#Fixed_Float_Values Round 1 [beta, thetamax, endowment, 1-beta]
Fixed_Float_Values = [[0.80, 1.20, 1.80, 0.20],  #1
                      [0.80, 4.00, 6.00, 0.20],  #9
                      [0.80, 1.20, 1.80, 0.20],  #5
                      [0.20, 4.00, 6.00, 0.80],  #14
                      [0.80, 4.00, 6.00, 0.20],  #7
                      [0.80, 4.00, 6.00, 0.20],  #6
                      [0.80, 1.20, 1.80, 0.20],  #4
                      [0.80, 4.00, 6.00, 0.20],  #10
                      [0.20, 4.00, 6.00, 0.80],  #13
                      [0.20, 4.00, 6.00, 0.80],  # 12
                      [0.20, 4.00, 6.00, 0.80],  # 11
                      [0.80, 1.20, 1.80, 0.20],  #2
                      [0.20, 4.00, 6.00, 0.80],  #15
                      [0.80, 1.20, 1.80, 0.20],  # 3
                      [0.80, 4.00, 6.00, 0.20],  # 8
                      ]

#1[11, 9, 12, 6, 2, 14, 4, 7, 5, 10, 3, 15, 1, 8, 13]
#2[5, 14, 15, 10, 6, 4, 13, 2, 7, 12, 9, 8, 1, 11, 3]
#3[15, 12, 14, 6, 13, 1, 10, 2, 8, 4, 5, 11, 3, 7, 9]
#4[5, 2, 11, 1, 12, 4, 15, 13, 9, 14, 3, 8, 6, 10, 7]
#5[13, 8, 9, 7, 14, 1, 2, 6, 12, 15, 3, 4, 5, 11, 10]
#6[3, 9, 11, 13, 6, 8, 14, 1, 7, 10, 5, 15, 12, 4, 2]
#7[7, 2, 10, 15, 12, 11, 14, 8, 4, 9, 5, 3, 13, 1, 6]
#8[12, 13, 15, 11, 7, 14, 1, 9, 2, 3, 4, 8, 10, 5, 6]
#9[9, 2, 3, 6, 8, 7, 15, 10, 1, 11, 14, 13, 12, 5, 4]
#10[15, 3, 2, 5, 4, 13, 1, 7, 9, 8, 12, 14, 10, 6, 11]
#11[5, 6, 7, 9, 13, 11, 8, 14, 10, 3, 1, 12, 15, 2, 4]
#12[1, 9, 5, 14, 7, 6, 4, 10, 13, 12, 11, 2, 15, 3, 8]

class Constants(BaseConstants): #parameters that stay the same for all players
    name_in_url = 'rrrt_fri4'
    players_per_group = 2
    num_rounds = 15
    multiplier = 1.5

    buyer_role = 'buyer'
    seller_role = 'seller'

    ThetaMin = 1.00
    payoff_reject_buyer = 0
    fee = 10
    #firm_value = 2

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    subsession.group_randomly(fixed_id_in_group=False)
    import itertools
    RoundPython_ss = subsession.round_number - 1
    all_types_buyer = [Constants.ThetaMin, Fixed_Float_Values[RoundPython_ss][1]]* 3
    all_types_seller = [Constants.ThetaMin, Fixed_Float_Values[RoundPython_ss][1]]* 3
    random.shuffle(all_types_buyer)
    random.shuffle(all_types_seller)
    type_buyer = itertools.cycle(all_types_buyer)
    type_seller = itertools.cycle(all_types_seller)
    for player in subsession.get_players():
        if player.role == 'buyer':
            player.signal = next(type_buyer)
            player.signal_weight = player.signal * Fixed_Float_Values[RoundPython_ss][0]
            player.signal_weight_opp_high = Fixed_Float_Values[RoundPython_ss][1] * Fixed_Float_Values[RoundPython_ss][3]
            player.signal_weight_opp_low = Constants.ThetaMin * Fixed_Float_Values[RoundPython_ss][3]
            player.signal_weight_total_high = player.signal_weight + player.signal_weight_opp_high
            player.signal_weight_total_low = player.signal_weight + player.signal_weight_opp_low
            player.signal_weight_total_fifty_high = 1.5 * player.signal_weight_total_high
            player.signal_weight_total_fifty_low = 1.5 * player.signal_weight_total_low
        else:
            player.signal = next(type_seller)
            player.signal_weight = player.signal * Fixed_Float_Values[RoundPython_ss][3]
            player.signal_weight_opp_high = Fixed_Float_Values[RoundPython_ss][1] * Fixed_Float_Values[RoundPython_ss][0]
            player.signal_weight_opp_low = Constants.ThetaMin * Fixed_Float_Values[RoundPython_ss][0]
            player.signal_weight_total_high = player.signal_weight + player.signal_weight_opp_high
            player.signal_weight_total_low = player.signal_weight + player.signal_weight_opp_low
            player.signal_weight_total_fifty_high = 1.5 * player.signal_weight_total_high
            player.signal_weight_total_fifty_low = 1.5 * player.signal_weight_total_low


class Group(BaseGroup):
    #RoundPython_sd = group.round_number - 1
    #buyer_choice = models.CurrencyField(min=Constants.ThetaMin, max=2)
    #buyer_choice = models.CurrencyField(min=Constants.ThetaMin, max=Fixed_Float_Values[RoundPython_sd][2])
    buyer_choice = models.CurrencyField()
    seller_choice = models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=BOOL_Choice)
    pass


class Player(BasePlayer):
    terminal = models.StringField(label="Please enter the number assigned to your computer terminal.",
                                     max_length=2)
    Q1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=Q1_Choice)
    Q2 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=Q2_Choice)
    Q3 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=Q3_Choice)
    Q1_answer=models.StringField()
    Q2_answer = models.StringField()
    Q3_answer = models.StringField()
    signal = models.CurrencyField()
    signal_weight = models.CurrencyField()
    signal_weight_opp_high = models.CurrencyField()
    signal_weight_opp_low = models.CurrencyField()
    signal_weight_total_high = models.CurrencyField()
    signal_weight_total_low = models.CurrencyField()
    signal_weight_total_fifty_high = models.CurrencyField()
    signal_weight_total_fifty_low = models.CurrencyField()
    is_buyer = models.IntegerField()
    firm_value = models.CurrencyField()
    selected_round = models.IntegerField()
    selected_payoff = models.CurrencyField()
    selected_payoff_scaled = models.CurrencyField()
    final_payoff = models.CurrencyField()
    ## Question 1
    Question1Pair1 = models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=BOOL_Choice_HL, label=""
                                         )
    Question1Pair2 = models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=BOOL_Choice_HL, label=""
                                         )
    Question1Pair3 = models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=BOOL_Choice_HL, label=""
                                         )
    Question1Pair4 = models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=BOOL_Choice_HL, label=""
                                         )
    Question1Pair5 = models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=BOOL_Choice_HL, label=""
                                         )
    Question1Pair6 = models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=BOOL_Choice_HL, label=""
                                         )
    Question1Pair7 = models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=BOOL_Choice_HL, label=""
                                         )
    Question1Pair8 = models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=BOOL_Choice_HL, label=""
                                         )
    Question1Pair9 = models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=BOOL_Choice_HL, label=""
                                         )
    Question1Pair10 = models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=BOOL_Choice_HL, label=""
                                          )
    AT_Choice = models.StringField()
    AT_Payoff = models.CurrencyField()
    pass


#def buyer_choice_choices(player: Player):
    #RoundPython = player.round_number - 1
    #return currency_range(Constants.ThetaMin, Fixed_Float_Values[RoundPython][2], 0.01)

def buyer_choice_min(player: Player):
    return Constants.payoff_reject_buyer #minimum_bid=0

def buyer_choice_max(player: Player):
    RoundPython = player.round_number - 1
    return Fixed_Float_Values[RoundPython][2]

#def get_partner(player: Player):
    #return player.get_others_in_group()[0]

#def buyer_choice_error_message(player, value):
    #RoundPython = group.round_number - 1
    #print('value is', value)
    #if value > 5:
        #return 'Cannot offer more than your remaining budget'
    #RoundPython = group.round_number - 1
    #print('value is', value)
    #if value > Fixed_Float_Values[RoundPython][2]:
        #return 'Cannot offer more than your remaining budget'

def set_payoffs(group: Group):
    for p in group.get_players():
        set_payoff(group)

def set_payoff(group: Group):
    buyer, seller = group.get_players()
    #record roles
    buyer.is_buyer = 1
    seller.is_buyer = 0

    buyer_choice= group.buyer_choice
    seller_choice = group.seller_choice

    RoundPython_g = group.round_number - 1

    firm_value = Fixed_Float_Values[RoundPython_g][0] * buyer.signal + Fixed_Float_Values[RoundPython_g][3] * seller.signal

    if not group.seller_choice:
        buyer.payoff = Constants.payoff_reject_buyer
        seller.payoff = firm_value
        buyer.firm_value = firm_value
        seller.firm_value = firm_value
    else:
        buyer.payoff = Constants.multiplier * firm_value - buyer_choice
        seller.payoff = buyer_choice
        buyer.firm_value = firm_value
        seller.firm_value = firm_value

    #players = group.get_players()
    #for p in enumerate(players):
        #p.payoff = payoff  # Assign as integer
        #if 'round_payoffs' not in p.participant.vars:
            #p.participant.vars['round_payoffs'] = []
        # Store as plain integer, not Currency
        #participant = players.participant
        #participant.round_payoffs.append(p.payoff)
        #p.participant.vars['round_payoffs'].append(p.payoff)
        #print(
            #f"Player {p.id_in_group}, Round {p.round_number}: Payoff = {p.payoff}, Round Payoffs = {p.participant.vars['round_payoffs']}")

    #random_round = random.randint(1, Constants.num_rounds)
    #for player in enumerate(players):
        #if player.round_number == random_round:
            #player.selected_round = random_round
            #player_in_selected_round = player.in_round(random_round)
            #player.final_payoff = payoff
    #for p in enumerate(players):
        #p.payoff = payoff  # Assign as integer
        #if 'round_payoffs' not in p.participant.vars:
            #p.participant.vars['round_payoffs'] = []
            # Store as plain integer, not Currency
            #p.participant.vars['round_payoffs'].append(int(p.payoff))
        #p.participant.vars['round_payoffs'].append(p.payoff)
        #print(
            #f"Player {p.id_in_group}, Round {p.round_number}: Payoff = {p.payoff}, Round Payoffs = {p.participant.vars['round_payoffs']}")


def set_final_payoffs(group: Group):
    #players = group.get_players()
    for p in group.get_players():
        p.selected_round = random.randint(1, Constants.num_rounds)
        player_in_selected_round = p.in_round(p.selected_round)
        p.selected_payoff = player_in_selected_round.payoff
        p.selected_payoff_scaled = p.selected_payoff * 4
        p.final_payoff =(player_in_selected_round.payoff * 4) + Constants.fee + p.AT_Payoff

    #if player.round_number == selected_round:
        #player.selected_round = selected_round
        #player.final_payoff = payoff
        #seller.selected_round = selected_round
        #seller.final_payoff = seller.payoff

    #print(f"Setting final payoffs for group {group.id_in_subsession}")
    #for p in group.get_players():
        #round_payoffs = p.participant.vars.get('round_payoffs', [])
        #print(f"Player {p.id_in_group}: Round Payoffs = {round_payoffs}")
        #if round_payoffs and len(round_payoffs) >= Constants.num_rounds:
            #p.selected_round = random.randint(1, Constants.num_rounds)
            #p.final_payoff = round_payoffs[p.selected_round - 1]  # Already an int
            #p.participant.payoff = p.final_payoff  # Store as int
        #else:
            #p.selected_round = 0
            #p.final_payoff = 0
            #p.participant.payoff = p.final_payoff
        #print(f"Player {p.id_in_group}: Selected Round = {p.selected_round}, Final Payoff = {p.final_payoff}")


# PAGES
class Welcome(Page):
    form_model = 'player'
    form_fields = ["terminal"]

    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.terminal = player.terminal

    def is_displayed(self):
        return self.round_number == 1
    pass

class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1
    pass

class Intro_2(Page):
    def is_displayed(self):
        return self.round_number == 1
    pass

class Intro_3(Page):
    def is_displayed(self):
        return self.round_number == 1
    pass

class Intro_Questions(Page):
    form_model = 'player'
    form_fields = ["Q1", "Q2", "Q3"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.Q1 == 1:
            player.Q1_answer = "correct"
        else:
            player.Q1_answer = "wrong"

        if player.Q2 == 2:
            player.Q2_answer = "correct"
        else:
            player.Q2_answer = "wrong"

        if player.Q3 == 2:
            player.Q3_answer = "correct"
        else:
            player.Q3_answer = "wrong"

    def is_displayed(self):
        return self.round_number == 1
    pass

class Intro_Answers(Page):
    def is_displayed(self):
        return self.round_number == 1
    pass

class IntroWaitPage(WaitPage):
    wait_for_all_groups = True
    pass

class CompareNumsChoice(Page):
    form_model = 'group'
    form_fields = ["buyer_choice"]

    def vars_for_template(player): #pass variables to the template
        RoundPython = player.round_number - 1
        Beta = Fixed_Float_Values[RoundPython][0]
        ThetaMax = Fixed_Float_Values[RoundPython][1]
        Endowment = Fixed_Float_Values[RoundPython][2]
        Beta_Complement= Fixed_Float_Values[RoundPython][3]
        return dict(
            Beta=Beta,
            ThetaMax=ThetaMax,
            Endowment=Endowment,
            Beta_Complement=Beta_Complement
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1
    pass

class WaitPagebuyer(WaitPage):
    wait_for_all_groups = True
    template_name = 'rrrt_fri4/WaitPagebuyer.html'

    #def vars_for_template(player: Player):
        #values_to_display = {}
        #for p in player.in_all_rounds():
            #value = p.field_maybe_none('firm_value')
            #key = f'value_in_round_{player.round_number}'
            # if value is defined in the round, use its value
            #if value:
                #values_to_display[key] = value
            # if not defined, replace with ?
            #else:
                #values_to_display[key] = "?"

        #return dict(
            #values_to_display=values_to_display,
        #)

    def vars_for_template(player):
        if player.round_number > 1:
            prev_player = player.in_round(player.round_number - 1)
            prev_payoff = prev_player.payoff
            prev_firm_value = prev_player.firm_value
            prev_buyer_choice = prev_player.group.buyer_choice
            prev_seller_choice_before = prev_player.group.seller_choice
            if prev_seller_choice_before == True:
                prev_seller_choice = "accepted"
            else:
                prev_seller_choice = "rejected"
            prev_is_buyer_before = prev_player.is_buyer
            if prev_is_buyer_before == 1:
                prev_is_buyer = "buyer"
            else:
                prev_is_buyer = "seller"
            #Seller_Choice = group.seller_choice
            return dict(
                #payoff=payoff,
                prev_payoff=prev_payoff,
                prev_firm_value=prev_firm_value,
                prev_buyer_choice=prev_buyer_choice,
                prev_seller_choice=prev_seller_choice,
                prev_is_buyer=prev_is_buyer,
                #Seller_Choice=Seller_Choice
            )

pass

class CompareNumsChoice_seller(Page):
    form_model = 'group'
    form_fields = ["seller_choice"]

    def vars_for_template(player): #pass variables to the template
        RoundPython = player.round_number - 1
        Beta = Fixed_Float_Values[RoundPython][0]
        ThetaMax = Fixed_Float_Values[RoundPython][1]
        Endowment = Fixed_Float_Values[RoundPython][2]
        Beta_Complement = Fixed_Float_Values[RoundPython][3]
        return dict(
            Beta=Beta,
            ThetaMax=ThetaMax,
            Endowment=Endowment,
            Beta_Complement=Beta_Complement
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2
    pass

class WaitPageseller(WaitPage):
    wait_for_all_groups = True
    template_name = 'rrrt_fri4/WaitPageseller.html'

    def vars_for_template(player):
        if player.round_number > 1:
            prev_player = player.in_round(player.round_number - 1)
            prev_payoff = prev_player.payoff
            prev_firm_value = prev_player.firm_value
            prev_buyer_choice = prev_player.group.buyer_choice
            prev_seller_choice_before = prev_player.group.seller_choice
            if prev_seller_choice_before == True:
                prev_seller_choice = "accepted"
            else:
                prev_seller_choice = "rejected"
            prev_is_buyer_before = prev_player.is_buyer
            if prev_is_buyer_before == 1:
                prev_is_buyer = "buyer"
            else:
                prev_is_buyer = "seller"
            #Seller_Choice = group.seller_choice
            return dict(
                #payoff=payoff,
                prev_payoff=prev_payoff,
                prev_firm_value=prev_firm_value,
                prev_buyer_choice=prev_buyer_choice,
                prev_seller_choice=prev_seller_choice,
                prev_is_buyer=prev_is_buyer
                #Seller_Choice=Seller_Choice
            )

    pass

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
    #def before_next_page(player: Player, timeout_happened): #execute code below after form validation, before player proceeds to the next page
        #import random
        #player.selected_round =1
        #participant = player.participant
        #participant.selected_round = 1
        # if it's the last round
        #if player.round_number == Constants.num_rounds:
            #random_round = random.randint(1, Constants.num_rounds)
            #participant.selected_round = 1
            #player_in_selected_round = player.in_round(1)
            #player.payoff = player_in_selected_round.payoff


        #random_round = random.randint(1, Constants.num_rounds)
        #if player.round_number == 1:
            #participant = player.participant
            #participant.selected_round = player.round_number
            #player_in_selected_round = player.in_round(random_round)
            #if player.role == 'buyer':
                #participant.Total = player.payoff
            #else:
                #participant.Total = player.payoff

           #def vars_for_template(player):
                #return dict(
                    #selected_round=selected_round,
                    #payoff_final=payoff_final
                #)
            #if player.seller_choice is True: #1: fixed price; 0:price range
                #participant.PaymentSellerChoice = "accepted"
                #participant.CostS2 = 3.00
            #else:
                #participant.PaymentSellerChoice = "rejected"
                #participant.CostS2 = 3.50
            #participant.Total = 6.00 - participant.CostS2
            #participant.Total = round(participant.Total, 2)
    pass

class Outcome(Page):
    def vars_for_template(group):
        Buyer_Choice = group.buyer_choice
        Seller_Choice = group.seller_choice
        return dict(
            Buyer_Choice = Buyer_Choice,
            Seller_Choice = Seller_Choice,
        )

    def vars_for_template(player): #pass variables to the template
        RoundPython = player.round_number - 1
        Beta = Fixed_Float_Values[RoundPython][0]
        ThetaMax = Fixed_Float_Values[RoundPython][1]
        Endowment = Fixed_Float_Values[RoundPython][2]
        Beta_Complement = Fixed_Float_Values[RoundPython][3]
        is_buyer = player.is_buyer
        if is_buyer == 1:
            is_buyer_after = "buyer"
        else:
            is_buyer_after = "seller"
        return dict(
            Beta=Beta,
            ThetaMax=ThetaMax,
            Endowment=Endowment,
            Beta_Complement=Beta_Complement,
            is_buyer_after=is_buyer_after
        )

    @staticmethod
    def is_displayed(group: Group):
        return group.id_in_group == 1 or 2

    pass

class Additional_Task(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ["Question1Pair1",
                   "Question1Pair2",
                   "Question1Pair3",
                   "Question1Pair4",
                   "Question1Pair5",
                   "Question1Pair6",
                   "Question1Pair7",
                   "Question1Pair8",
                   "Question1Pair9",
                   "Question1Pair10"
                   ]

    def before_next_page(player: Player, timeout_happened):
        # participant = player.participant
        ## Change the question number/payoff with randomness
        if player.Question1Pair5 is True:  # change Pair8
            player.AT_Choice = "Option 2"
            player.AT_Payoff = 0.10  # change
        else:
            player.AT_Choice = "Option 1"
            player.AT_Payoff = 2.00  # change
        #participant.SubTotal = participant.TotalS2 + participant.TotalS1 + participant.TotalS2b
        #participant.TotalS2 = 6.00 - participant.CostS2
        #participant.TotalS2 = round(participant.TotalS2, 2)
        #participant.Total = participant.SubTotal + participant.S3_Payoff #show up fee = 0
        #participant.Total = round(participant.Total, 2)
    pass

class FinalWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    after_all_players_arrive = set_final_payoffs
    pass

class Payoff(Page):
    @staticmethod
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'selected_round': self.selected_round,
            'final_payoff': self.final_payoff
        }
    pass

page_sequence = [Welcome, Intro, Intro_2, Intro_3, Intro_Questions, Intro_Answers, IntroWaitPage, CompareNumsChoice, WaitPagebuyer, CompareNumsChoice_seller, WaitPageseller, ResultsWaitPage, Outcome, Additional_Task, FinalWaitPage, Payoff]

