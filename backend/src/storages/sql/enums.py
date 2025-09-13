import enum
import sqlmodel


class StorySessionStatus(str, enum.Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


story_session_status_enum = sqlmodel.Enum(
    StorySessionStatus,
    name="storysessionstatus",
    create_type=False
)

# status: Mapped[StorySessionStatus] = mapped_column(
#     story_session_status_enum,
#     nullable=False
# )
# status = mapped_column(SQLEnum(StorySessionStatus, name="storysessionstatus"))
