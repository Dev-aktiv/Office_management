{
    'name': 'Pharmacy management',
    'version': '15.0.0.1.0',
    'summary': '',
    'author': 'Aktiv-Software',
    'website': '',
    'sequence': 10,
    'license': 'LGPL-3',
    'description': """
    """,
    'category': 'Management/Pharmacy management',
    'website': '',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/employee_manage_views.xml",
        "views/product_details_views.xml",
        "views/product_types_views.xml",
        "views/products_views.xml",
        "views/skills_views.xml",
        "views/product_company_views.xml"
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
    },
}