from ninja import Schema


class GarbageSensorRequestSchema(Schema):
    sensor_id: int  


class UpdateStatusSchema(Schema):
    sensor_id: int
    status: str  


class GarbageSensorDataSchema(Schema):
    sensor_id: int
    location: str
    status: str
