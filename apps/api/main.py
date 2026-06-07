from fastapi import FastAPI
from apps.api.routes.audit import router as audit_router

app = FastAPI(title='PropRank API', version='0.1.0')

app.include_router(audit_router)

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.get('/')
def root():
    return {'name': 'PropRank', 'version': '0.1.0'}
