"""
Módulo para coleta de dados multimodais (áudio e vídeo) para documentação linguística.
"""

from voxlingua.data_collection.audio_capture import AudioCapture
from voxlingua.data_collection.visual_capture import VisualCapture
from voxlingua.data_collection.multimodal_sync import MultimodalCapture

__all__ = ['AudioCapture', 'VisualCapture', 'MultimodalCapture']
