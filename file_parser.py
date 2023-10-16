import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []

AVI_VIDEO=  []
MP4_VIDEO=[]
MOV_VIDEO=[]
MKV_VIDEO=[]

DOC_DOCUMENTS=[]
DOCX_DOCUMENTS=[]
TXT_DOCUMENTS=[]
PDF_DOCUMENTS=[]
XLSX_DOCUMENTS=[]
PPTX_DOCUMENTS=[]

MP3_AUDIO = []
OGG_AUDIO=[]
WAV_AUDIO=[]

ZIP_ARCHIVES = []
GZ_ARCHIVES=[]
TAR_ARCHIVES=[]

AMR_AUDIO=[]
MY_OTHER = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    
    'AVI': AVI_VIDEO, 
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'MP3': MP3_AUDIO,
    
    'OGG':OGG_AUDIO,
    'WAV':WAV_AUDIO,
    'AMR':AMR_AUDIO,
    
    'DOC': DOC_DOCUMENTS,
    'DOCX':DOCX_DOCUMENTS,
    'PDF':PDF_DOCUMENTS,
    'TXT':TXT_DOCUMENTS,
    'XLSX':XLSX_DOCUMENTS,
    'PPTX':PPTX_DOCUMENTS,
    
    'ZIP': ZIP_ARCHIVES,
    'GZ':GZ_ARCHIVES,
    'TAR':TAR_ARCHIVES,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()  # suffix[1:] -> .jpg -> jpg

def scan(folder: Path):
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():  # перевіряємо чи обєкт папка
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue
        

        # Робота з файлом
        extension = get_extension(item.name)  # беремо розширення файлу
        full_name = folder / item.name  # беремо повний шлях до файлу

        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                temp=REGISTER_EXTENSION[extension]
                temp.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)  # .mp4, .mov, .avi
                MY_OTHER.append(full_name)

if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    
    print(f'AUDIO mp3: {MP3_AUDIO}')
    print(f'AUDIO OGG:{OGG_AUDIO}')
    print(f'AUDIO WAV:{WAV_AUDIO}')
    print(f'AUDIO AMR:{AMR_AUDIO}')
    print(f'Video avi: {AVI_VIDEO}')
    
    print(f'video MP4:{MP4_VIDEO}')
    print(f'video MOV:{MOV_VIDEO}')
    print(f'video MKV: {MKV_VIDEO}')
    
    print(f'DOCUMENTS DOC:{DOC_DOCUMENTS}')
    print(f'DOCUMENTS DOCX:{DOCX_DOCUMENTS}')
    print(f'DOCUMENTS TXT:{TXT_DOCUMENTS}')
    print(f'DOCUMENTS PDF:{PDF_DOCUMENTS}')
    print(f'DOCUMENTS XLSX:{XLSX_DOCUMENTS}')
    print(f'DOCUMENTS PPTX:{PPTX_DOCUMENTS}')

    print(f'Archives zip: {ZIP_ARCHIVES}')
    print(f"Archives GZ:{GZ_ARCHIVES}")
    print(f'Archives TAR:{TAR_ARCHIVES}')
    
    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')