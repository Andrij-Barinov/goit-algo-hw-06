# Домашнє завдання: Робота з графами

## Опис завдання

Це домашнє завдання спрямоване на освоєння роботи з графами, використовуючи бібліотеку NetworkX у Python. Ви дізнаєтеся, як створювати, аналізувати та виконувати пошукові алгоритми на графах, а також знайдете найкоротший шлях у графі за допомогою алгоритму Дейкстри.

## Структура проєкту

Проєкт складається з трьох Python файлів:

1. **`graph_creation.py`** — відповідає за створення та аналіз графа.
2. **`search_algorithms.py`** — містить реалізацію та порівняння алгоритмів DFS і BFS.
3. **`dijkstra_algorithm.py`** — реалізує алгоритм Дейкстри для пошуку найкоротшого шляху та візуалізації результату.

## Виконані завдання

### Завдання 1: Створення та аналіз графа

Було створено граф, що моделює транспортну систему міста. Граф складається з п'яти станцій, з'єднаних сімома дорогами.

**Аналіз графа:**

- **Кількість вершин:** 5
- **Кількість ребер:** 7
- **Ступінь кожної вершини:**
  - Station1: 3
  - Station2: 3
  - Station3: 3
  - Station4: 3
  - Station5: 2

### Завдання 2: Реалізація та порівняння DFS і BFS

**Результати:**

- **DFS шлях:** Station1 -> Station2 -> Station3 -> Station4 -> Station5
- **BFS шлях:** Station1 -> Station2 -> Station3 -> Station5 -> Station4

**Порівняння:**

- DFS (пошук у глибину) досліджує граф, переходячи глибше по одному шляху до кінця перед поверненням назад.
- BFS (пошук у ширину) досліджує сусідів кожної вершини на поточному рівні перед переходом на наступний рівень, що робить його більш підходящим для пошуку найкоротшого шляху в невагових графах.

### Завдання 3: Реалізація алгоритму Дейкстри

Було додано ваги до ребер графа, що відображають відстань між станціями. Алгоритм Дейкстри був застосований для знаходження найкоротшого шляху між двома станціями.

**Результати:**

- **Найкоротший шлях за алгоритмом Дейкстри:** Station1 -> Station3 -> Station4
- **Довжина найкоротшого шляху:** 9

## Як використовувати

1. Запустіть `graph_creation.py` для створення та аналізу графа.
2. Запустіть `search_algorithms.py` для виконання та порівняння алгоритмів DFS і BFS.
3. Запустіть `dijkstra_algorithm.py` для виконання алгоритму Дейкстри та візуалізації найкоротшого шляху.

## Висновки

Це домашнє завдання дозволяє зрозуміти основи роботи з графами, дослідити різницю між пошуковими алгоритмами та навчитися знаходити найкоротші шляхи в графах з вагами. Дані навички є основою для подальшого розуміння та вирішення більш складних задач у сфері комп'ютерних наук.
