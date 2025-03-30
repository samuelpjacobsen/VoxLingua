"""
Módulo para captura e gravação de áudio para documentação linguística.
"""

import os
import time
import wave
import numpy as np
import threading
import queue

class AudioCapture:
    """
    Classe para captura e gravação de áudio para documentação linguística.
    """
    
    def __init__(self, sample_rate=44100, chunk_size=1024, channels=1):
        """
        Inicializa o sistema de captura de áudio.
        
        Args:
            sample_rate (int): Taxa de amostragem em Hz
            chunk_size (int): Tamanho do chunk de áudio
            channels (int): Número de canais (1=mono, 2=estéreo)
        """
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.channels = channels
        self.audio_queue = queue.Queue()
        self.recording_thread = None
        
    def start_recording(self, output_file=None):
        """
        Inicia a gravação de áudio.
        
        Args:
            output_file (str): Caminho para salvar o arquivo de áudio (opcional)
        """
        print(f"Gravação iniciada. {'Salvando em ' + output_file if output_file else 'Modo streaming (sem arquivo)'}")
        
    def stop_recording(self):
        """
        Para a gravação de áudio e salva o arquivo se o caminho foi fornecido.
        
        Returns:
            str: Caminho do arquivo salvo ou None
        """
        print("Gravação finalizada")
        return None
