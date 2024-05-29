{
    'name': 'School Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'A simple school management system for managing students, teachers, and classes.',
    'author': 'Brijesh Patel',
    'depends': ['base','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/class_view.xml',



    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
