"""
Módulo para sincronização multimodal de áudio e vídeo para documentação linguística.
"""

from datetime import datetime
from voxlingua.data_collection.audio_capture import AudioCapture
from voxlingua.data_collection.visual_capture import VisualCapture

class MultimodalCapture:
    """
    Classe para captura sincronizada de áudio e vídeo.
    """
    
    def __init__(self, camera_id=0, resolution=(640, 480), fps=30, sample_rate=44100):
        """
        Inicializa o sistema de captura multimodal.
        
        Args:
            camera_id (int): ID da câmera a ser usada
            resolution (tuple): Resolução da captura de vídeo
            fps (int): Frames por segundo para o vídeo
            sample_rate (int): Taxa de amostragem do áudio (Hz)
        """
        self.audio_capture = AudioCapture(sample_rate=sample_rate)
        self.visual_capture = VisualCapture(camera_id=camera_id, resolution=resolution, fps=fps)
        self.session_id = None
        
    def start_capture(self, output_dir=None, session_name=None):
        """
        Inicia a captura sincronizada de áudio e vídeo.
        
        Args:
            output_dir (str): Diretório onde os arquivos serão salvos
            session_name (str): Nome da sessão
            
        Returns:
            str: ID da sessão criada
        """
        # Gerar ID de sessão
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.session_id = session_name if session_name else f"session_{timestamp}"
        
        # Iniciar capturas individuais
        self.audio_capture.start_recording()
        self.visual_capture.start_capture()
        
        print(f"Captura multimodal iniciada. ID da sessão: {self.session_id}")
        return self.session_id
    
    def stop_capture(self):
        """
        Para a captura sincronizada e salva os arquivos.
        
        Returns:
            dict: Dicionário com os caminhos dos arquivos salvos
        """
        # Parar capturas individuais
        self.audio_capture.stop_recording()
        self.visual_capture.stop_capture()
        
        print(f"Captura multimodal finalizada. ID da sessão: {self.session_id}")
        return {'session_id': self.session_id}
