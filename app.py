from fastapi import Depends, FastAPI, Request, HTTPException
from starlette.middleware.sessions import SessionMiddleware
import uvicorn

app = FastAPI(title="Session Login", description="Utilisation des session pour la connection utilisateur")
app.add_middleware(SessionMiddleware, secret_key="votre_clé_secrète")

@app.post("/login")
def login(username: str, password: str, request: Request):
    
    request.session["username"] = username
    request.session["password"] = password
    
    return "login succesfully !"


def get_current_user(request: Request):
    username = request.session.get("username")
    print(username)
    if username is None:
        raise HTTPException(status_code=401, detail="Authentification requise")
    return True


@app.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    # Cette route est protégée et nécessite une authentification valide
    return {"message": "Vous avez accès à cette route protégée."}



if __name__ == "__main__" :
    uvicorn.run("app:app", reload=True)