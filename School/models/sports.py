from odoo import fields, models, api
from odoo.exceptions import UserError


class Sports(models.Model):
    _name = 'sport.activity'
    _description = 'sports'

    p_id = fields.Integer(string='p_id')

    sport_name = fields.Selection(
        [('cricket', 'Cricket'),
         ('football', 'Football')
        ],
        string='Sports'
    )

    #Cricket
    #player Details
    player_name = fields.Char(string="Player Name")
    player_age = fields.Integer(String='Age')
    player_gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    player_phone = fields.Char(string='Phone')

    #cricket specifics:
    c_team = fields.Selection(
        [('csk','CSK'),
         ('rcb','RCB'),
         ('mi', 'MI')],
         string='Team'
    )
    style = fields.Selection(
        [('batsman','Batsman'),
         ('bowler', 'Bowler'),
         ('all_round', 'All Rounder')
        ],
        string="Style"
    )

    #Batting statistics
    total_run = fields.Integer(string='Total Runs')
    centuries = fields.Integer(string='Centuries')
    half_centuries = fields.Integer(string='Half Centuries')
    fours = fields.Integer(string='Fours')
    sixes = fields.Integer(string='Sixes')
    batting_average = fields.Integer(string='Batting Average')

    #Bowling Statistics
    wicket = fields.Integer(string='Wicker Taken')
    dot_balls = fields.Integer(string='Dot Balls')
    bowling_average = fields.Integer(string='Bowling Average')
    five_wicket = fields.Integer(string='Five-Wicket Hauls')

    #fielding Statistics
    catches = fields.Integer(string='Catches')
    run_outs = fields.Integer(string='Run-Outs')
    stumping = fields.Integer(string='Stumpings')

    #Match Record
    match_played = fields.Integer(string='Match Played')
    inning_played = fields.Integer(string='Inning Played')
    c_matches_won = fields.Integer(string='Matches Won')
    matches_lost = fields.Integer(string='Matches Lost')
    matches_draw = fields.Integer(string='Matches Draw/Tied')

    #performance matrics
    man_of_the_match = fields.Integer(string='Player of the Match Awards')
    man_of_the_series = fields.Integer(string='Player of the Series Awards')




    #Football
    f_team = fields.Selection(
        [('india', 'India'),
         ('argentina', 'Argentina'),
         ('brazil', 'Brazil')],
        string='Team'
    )

    position = fields.Selection(
        [('goalkeeper', 'Goal Keeper'),
         ('defenders', 'Defenders'),
         ('midfielders', 'Midfielders'),
         ('forwards', 'Forwards')],
        string='Position'
    )

    #Match Records
    matches_played = fields.Integer(string='Matches Played')
    matches_started = fields.Integer(string='Matches Started')
    f_matches_won = fields.Integer(string='Matches Won')
    goals_scored_in_wins = fields.Integer(string='Goals Scored in Wins')
    clean_sheets_in_wins = fields.Integer(string='Clean Sheets in Wins')


    #Match Statistics
    goals_scored = fields.Integer(string='Goals Scored')
    assists = fields.Integer(string='Assists')
    pass_completion_rate = fields.Float(string='Pass Completion Rate')
    shots_on_target = fields.Integer(string='Shots on Target')
    minutes_played = fields.Integer(string='Minutes Played')

    # Team Statistics
    possession_percentage = fields.Float(string='Possession Percentage')
    shots_on_goal = fields.Integer(string='Shots on Goal')
    passes_completed = fields.Integer(string='Passes Completed')
    corners_taken = fields.Integer(string='Corners Taken')
    tackles = fields.Integer(string='Tackles')

    #Performance Matrics
    man_of_the_match_awards = fields.Integer(string='Man of the Match Awards')
    average_rating = fields.Float(string='Average Rating')
    distance_covered = fields.Float(string='Distance Covered (km)')
    sprint_speed = fields.Float(string='Sprint Speed (km/h)')
    aerial_duels_won = fields.Integer(string='Aerial Duels Won')


    def unlink(self):
        raise UserError("you can not delete this record")

    def _search_ids(self):
        players_id = self.env['sport.activity'].search([])
        print("players id>>>>>>>>>> ", players_id)


