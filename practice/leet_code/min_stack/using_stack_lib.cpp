//
// Created by 진민성 on 3/28/25.
//
#include <iostream>
#include <stack>

class MinStack {
private:
    std::stack<int> mainStack;
    std::stack<int> minStack;

public:
    void push(int value) {
        mainStack.push(value);

        if (minStack.empty() || value <= minStack.top()) {
            minStack.push(value);
        } else {
            minStack.push(minStack.top());
        }
    }

    int pop() {
        if (mainStack.empty()) {
            return -1;  // Stack is empty
        }

        int popped_value = mainStack.top();
        mainStack.pop();
        minStack.pop();

        return popped_value;
    }

    int getMin() {
        if (mainStack.empty()) {
            return -1;  // Stack is empty
        }

        return minStack.top();
    }
};

int main() {
    MinStack minStack;

    minStack.push(3);
    minStack.push(5);
    minStack.push(2);
    minStack.push(1);

    std::cout << "Minimum element: " << minStack.getMin() << std::endl;  // Expected output: 1

    minStack.pop();
    minStack.pop();

    std::cout << "Minimum element after popping: " << minStack.getMin() << std::endl;  // Expected output: 3

    return 0;
}
