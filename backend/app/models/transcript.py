from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base

class Transcript(Base):
    __tablename__ = "transcripts"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    grade = Column(String, nullable=False)            # jaise A-, B+, F
    status = Column(String, nullable=False)           # Passed ya Failed
    semester_taken = Column(String, nullable=False)   # jaise "Fall 2022"