def main():
    """Crea una lista con solo los nombres de las frutas"""
    precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}
    
    lista_frutas = list(precios_frutas.keys())
    
    print(lista_frutas)

if __name__ == "__main__":
    main()
