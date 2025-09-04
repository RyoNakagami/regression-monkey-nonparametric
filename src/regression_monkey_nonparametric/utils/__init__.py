# Expose dataset config at the package level
from .setup import git_path_setting
from .dataset import DATASET_CONFIG

__all__ = ["git_path_setting", "DATASET_CONFIG"]
