# import os
# import shutil
 
# def organizar_downloads():
#     pasta_downloads = os.path.expanduser("Downloads")
 
#     destino_documentos = os.path.join(pasta_downloads, "documentos")
#     destino_imagens = os.path.join(pasta_downloads, "imagens")
#     destino_videos = os.path.join(pasta_downloads, "videos")
 
#     os.makedirs(destino_documentos, exist_ok=True)
#     os.makedirs(destino_imagens, exist_ok=True)
#     os.makedirs(destino_videos, exist_ok=True)
 
#     extensoes_documentos = [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"]
#     extensoes_imagens = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"]
#     extensoes_videos = [".mp4", ".avi", ".mov", ".mkv", ".wmv"]
 
#     for arquivo in os.listdir(pasta_downloads):
#         caminho_arquivo = os.path.join(pasta_downloads, arquivo)
 
#         if os.path.isfile(caminho_arquivo):
#             nome, extensao = os.path.splitext(arquivo)
 
#             if extensao.lower() in extensoes_documentos:
#                 shutil.move(caminho_arquivo, os.path.join(destino_documentos, arquivo))
#             elif extensao.lower() in extensoes_imagens:
#                 shutil.move(caminho_arquivo, os.path.join(destino_imagens, arquivo))
#             elif extensao.lower() in extensoes_videos:
#                 shutil.move(caminho_arquivo, os.path.join(destino_videos, arquivo))
 
# organizar_downloads()