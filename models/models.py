# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    reader_id = fields.Many2one('res.users', ondelete='set null', string="Reader", index=True )


class Shelf(models.Model):
    _name = 'library.shelf'

    name = fields.Char(string="Title", required=True)
    spaces = fields.Integer(string="Number of spaces")
    manager_id = fields.Many2one('res.partner', string="Manager")
    book_id = fields.Many2one('library.book', string="Book", ondelete="cascade", required=True)