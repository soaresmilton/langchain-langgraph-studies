from pydantic import BaseModel, Field
from typing import List, Union

class BaseResponseStructure(BaseModel):
    """Job information scheme."""
    
    job_title: str = Field(description="Job title of the opportunity")
    job_description: str = Field(description="Job opportunity description from LinkedIn or corresponded website")
    company: str = Field(description="Company where the job is")
    url: str = Field(description="Teh URL  the opportunity")
    

class ListResponseStructure(BaseModel):
    """List all found jobs"""
    jobs_found: List[BaseResponseStructure] = Field(default_factory=list, description="List with all found jobs")