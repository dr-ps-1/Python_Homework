import pytest
from db import SubjectTable

DB_URL = "postgresql://postgres:DxM39Y$@localhost:5432/QA"


@pytest.fixture
def db():
    return SubjectTable(DB_URL)


@pytest.fixture
def unique_subject_title():
    import time
    return f"Автотест Предмет {int(time.time() * 1000)}"
