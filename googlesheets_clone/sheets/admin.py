from django.contrib import admin

# Registering models 
from .models import Spreadsheet, Sheet, Row, Column, Cell, CellFormat, DataValidation

admin.site.register(Spreadsheet)
admin.site.register(Sheet)
admin.site.register(Row)
admin.site.register(Column)
admin.site.register(Cell)
admin.site.register(CellFormat)
admin.site.register(DataValidation)
