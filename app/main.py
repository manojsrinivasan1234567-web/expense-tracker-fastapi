
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import models, schemas


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Expense Tracker API",
    description="Expense management with PostgreSQL",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running"}


# CREATE
@app.post(
    "/expenses",
    response_model=schemas.ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
):
    new_expense = models.Expense(**expense.model_dump())

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


# READ ALL
@app.get("/expenses", response_model=list[schemas.ExpenseResponse])
def get_expenses(db: Session = Depends(get_db)):
    return (
        db.query(models.Expense)
        .order_by(models.Expense.id.desc())
        .all()
    )


# READ TOTAL
@app.get("/expenses/summary")
def expense_summary(db: Session = Depends(get_db)):
    expenses = db.query(models.Expense).all()

    total = sum(item.amount for item in expenses)

    return {
        "total_expenses": round(total, 2),
        "number_of_expenses": len(expenses),
    }


# READ ONE
@app.get(
    "/expenses/{expense_id}",
    response_model=schemas.ExpenseResponse,
)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = (
        db.query(models.Expense)
        .filter(models.Expense.id == expense_id)
        .first()
    )

    if expense is None:
        raise HTTPException(404, "Expense not found")

    return expense


# UPDATE
@app.patch(
    "/expenses/{expense_id}",
    response_model=schemas.ExpenseResponse,
)
def update_expense(
    expense_id: int,
    updates: schemas.ExpenseUpdate,
    db: Session = Depends(get_db),
):
    expense = (
        db.query(models.Expense)
        .filter(models.Expense.id == expense_id)
        .first()
    )

    if expense is None:
        raise HTTPException(404, "Expense not found")

    changes = updates.model_dump(exclude_unset=True)

    required_fields = {"title", "amount", "category", "expense_date"}

    for field in required_fields:
        if field in changes and changes[field] is None:
            raise HTTPException(422, f"{field} cannot be null")

    for field, value in changes.items():
        setattr(expense, field, value)

    db.commit()
    db.refresh(expense)

    return expense


# DELETE
@app.delete(
    "/expenses/{expense_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
):
    expense = (
        db.query(models.Expense)
        .filter(models.Expense.id == expense_id)
        .first()
    )

    if expense is None:
        raise HTTPException(404, "Expense not found")

    db.delete(expense)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
