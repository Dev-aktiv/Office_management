{
    'name': 'Office Management',
    'version': '15.0.0.1.0',
    'summary': '',
    'author': 'Aktiv-Software',
    'website': '',
    'sequence': 10,
    'license': 'LGPL-3',
    'description': """
    """,
    'category': 'Management/office_management',
    'website': '',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/employee_info_views.xml",
        "views/attendance_info_views.xml"
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
    },
}