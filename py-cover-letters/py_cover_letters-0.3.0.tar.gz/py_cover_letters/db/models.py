from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class CoverLetter(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str
    position_name: str
    greeting: Optional[str]
    to_email: Optional[str]
    cover_template: Optional[str] = Field(description='Name of the cover letter template to use.')
    date_sent_via_email: Optional[datetime]
    date_generated: Optional[datetime]
    description: Optional[str]
    delete: bool = Field(default=False, description='Delete from the excel on next synchronization')

    def get_context(self):
        excluded_fields = {'id', 'greeting', 'to_email', 'cover_template', 'date_sent_email',
                           'date_generated', 'description', 'delete'}
        context = self.dict(exclude=excluded_fields)
        return context
