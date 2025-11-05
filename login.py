import re

class login:

    def validate_pass_correo(self,password,email):
        user = email.split("@")[0]
        password = password.strip()
        email = email.strip()
        
        if not email:
            return False, "Tu correo no puede ser nulo"
        if len(user) < 5:
            return False, "Tu usuario debe tener mas de 5 caracteres"
        if not "@" in email:
            return False, "Tu correo no tiene @"
        if "@" in email and not email.split("@")[1]:
            return False, "Tu correo no tiene dominio"
        
        if not password:
            return False, "Tu contraseña no puede ser nula "
        if len(password) < 8:
            return False,"Tu contraseña debe tener al menos 8 caracteres"
        if not (re.search("[A-Z]", password)):
            return False,"Tu contraseña necesita al menos una mayuscula"
        if not(re.search("[a-z]", password)):
            return False,"Tu contraseña necesita al menos una minuscula"
        if not (re.search("[0-9]", password)):
            return False,"Tu contraseña necesita al menos un número"
        if not re.search(r"[^A-Za-z0-9]", password):
            return False,"Tu contraseña necesita al menos un caracter especial"
        if user in password:
            return False, "Tu contraseña no debe contener tu usuario"
           
        return True, "Credenciales validas"
