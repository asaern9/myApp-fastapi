from fastapi import APIRouter, File, UploadFile

router = APIRouter()


@router.post('/file')
async def add_file(file: UploadFile):
    content = file.file.read()
    file_details = {
        "filename": file.filename,
        "filetype": file.content_type,
        "content": content
    }
    return file_details

