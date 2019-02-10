{
    'name': 'EESTISOFT partner user assign',
    'version': '12.0.4.8',
    'author': 'EESTISOFT, ''Giulio Milani',
    'category': 'Productivity',
    'website': 'https://eestisoft.com',
    'sequence': 2,
    'summary': 'Adds group ',
    'description': """
Adds massive Salesperson on partners
	
Made with love.
    """,
    'images':['thumb.png'],
	'depends': ['base','contacts'],
    'data': ['views/ees_partner_user_assign.xml','views/ir.model.access.csv'],
    'installable': True,
    'application': True,
    'auto_install': False
}
