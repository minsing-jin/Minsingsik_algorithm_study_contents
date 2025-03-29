//
// Created by 진민성 on 3/28/25.
//
#include <iostream>
#include <limits>

#define MAX_SIZE 100

int stack[MAX_SIZE];
int top = -1;
int minValue = INT_MAX;

void push(int x) {
    if (top == MAX_SIZE - 1) {
        std::cout << "Stack Overflow\n";
        return;
    }

    if (isEmpty()) {
        stack[++top] = x;
        minValue = x;
    } else {
        if (x >= minValue) {
            stack[++top] = x;
        } else {
            stack[++top] = 2 * x - minValue;
            minValue = x;
        }
    }
}

int pop() {
    if (isEmpty()) {
        std::cout << "Stack Underflow\n";
        return INT_MIN;
    }

    int popped = stack[top--];
    if (popped >= minValue) {
        return popped;
    } else {
        int temp = minValue;
        minValue = 2 * minValue - popped;
        return temp;
    }
}

int topElement() {
    if (isEmpty()) {
        std::cout << "Stack is empty\n";
        return INT_MIN;
    }

    return stack[top] >= minValue ? stack[top] : minValue;
}

int getMin() {
    if (isEmpty()) {
        std::cout << "Stack is empty\n";
        return INT_MIN;
    }

    return minValue;
}

bool isEmpty() {
    return top == -1;
}

int main() {
    // Example usage (same as C)
    return 0;
}
