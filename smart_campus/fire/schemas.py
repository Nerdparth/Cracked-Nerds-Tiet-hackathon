from ninja import Schema


class FireSensorDataSchema(Schema):
    sensor_id: int
    fire_hazard_level: int  
    smoke_level: float  
    temp_level: float  


class ManualFireReportSchema(Schema):
    location: str  
