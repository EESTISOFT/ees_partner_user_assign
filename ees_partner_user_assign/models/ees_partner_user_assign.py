# -*- coding: utf-8 -*-
# © 2018 Giulio Milani
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
	

from odoo import api, fields, models
from datetime import datetime

class ees_partner_user_assign_multi_action(models.TransientModel):
	_name = 'ees_partner_user_assign.multi_saleperson_action'
	user = fields.Many2one('res.users',string="User")
	partners = fields.Many2many('res.partner', string="Partners")
	@api.depends('user','partners')
	def do_tag_all(self):
		if self.user:
			if self.partners:
				for p in self.partners:
					p.user_id=self.user
					
	@api.depends('user','partners')
	def do_untag_all(self):
			if self.partners:
				for p in self.partners:
					p.user_id=False
				
	
	@api.multi 
	def create_wizard(self): 
		wizard_id = self.create({})
		wizard_id.partners = self.env.context.get('active_ids', []) or []
		return { 
			'name': 'Purchase Wizard', 
			'view_type': 'form', 
			'view_mode': 'form', 
			'res_model': 'ees_partner_user_assign.multi_saleperson_action', 
			'res_id': wizard_id.id, 
			'type': 'ir.actions.act_window', 
			'target': 'new', 
			'context': self.env.context 
		}