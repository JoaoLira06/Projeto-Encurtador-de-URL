from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.utils import generate_short_code

router = APIRouter()

@router.post("/shorten", response_model=schemas.URLResponse, status_code=201)

def shorten_url(playload: schemas.URLCreate, db: Session = Depends(get_db)):
    for _ in range(5):
        code = generate_short_code()
        exists = db.query(models.URL).filter(models.URL.short_code == code ).first()
        if not exists:
            break
        else:
            raise HTTPException(status_code=500, detail = "Não foi possivel gerar o código único.")

        url_obj = models.URL(
            original_url=str(payload.original_url),
            short_code=code
        )
        db.add(url_obj)
        db.commit()
        db.refresh(url_obj)

        return schemas.URLResponse(
            short_code=url_obj.short_code,
            original_url=url_obj.original_url,
            short_code=f"http://localhost:8000/{url_obj.short_code}"
        )