# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

class Shelf(models.Model):
    _name = 'library.shelf'

    name = fields.Char(string="Title", required=True)
    spaces = fields.Integer(string="Number of spaces")