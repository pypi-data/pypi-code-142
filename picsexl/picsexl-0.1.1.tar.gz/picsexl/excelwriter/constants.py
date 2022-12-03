from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Font, PatternFill

DECLINED_EVENT_FONT = Font(size=11, bold=False, color="9C0103")
DECLINED_EVENT_FILL = PatternFill(
    start_color="FFC7CE", end_color="FFC7CE", fill_type="solid"
)
DECLINED_EVENT_RULE = FormulaRule(
    formula=['$E1="DECLINED"'], fill=DECLINED_EVENT_FILL, font=DECLINED_EVENT_FONT
)
