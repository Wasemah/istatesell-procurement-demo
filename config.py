"""
Configuration settings for iStateSell Procurement System
"""

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///istatesell.db'
    DEBUG = os.environ.get('DEBUG', False)
    
    # Real estate specific settings
    MAX_PROJECT_BUDGET = 10000000  # 10 million
    DEFAULT_CURRENCY = 'USD'
