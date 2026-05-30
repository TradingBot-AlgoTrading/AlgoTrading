"""
Base Strategy Module

This module provides the base class for all trading strategies.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
import logging

logger = logging.getLogger(__name__)


class BaseStrategy(ABC):
    """
    Abstract base class for trading strategies.
    
    All trading strategies should inherit from this class and implement
    the required methods.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the strategy.
        
        Args:
            config: Configuration dictionary for the strategy.
        """
        self.config = config or {}
        self.is_running = False
        logger.info(f"Initializing {self.__class__.__name__}")
    
    @abstractmethod
    def analyze(self, data: Any) -> Any:
        """
        Analyze market data and generate trading signals.
        
        Args:
            data: Market data to analyze.
            
        Returns:
            Trading signal or analysis result.
        """
        pass
    
    @abstractmethod
    def execute(self, signal: Any) -> bool:
        """
        Execute a trade based on the signal.
        
        Args:
            signal: Trading signal from analyze().
            
        Returns:
            True if trade was executed successfully, False otherwise.
        """
        pass
    
    def start(self):
        """Start the strategy."""
        self.is_running = True
        logger.info(f"Strategy {self.__class__.__name__} started")
    
    def stop(self):
        """Stop the strategy."""
        self.is_running = False
        logger.info(f"Strategy {self.__class__.__name__} stopped")
