from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return ((n, a))

numeros = [10, 20, 30, 40]

#max_workers = O número básico e máximo do pool (número de threads)
with ThreadPoolExecutor(max_workers=5) as executor: #instanciando uma implementação da interface ExecutorService e entregando as tarefas para execução
    
    ini = time.time()
    fibSubmit = {executor.submit(fib, n,): n for n in numeros} # chamando a função de fibonacci para a execução nos threads
    fim = time.time()
    


    for future in as_completed(fibSubmit): #Printando a resposta da função de fibonacci com os numeros sugeridos, com tratamento de exeção de erro
        try:
            n, f = future.result()
        except Exception as exc:
            print("Erro! {0}".format(exc))
        else:
            print ("Fibonacci({0}): {1}".format(n, f))

    print('Tempo Gasto: %s\n' % (fim - ini))


