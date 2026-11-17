# -*- coding: utf-8 -*-
"""
Vercel Serverless Function entry point for Minh An AI Agent.
"""
import sys
import os

# Add parent directory to path so imports work on Vercel
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app import MinhAnApiHandler

class handler(MinhAnApiHandler):
    """
    Vercel serverless entry point class.
    Vercel automatically instantiates this class for inbound requests.
    """
    pass

