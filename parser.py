from pydantic import BaseModel
from typing import List


class LearningPhase(BaseModel):
    title: str
    topics: List[str]
    outcome: str


class LearningPath(BaseModel):
    key_topics: List[str]
    learning_goal_summary: str
    learning_phases: List[LearningPhase]
    recommended_resources: List[str]
    youtube_channels: List[str]
    recommended_projects: List[str]