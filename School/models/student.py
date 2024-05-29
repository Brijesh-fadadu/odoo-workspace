from odoo import fields, models, api, _
from datetime import date
from dateutil.relativedelta import relativedelta



class Student(models.Model):
    _inherit = 'res.partner'
    dob = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age')
    new_gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    class_id = fields.Many2one('school_class', string='Subject')
    teacher_id = fields.Many2one(related='class_id.teacher_id', string='Class Teacher', tracking=True)
    admission_date = fields.Date(string='Admission Date', default=date.today())
    status = fields.Selection([('unpaid','Unpaid'), ('paid','Paid') ], string='Fees Status', required=True, default='unpaid')

    identity = fields.Selection([('Teacher', 'Teacher'), ('Student','Student')], string='Identity', readonly=1)

    #Master Education Details
    new_class_id = fields.Many2one('new.class', string='Standard')
    new_section_id = fields.Many2one('new.section', string='Section')
    new_subjects_ids = fields.Many2many('new.subject',stirng='Subjects')

    @api.onchange('new_class_id','new_section_id')
    def _compute_subjects(self):
        search_master_data = self.env['master.education'].search([('class_id', '=', self.new_class_id.id),
                                                                  ('section_id', '=', self.new_section_id.id)
                                                                  ])
        ids_of_subject = search_master_data.mapped('subject_ids.id')
        # (1,2,3,9)
        print(ids_of_subject)
        self.write({"new_subjects_ids": [(6, 0, ids_of_subject)]})








    # Teacher Columns
    subject_taught = fields.Char(string='Subject Taught')
    class_ids = fields.One2many('school_class', 'teacher_id', string='Class Taught')
    joining_date = fields.Date(string='Joining Date', default=date.today())


    #Sports
    sport_name = fields.Selection(
        [('cricket', 'Cricket'),
         ('football', 'Football')],
        string='Sports'
    )

    #Cricket

    # cricket specifics:
    c_team = fields.Selection(
        [('csk', 'CSK'),
         ('rcb', 'RCB'),
         ('mi', 'MI')],
        string='Team'
    )
    style = fields.Selection(
        [('batsman', 'Batsman'),
         ('bowler', 'Bowler'),
         ('all_round', 'All Rounder')
         ],
        string="Style"
    )

    # Batting statistics
    total_run = fields.Integer(string='Total Runs')
    centuries = fields.Integer(string='Centuries')
    half_centuries = fields.Integer(string='Half Centuries')
    fours = fields.Integer(string='Fours')
    sixes = fields.Integer(string='Sixes')
    batting_average = fields.Integer(string='Batting Average')

    # Bowling Statistics
    wicket = fields.Integer(string='Wicker Taken')
    dot_balls = fields.Integer(string='Dot Balls')
    bowling_average = fields.Integer(string='Bowling Average')
    five_wicket = fields.Integer(string='Five-Wicket Hauls')

    # fielding Statistics
    catches = fields.Integer(string='Catches')
    run_outs = fields.Integer(string='Run-Outs')
    stumping = fields.Integer(string='Stumpings')

    # Match Record
    match_played = fields.Integer(string='Match Played')
    inning_played = fields.Integer(string='Inning Played')
    c_matches_won = fields.Integer(string='Matches Won')
    matches_lost = fields.Integer(string='Matches Lost')
    matches_draw = fields.Integer(string='Matches Draw/Tied')

    # performance matrics
    man_of_the_match = fields.Integer(string='Player of the Match Awards')
    man_of_the_series = fields.Integer(string='Player of the Series Awards')

    # Football
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

    # Match Records
    matches_played = fields.Integer(string='Matches Played')
    matches_started = fields.Integer(string='Matches Started')
    f_matches_won = fields.Integer(string='Matches Won')
    goals_scored_in_wins = fields.Integer(string='Goals Scored in Wins')
    clean_sheets_in_wins = fields.Integer(string='Clean Sheets in Wins')

    # Match Statistics
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

    # Performance Matrics
    man_of_the_match_awards = fields.Integer(string='Man of the Match Awards')
    average_rating = fields.Float(string='Average Rating')
    distance_covered = fields.Float(string='Distance Covered (km)')
    sprint_speed = fields.Float(string='Sprint Speed (km/h)')
    aerial_duels_won = fields.Integer(string='Aerial Duels Won')




    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            rec.age = relativedelta(date.today(), rec.dob).years

    def action_complaint(self):
        return {
            'name': _('Complaint'),
            'view_mode': 'form',
            'res_model': 'student_complaint',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

    def action_paid(self):
        self.status = 'paid'

    def _sport_activity_data(self):
        self.ensure_one()  # Ensure this method is called on a single record
        return {
            'p_id' : self.id,
            'sport_name': self.sport_name,
            'player_name': self.name,
            'player_age': self.age,
            'player_gender': self.new_gender,
            'player_phone': self.phone,
            'c_team': self.c_team,
            'style': self.style,
            'total_run': self.total_run,
            'centuries': self.centuries,
            'half_centuries': self.half_centuries,
            'fours': self.fours,
            'sixes': self.sixes,
            'batting_average': self.batting_average,
            'wicket': self.wicket,
            'dot_balls': self.dot_balls,
            'bowling_average': self.bowling_average,
            'five_wicket': self.five_wicket,
            'catches': self.catches,
            'run_outs': self.run_outs,
            'stumping': self.stumping,
            'match_played': self.match_played,
            'inning_played': self.inning_played,
            'c_matches_won': self.c_matches_won,
            'matches_lost': self.matches_lost,
            'matches_draw': self.matches_draw,
            'man_of_the_match': self.man_of_the_match,
            'man_of_the_series': self.man_of_the_series,
            'f_team': self.f_team,
            'position': self.position,
            'matches_played': self.matches_played,
            'matches_started': self.matches_started,
            'f_matches_won': self.f_matches_won,
            'goals_scored_in_wins': self.goals_scored_in_wins,
            'clean_sheets_in_wins': self.clean_sheets_in_wins,
            'goals_scored': self.goals_scored,
            'assists': self.assists,
            'pass_completion_rate': self.pass_completion_rate,
            'shots_on_target': self.shots_on_target,
            'minutes_played': self.minutes_played,
            'possession_percentage': self.possession_percentage,
            'shots_on_goal': self.shots_on_goal,
            'passes_completed': self.passes_completed,
            'corners_taken': self.corners_taken,
            'tackles': self.tackles,
            'man_of_the_match_awards': self.man_of_the_match_awards,
            'average_rating': self.average_rating,
            'distance_covered': self.distance_covered,
            'sprint_speed': self.sprint_speed,
            'aerial_duels_won': self.aerial_duels_won,
        }

    @api.model
    def create(self, vals):
        res = super(Student, self).create(vals)
        data = res._sport_activity_data()
        self.env['sport.activity'].create(data)
        return res


    def write(self, vals):
        res = super(Student, self).write(vals)
        for student in self:
            sport_activity = self.env['sport.activity'].search([('p_id', '=', student.id)])
            if sport_activity:
                data = student._sport_activity_data()
                sport_activity.write(data)
        print("write >>>>>>>>>", res)
        return res

    def action_orm(self):

        students_id = self.env['res.partner'].search([('identity', '=', 'Student')])
        students_count = self.env['res.partner'].search_count([('identity', '=', 'Student')])
        print("Students ID", students_id)
        print("Students Count", students_count)

        read_students = self.env['res.partner'].search([('sport_name', '=', 'cricket')]).read(['name'])
        print("read sport students>>>>>>>>>.", read_students)

        browse_result = self.env['res.partner'].browse(100).read(['age'])
        print("browse result>>>>>>>>>>", browse_result)

        browse_students = self.env['res.partner'].browse([100,101])
        print("Mapped Students>>>>>>>>>>", browse_students.mapped('name'))

        # fetch_students = self.env['res.partner'].search_fetch([('sport_name', '=', 'cricket')], ['name'])
        # print("fetch students>>>>>>>>>>>>>>>>>>", fetch_students)

        print("self>>>>>>>>>>>", self)
        print("self env>>>>>>>>>>>", self.env)
        print("self lang>>>>>>>>>>>", self.env.lang)


        search_cricket_data = self.env['res.partner'].search([('sport_name', '=', 'cricket')])
        print("search cricket data >>>>", search_cricket_data.read(['name']))
        filtered_cricket_data = self.env['res.partner'].search([]).filtered_domain([('sport_name', '=', 'cricket')]).sorted(key=lambda s: s.id)
        print("filtered cricket data ", filtered_cricket_data)
        print("sorted by id filtered cricket data ", filtered_cricket_data.read(['name']))
        print("sorted by id mapped cricket data", filtered_cricket_data.mapped('name'))




































