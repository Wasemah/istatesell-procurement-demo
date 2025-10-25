"""
Unit tests for iStateSell models
"""

import pytest
from backend.cms_logic import RealEstateCMS
from backend.utils.validators import validate_budget, validate_project_requirements

class TestRealEstateCMS:
    def setup_method(self):
        self.cms = RealEstateCMS()
    
    def test_add_project(self):
        project = self.cms.add_project("Test Tower", 500000, ["cement", "steel"])
        assert project['name'] == "Test Tower"
        assert project['budget'] == 500000
    
    def test_budget_validation(self):
        assert validate_budget(100000) == True
        
        with pytest.raises(ValueError):
            validate_budget(-1000)
    
    def test_requirements_validation(self):
        assert validate_project_requirements(["material", "labor"]) == True
        
        with pytest.raises(ValueError):
            validate_project_requirements([])

if __name__ == "__main__":
    pytest.main()
