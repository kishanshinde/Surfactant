import uuid
from dataclasses import dataclass, field
from typing import List, Optional

from ._file import File
from ._provenance import AnalysisDataProvenance

# pylint: disable=too-many-instance-attributes


@dataclass
class AnalysisData:
    UUID: str = field(default_factory=uuid.uuid4)
    origin: str = None
    testName: str = None
    testVersion: str = None
    specificEnvironment: Optional[str] = None
    files: Optional[List[File]] = None
    linksToKnownVulnerabilities: Optional[str] = None
    provenance: Optional[List[AnalysisDataProvenance]] = None
