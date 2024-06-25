from typing import Protocol, Self

import copy




class DocumentPrototype(Protocol):
    def clone(self) -> Self: ...


class FinancialReport(DocumentPrototype):
    def __init__(self, title, content, charts):
        self.title = title
        self.content = content
        self.charts = charts
    
    def clone(self) -> Self:
        return copy.deepcopy(self)
    
    def __str__(self):
        charts_str = ', '.join(self.charts)
        return f"Title: {self.title}\nContent: {self.content}\nCharts: {charts_str}"


original_report = FinancialReport(
    title="Monthly Financial Report",
    content="This is the financial report for the month.",
    charts=["Revenue Chart", "Expense Chart", "Profit Chart"]
)

print("Original Report:")
print(original_report)


cloned_report = original_report.clone()
cloned_report.title = "Monthly Financial Report - June"
cloned_report.content = "This is the financial report for June."

print("\nCloned Report:")
print(cloned_report)
