from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from ..database import Base

class Course(Base):
    __tablename__ = "courses"
    __table_args__ = (UniqueConstraint("program", "course_code", name="uq_program_course_code"),)
    id = Column(Integer, primary_key=True, index=True)
    program = Column(String, nullable=False)                  # jaise BSCS
    course_code = Column(String, nullable=False)              # space ke bina, jaise CSC1101
    course_name = Column(String, nullable=False) #FOP ,OOp
    credit_hours = Column(Integer, nullable=False) #3 ,2, OR 1
    course_type = Column(String, nullable=False)              # Core ya Elective
    semester_no = Column(Integer, nullable=False)             # 1 se 8
    prerequisite_id = Column(Integer, ForeignKey("courses.id"), nullable=True)  # self FK self join