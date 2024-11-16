from ninja import Schema


class ScheduleEntrySchema(Schema):
    day: str  
    time: str  
    subject: str  


class ScheduleListSchema(Schema):
    day: str
    time: str
    subject: str
