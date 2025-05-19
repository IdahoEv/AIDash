from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..models.paper import Paper, PaperCreate
from ..models.database import get_db, DBPaper

router = APIRouter()

@router.post("/papers/", response_model=Paper)
def create_paper(paper: PaperCreate, db: Session = Depends(get_db)):
    db_paper = DBPaper(
        title=paper.title,
        authors=paper.authors,
        abstract=paper.abstract,
        categories=paper.categories,
        url=paper.url,
        doi=paper.doi
    )
    db.add(db_paper)
    db.commit()
    db.refresh(db_paper)
    return db_paper

@router.get("/papers/", response_model=List[Paper])
def read_papers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    papers = db.query(DBPaper).offset(skip).limit(limit).all()
    return papers

@router.get("/papers/{paper_id}", response_model=Paper)
def read_paper(paper_id: int, db: Session = Depends(get_db)):
    paper = db.query(DBPaper).filter(DBPaper.id == paper_id).first()
    if paper is None:
        raise HTTPException(status_code=404, detail="Paper not found")
    return paper

@router.put("/papers/{paper_id}", response_model=Paper)
def update_paper(paper_id: int, paper: PaperCreate, db: Session = Depends(get_db)):
    db_paper = db.query(DBPaper).filter(DBPaper.id == paper_id).first()
    if db_paper is None:
        raise HTTPException(status_code=404, detail="Paper not found")
    
    for key, value in paper.dict().items():
        setattr(db_paper, key, value)
    
    db.commit()
    db.refresh(db_paper)
    return db_paper

@router.delete("/papers/{paper_id}")
def delete_paper(paper_id: int, db: Session = Depends(get_db)):
    paper = db.query(DBPaper).filter(DBPaper.id == paper_id).first()
    if paper is None:
        raise HTTPException(status_code=404, detail="Paper not found")
    
    db.delete(paper)
    db.commit()
    return {"message": "Paper deleted successfully"} 