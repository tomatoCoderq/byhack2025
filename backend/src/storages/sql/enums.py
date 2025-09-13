import enum



class StorySessionStatus(str, enum.Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    
# status = mapped_column(SQLEnum(StorySessionStatus, name="storysessionstatus"))
