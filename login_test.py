from login import login
 
class TestLogin:

    correoTest = 'santiago@gmail.com'
    passwordTest = 'Pa$$@123456789'

    def setup_method(self):
        self.login = login()
    
    # =========================================================================
    # PRUEBAS PARA validar contraseña
    # =========================================================================

    def test_validar_password_camino_1_password_null(self):
        resultado, mensaje = self.login.validate_pass_correo("",self.correoTest)
        assert resultado == False
        assert "nula" in mensaje
    
    def test_validar_password_camino_2_no_longitud(self):
        resultado, mensaje = self.login.validate_pass_correo("Pass@1",self.correoTest)
        assert resultado == False
        assert "8" in mensaje

    def test_validar_password_camino_3_no_mayuscula(self):
        resultado, mensaje = self.login.validate_pass_correo("sin_numero123",self.correoTest)
        assert resultado == False
        assert "mayuscula" in mensaje
    
    def test_validar_password_camino_4_no_minuscula(self):
        resultado, mensaje = self.login.validate_pass_correo("PASSWORD123",self.correoTest)
        assert resultado == False
        assert "minuscula" in mensaje

    def test_validar_password_camino_5_no_numero(self):
        resultado, mensaje = self.login.validate_pass_correo("SIN_numero",self.correoTest)
        assert resultado == False
        assert "número" in mensaje    
    
    def test_validar_password_camino_6_no_caracter_especial(self):
        resultado, mensaje = self.login.validate_pass_correo("PASSWORD123apyth",self.correoTest)
        assert resultado == False
        assert "especial" in mensaje

    def test_validar_password_camino_7_contiene_usuario(self):
        resultado, mensaje = self.login.validate_pass_correo("santiagoGMG123#$",self.correoTest)
        assert resultado == False
        assert "usuario" in mensaje

    def test_validar_password_camino_8_password_valido(self):
        resultado, mensaje = self.login.validate_pass_correo("Pa$$@123456789",self.correoTest)
        assert resultado == True
        assert "Credenciales" in mensaje

    # =========================================================================
    # PRUEBAS PARA validar correo
    # =========================================================================
    
    def test_validar_correo_camino_1_nulo(self):
        resultado , mensaje = self.login.validate_pass_correo(self.passwordTest,"")
        assert resultado == False
        assert "nulo" in mensaje

    def test_validar_correo_camino_2_usaurio_no_mayor_a_5_caracteres(self):
        resultado,mensaje = self.login.validate_pass_correo(self.passwordTest,"SGMG@uacam.mx")
        assert resultado == False
        assert "usuario" in mensaje

    def test_validar_correo_camino_3_no_tiene_arroba(self):
        resultado,mensaje = self.login.validate_pass_correo(self.passwordTest,"santiago_uacam.mx")
        assert resultado == False
        assert "@" in mensaje
    def test_validar_correo_camino_4_no_tiene_dominio(self):
        resultado,mensaje = self.login.validate_pass_correo(self.passwordTest,"al064489@")
        assert resultado == False
        assert "dominio" in mensaje
    def test_validar_correo_camino_5_correo_valido(self):
        resultado,mensaje = self.login.validate_pass_correo(self.passwordTest,"al064489@uacam.mx")
        assert resultado == True
        assert "Credenciales" in mensaje

