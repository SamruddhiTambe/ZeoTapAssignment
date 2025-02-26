from django.shortcuts import render, get_object_or_404
from .models import Spreadsheet, Sheet, Cell
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def spreadsheet_list(request):
    """Display a list of all spreadsheets."""
    spreadsheets = Spreadsheet.objects.all()
    return render(request, "sheets/spreadsheet_list.html", {"spreadsheets": spreadsheets})

def sheet_detail(request, sheet_id):
    """Display a specific sheet with its cells."""
    sheet = get_object_or_404(Sheet, id=sheet_id)
    cells = Cell.objects.filter(sheet=sheet)
    return render(request, "sheets/sheet_detail.html", {"sheet": sheet, "cells": cells})

@csrf_exempt
def update_cell(request):
    """Update a cell's value via AJAX."""
    if request.method == "POST":
        cell_id = request.POST.get("cell_id")
        value = request.POST.get("value")

        cell = Cell.objects.get(id=cell_id)
        cell.value = value
        cell.save()

        return JsonResponse({"status": "success", "value": value})

