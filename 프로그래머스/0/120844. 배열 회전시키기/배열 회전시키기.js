function solution(numbers, direction) {
   return direction === 'right' ? [numbers.pop(), ...numbers]:[...numbers.slice(1), numbers[0]];}