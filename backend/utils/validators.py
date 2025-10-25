"""
Data validation utilities for real estate procurement
"""

def validate_budget(budget):
    """Validate project budget"""
    if not isinstance(budget, (int, float)):
        raise ValueError("Budget must be a number")
    if budget <= 0:
        raise ValueError("Budget must be positive")
    if budget > 10000000:  # 10 million
        raise ValueError("Budget exceeds maximum allowed")
    return True

def validate_project_requirements(requirements):
    """Validate project requirements list"""
    if not isinstance(requirements, list):
        raise ValueError("Requirements must be a list")
    if len(requirements) == 0:
        raise ValueError("At least one requirement is needed")
    return True

def validate_vendor_quote(quote_amount, vendor_type):
    """Validate vendor quotation"""
    if not isinstance(quote_amount, (int, float)):
        raise ValueError("Quote must be a number")
    
    # Different validation based on vendor type
    max_quotes = {
        'material_supplier': 500000,
        'contractor': 2000000,
        'consultant': 100000
    }
    
    max_amount = max_quotes.get(vendor_type, 1000000)
    if quote_amount > max_amount:
        raise ValueError(f"Quote exceeds maximum for {vendor_type}")
    
    return True
