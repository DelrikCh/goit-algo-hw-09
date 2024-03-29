# Порівняння ефективності жадібного алгоритму та алгоритму динамічного програмування для видачі решти

Під час тестування на великих сумах (9128360), було проведено порівняння ефективності двох алгоритмів для визначення оптимального способу видачі решти. Ось отримані результати:

## Жадібний алгоритм:
- Час виконання: 2.86102294921875e-06
- Результат: {50: 182567, 25: 0, 10: 1, 5: 0, 2: 0, 1: 0}

## Алгоритм динамічного програмування:
- Час виконання: 5.590205192565918
- Результат: {50: 182567, 25: 0, 10: 1, 5: 0, 2: 0, 1: 0}

## Висновки:
Загалом, жадібний алгоритм виявився швидшим за алгоритм динамічного програмування на великих сумах. Проте, алгоритм динамічного програмування зазвичай гарантує оптимальний результат, тоді як жадібний алгоритм може не завжди забезпечувати оптимальний варіант, особливо у складних ситуаціях з великою кількістю монет різного номіналу.
