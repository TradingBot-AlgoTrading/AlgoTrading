"""
Configuration module for AlgoTrading.
"""

# Default configuration
DEFAULT_CONFIG = {
    "api_key": "",
    "api_secret": "",
    "trading_pair": "BTC/USDT",
    "strategy": "default",
    "risk_management": {
        "max_position_size": 0.1,
        "stop_loss_pct": 0.02,
        "take_profit_pct": 0.04
    }
}


def load_config(config_path: str = None) -> dict:
    """
    Load configuration from file or return defaults.
    
    Args:
        config_path: Path to configuration file.
        
    Returns:
        Configuration dictionary.
    """
    config = DEFAULT_CONFIG.copy()
    
    if config_path:
        import json
        import os
        
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                user_config = json.load(f)
                config.update(user_config)
    
    return config
