# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    reader_id = fields.Many2one('res.users', ondelete='set null', string="Reader", index=True )
    shelf_ids = fields.Many2one('library.shelf', string="Shelf", required=True)


class Shelf(models.Model):
    _name = 'library.shelf'

    name = fields.Char(string="Name of shelf", required=True)
    spaces = fields.Integer(string="Number of spaces", required=True)
    manager_id = fields.Many2one('res.partner', string="Manager")
    book_ids = fields.One2many('library.book', 'shelf_ids', string="Book")
    remaining_spaces = fields.Integer(string="Remaining spaces", compute = 'rem_spaces')

    @api.depends('spaces' , 'book_ids')
    def rem_spaces(self):
        for r in self:
            if not r.spaces:
                r.remaining_spaces = 0
            else:
                r.remaining_spaces = (r.spaces - len(r.book_ids))

    @api.onchange('spaces', 'book_ids')
    def verify_spaces(self):
        if self.spaces < 0:
            return {
                'warning': {
                    'title': "Incorrect 'spaces' value",
                    'message': "The number of spaces may not be negative",
                },
            }
        if len(self.book_ids) > self.spaces:
            return {
                'warning': {
                    'title': "Too many books",
                    'message': "This shelf cannot occupy all these books",
                },
            }




    
    

    