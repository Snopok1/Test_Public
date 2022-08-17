try:
    def sort_arrey():
        array = list(map(int, input('Введите последовательность целых чисел через пробел:').split()))
        for i in range(1, len(array)):
            x = array [i]
            idx = i
            while idx > 0 and array[idx - 1] > x:
                array[idx] = array[idx - 1]
                idx -= 1
            array[idx] = x
        return array

    def binary_search(array, element):
        low = 0
        high = len(array) - 1
        while low <= high:
            middle = (low + high) // 2
            if array[middle] == element:
                return middle
            elif array[middle] > element:
                high = middle - 1
            else:
                low = middle + 1
        return None

    array = sort_arrey()
    element = int(input('Введите любое целое число:'))

except ValueError as e:
    print('Ошибка! Необходимо вводить целые числа.')
else:
    print()
    print('Отсортированный список, введённых чисел:' '\n', array)
    print()
    print('Индекс числа',element,'в отсортированном списке:',binary_search(array, element))