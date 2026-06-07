from fastapi import APIRouter

router = APIRouter(prefix='/audit', tags=['audit'])

@router.post('')
def create_audit(payload: dict):
    url = payload.get('url')

    return {
        'url': url,
        'status': 'queued'
    }
