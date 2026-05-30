"""
Tests for the strategy module.
"""

import pytest
from src.strategy import BaseStrategy


class MockStrategy(BaseStrategy):
    """Mock strategy for testing purposes."""
    
    def analyze(self, data):
        return {"signal": "buy", "data": data}
    
    def execute(self, signal):
        return signal.get("signal") == "buy"


def test_strategy_initialization():
    """Test strategy initialization."""
    strategy = MockStrategy()
    assert strategy.is_running is False
    assert strategy.config == {}


def test_strategy_start_stop():
    """Test strategy start and stop."""
    strategy = MockStrategy()
    strategy.start()
    assert strategy.is_running is True
    strategy.stop()
    assert strategy.is_running is False


def test_strategy_analyze():
    """Test strategy analysis."""
    strategy = MockStrategy()
    result = strategy.analyze({"price": 100})
    assert result["signal"] == "buy"


def test_strategy_execute():
    """Test strategy execution."""
    strategy = MockStrategy()
    assert strategy.execute({"signal": "buy"}) is True
    assert strategy.execute({"signal": "sell"}) is False
