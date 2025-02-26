from django.db import models

class Spreadsheet(models.Model):
    """Model to store different spreadsheets"""
    name = models.CharField(max_length=255)  # Name of the spreadsheet
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of last update

    def __str__(self):
        return self.name


class Sheet(models.Model):
    """Model to store different sheets inside a spreadsheet"""
    spreadsheet = models.ForeignKey(Spreadsheet, on_delete=models.CASCADE, related_name="sheets")
    name = models.CharField(max_length=255, default="Sheet1")

    def __str__(self):
        return f"{self.spreadsheet.name} - {self.name}"


class Row(models.Model):
    """Model to store rows in a sheet"""
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE, related_name="rows")
    index = models.PositiveIntegerField()  # Row index

    def __str__(self):
        return f"Row {self.index} in {self.sheet}"


class Column(models.Model):
    """Model to store columns in a sheet"""
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE, related_name="columns")
    name = models.CharField(max_length=10)  # Column name like A, B, C...
    index = models.PositiveIntegerField()  # Column index

    def __str__(self):
        return f"Column {self.name} in {self.sheet}"


class Cell(models.Model):
    """Model to store cell data"""
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE, related_name="cells")
    row = models.ForeignKey(Row, on_delete=models.CASCADE, related_name="cells")
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="cells")
    value = models.TextField(blank=True, null=True)  # Can store text, numbers, formulas
    formula = models.TextField(blank=True, null=True)  # Stores the formula
    is_formula = models.BooleanField(default=False)  # Check if the cell contains a formula

    def __str__(self):
        return f"Cell {self.column.name}{self.row.index} in {self.sheet}"


class CellFormat(models.Model):
    """Model to store formatting of cells"""
    cell = models.OneToOneField(Cell, on_delete=models.CASCADE, related_name="format")
    bold = models.BooleanField(default=False)
    italic = models.BooleanField(default=False)
    font_size = models.PositiveIntegerField(default=12)
    font_color = models.CharField(max_length=20, default="black")  # Example: "red", "blue", "#FF5733"

    def __str__(self):
        return f"Format for {self.cell}"


class DataValidation(models.Model):
    """Model to store data validation rules"""
    cell = models.OneToOneField(Cell, on_delete=models.CASCADE, related_name="validation")
    validation_type = models.CharField(max_length=50, choices=[
        ("NUMBER_ONLY", "Number Only"),
        ("TEXT_ONLY", "Text Only"),
        ("DATE_ONLY", "Date Only"),
    ])
    error_message = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Validation for {self.cell}"
