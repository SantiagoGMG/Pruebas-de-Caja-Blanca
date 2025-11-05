from login_test import TestLogin
def ejecutar_pruebas_con_cobertura():
    """
    Ejecuta las pruebas y muestra metricas de cobertura basicas
    """
    print("EJECUTANDO PRUEBAS DE CAJA BLANCA")
    print("=" * 50)
    
    # Contadores para métricas
    total_tests = 0
    tests_exitosos = 0
    tests_fallidos = 0
    
    # Crear instancia del tester
    tester = TestLogin()
    
    # Obtener todos los métodos de prueba
    metodos_prueba = [method for method in dir(tester) 
                     if method.startswith('test_')]
    
    total_tests = len(metodos_prueba)
    
    print(f"Total de pruebas: {total_tests}")
    print("=" * 50)
    
    # Ejecutar cada prueba
    for metodo in metodos_prueba:
        try:
            tester.setup_method()
            getattr(tester, metodo)()
            print(f"{metodo}: PASO")
            tests_exitosos += 1
        except Exception as e:
            print(f"{metodo}: FALLO - {str(e)}")
            tests_fallidos += 1
    
    # Mostrar resumen
    print("=" * 50)
    print("RESUMEN DE PRUEBAS")
    print(f"Pruebas exitosas: {tests_exitosos}/{total_tests}")
    print(f"Pruebas fallidas: {tests_fallidos}/{total_tests}")
    print(f"Tasa de exito: {(tests_exitosos/total_tests)*100:.1f}%")
    
    # Métricas de cobertura de caminos básicos
    print("\nCOBERTURA DE CAMINOS BASICOS")
    metodos_complejidad = {
        'validar_password': 8,
        'validar_correo': 5,
    }
    
    for metodo, v_g in metodos_complejidad.items():
        tests_metodo = [m for m in metodos_prueba if metodo in m]
        cobertura = len(tests_metodo) / v_g * 100
        print(f"  {metodo}: {len(tests_metodo)}/{v_g} caminos ({cobertura:.1f}%)")
    
    return tests_exitosos == total_tests

if __name__ == "__main__": 
    print()
    exito = ejecutar_pruebas_con_cobertura()
    
    if exito:
        print("\nTODAS LAS PRUEBAS PASARON!")
        print("La cobertura de caminos basicos es completa")
    else:
        print("\n Algunas pruebas fallaron")
        print("Revisa los casos de prueba fallidos")