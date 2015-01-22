# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv

class account_invoice(osv.osv):
	_name = 'account.invoice'
	_inherit = 'account.invoice'


	def retrieve_picking_number(self, cr, uid, ids, field_name, arg, context=None):
		records = self.browse(cr, uid, ids)
		picking_obj = self.pool.get('stock.picking')
		res = {}
		for r in records:
			nro_remito = ''
			picking_ids = picking_obj.search(cr,uid,[('origin','=',r.origin)])
			for picking in picking_obj.browse(cr,uid,picking_ids):
				if picking.nro_impreso:
					nro_remito = nro_remito + picking.nro_impreso	
			res[r.id] = nro_remito
		return res

	_columns = {
		'nro_remito': fields.function(retrieve_picking_number, type = 'char', string = 'Nro. Remito'),
		}

account_invoice()
