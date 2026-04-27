# 📚 Linked List Implementations & Postfix Expression Evaluator

This project contains implementations of a singly linked list, a doubly linked list, and a postfix (Reverse Polish Notation) expression evaluator built using a custom stack based on a singly linked list.

---

## 📦 Overview

The project includes:

- MySinglyLinkedList → Singly linked list with head & tail optimization  
- MyLinkedList → Doubly linked list implementation  
- compute(postfix_expression) → Postfix expression evaluator (stack-based)

---

## 🔗 Singly Linked List (MySinglyLinkedList)

A singly linked list optimized with head and tail pointers for efficient operations.

### Features

- _head → first element  
- _tail → last element  
- _size → number of elements  

### Operations

add_first(e): Insert at front → O(1)  
add_last(e): Insert at end → O(1)  
remove_first(): Remove first → O(1)  
first(): Get first element → O(1)  
last(): Get last element → O(1)  
size(): Return size → O(1)  
is_empty(): Check if empty → O(1)  

---

## 🔗 Doubly Linked List (MyLinkedList)

A doubly linked list allowing traversal in both directions.

Each node contains:

- data  
- next  
- prev  

### Operations

add_first(e): O(1)  
add_last(e): O(1)  
remove_first(): O(1)  
remove_last(): O(1)  
first(): O(1)  
last(): O(1)  
size(): O(1)  
is_empty(): O(1)  

---

## 🧮 Postfix Expression Evaluator

### Function: compute(postfix_expression)

Evaluates expressions written in Reverse Polish Notation using a stack based on MySinglyLinkedList.

### Supported operators

Addition +
Subtraction -
Multiplication *
Division /  

---

### Algorithm

1. Split expression into tokens  
2. Push numbers onto stack  
3. When operator appears:
   - Pop two values  
   - Apply operation  
   - Push result  
4. Final stack must contain exactly one value  

---

## ⚠️ Error Handling

Raises errors for:

- Empty expression  
- Invalid token  
- Not enough operands  
- Division by zero  
- Remaining unused operands  

---

## ▶️ Example

3 4 + 2 * 7 / = 2.0  
5 1 2 + 4 * + 3 - = 14  

---

## ▶️ Run

python your_file.py

---

## 📌 Notes

- Stack uses singly linked list (add_first / remove_first)  
- Tail pointer ensures O(1) append  
- Doubly linked list supports bidirectional traversal  

---

## 👨‍💻 Authors
Kevin Youssef
Lukas Url
Bence Auer

Data structures exercise focusing on:

- Linked lists  
- Stack implementation  
- Postfix evaluation  