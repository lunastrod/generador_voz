# generador_voz

# Instalación en máquina nueva
 
## Requisitos previos
- Python 3.10 (desde python.org, no Microsoft Store)
- NVIDIA GPU con drivers actualizados
- Microsoft C++ Build Tools (con "Desktop development with C++")
## Pasos
 
```bash
# 0. Descargar RVC1006Nvidia
https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/RVC1006Nvidia.7z

# 1. Crear entorno virtual con Python 3.10
py -3.10 -m venv venv
.\venv\Scripts\Activate.ps1
 
# 2. Instalar PyTorch con CUDA 12.4
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
 
# 3. Instalar el resto de dependencias
pip install -r requirements_funciona.txt
```
 
## Ejecutar
 
```bash
venv\Scripts\activate
cd RVC1006Nvidia
python infer-web.py
```
 
Se abre la WebUI en http://localhost:7865
 
## Notas
- Ejecutar siempre desde dentro de `RVC1006Nvidia/`, no desde el directorio padre
- GPU detectada: RTX 3050 6GB — funciona con `is_half:True, device:cuda:0`


C:\Astrod\Programacion\generador_voz\Input\SOLOMIL0.WAV

C:\Astrod\Programacion\generador_voz\Output\SOLOMIL0.WAV