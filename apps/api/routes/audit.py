from fastapi import APIRouter
from apps.api.agents.technical_agent import TechnicalAgent

router = APIRouter(prefix='/audit', tags=['audit'])

@router.post('')
def create_audit(payload: dict):
    url = payload.get('url')

    agent = TechnicalAgent()
    audit = agent.run(url)

    return {
        'url': url,
        'audit': audit
    }
