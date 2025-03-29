//
// Created by 진민성 on 3/29/25.
//
class MyCircularQueue {
private:
    int *queue;
    int front;
    int rear;
    int MAXQUEUE;
public:
    MyCircularQueue(int k) {
        this->MAXQUEUE = k;
        this->queue = new int[this->MAXQUEUE];
        this->front = -1;
        this->rear = -1;
    }

    bool enQueue(int value) {
        if (isFull()) return false;
        if (isEmpty()) front = 0; // front init when arr is empty.
        rear = (rear + 1) % MAXQUEUE; // 순환적 증가
        queue[rear] = value;

        return true;
    }

    bool deQueue() {
        if (isEmpty()) return false;
        if (front == rear) { // Only one elem left
            front = -1;
            rear = -1;
        } else {
            front = (front+1) % MAXQUEUE;
        }
        return true;
    }

    int Front() {
        if (isEmpty()) return -1;
        return queue[front];
    }

    int Rear() {
        if (isEmpty()) return -1;
        return queue[rear];
    }

    bool isEmpty() {
        return front == -1;
    }

    bool isFull() {
        return front == (rear + 1) % MAXQUEUE;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */