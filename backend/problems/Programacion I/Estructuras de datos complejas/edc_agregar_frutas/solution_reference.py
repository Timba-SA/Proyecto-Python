def main():
    """Agrega frutas al diccionario de precios"""
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    
    # Agregar las tres frutas
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    
    print(precios_frutas)

if __name__ == "__main__":
    main()
