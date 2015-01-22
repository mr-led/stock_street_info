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

class stock_picking(osv.osv):
    _name = 'stock.picking'
    _inherit = 'stock.picking'

    _columns = {
	'street': fields.related('partner_id','street',type='char',relation='res.partner',size=128,string='Street',store=False,readonly=True),
	'city': fields.related('partner_id','city',type='char',relation='res.partner',size=128,string='City',store=False,readonly=True),
	'zip': fields.related('partner_id','zip',type='char',relation='res.partner',size=128,string='Zip',store=False,readonly=True),
	'nro_impreso': fields.char('Nro Impreso',size=24),
    }

stock_picking()


