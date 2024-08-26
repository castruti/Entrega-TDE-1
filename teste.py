# Gabriel Calado da Silva Castro

# Este programa realiza operações entre conjuntos, como união, interseção, diferença e produto cartesiano,
# a partir de dados fornecidos em um arquivo de texto.

def process_operations(file_name):
    with open(file_name, 'r') as file:
        num_operations = int(file.readline().strip())
        results = []

        for _ in range(num_operations):
            operation = file.readline().strip()
            set1 = file.readline().strip().split(', ')
            set2 = file.readline().strip().split(', ')

            if operation == 'U':
                result = sorted(set(set1).union(set(set2)), key=lambda x: (set1 + set2).index(x))
                operation_str = "União"
            elif operation == 'I':
                result = sorted(set(set1).intersection(set(set2)), key=lambda x: (set1 + set2).index(x))
                operation_str = "Interseção"
            elif operation == 'D':
                result = sorted(set(set1).difference(set(set2)), key=lambda x: set1.index(x))
                operation_str = "Diferença"
            elif operation == 'C':
                result = [(a, b) for a in set1 for b in set2]
                operation_str = "Produto cartesiano"
                result = [f'({a}, {b})' for a, b in result]

            result_str = ', '.join(result)
            results.append(f"{operation_str}: conjunto 1 {{{', '.join(set1)}}}, conjunto 2 {{{', '.join(set2)}}}. Resultado: {{{result_str}}}")

    return results

def main():
    file_name = r'C:\Users\castruti\OneDrive\Área de Trabalho\Faculdade\Nova pasta\input3.txt'
    results = process_operations(file_name)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
