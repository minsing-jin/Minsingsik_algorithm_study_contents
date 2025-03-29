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
        this->MAXQUEUE = k+1; // 애초에 MAXQUEUE는 실제 array 칸의 개수로 설정해야함. -> k로 설정한건 내 상상속 array 칸의 개수
        this->queue = new int[this->MAXQUEUE];
        this->front = 0; // reserved space init
        this->rear = 0;
    }

    bool enQueue(int value) {
        if (isFull()) return false;
        if (rear == MAXQUEUE-1) rear = 0; else rear += 1;
        queue[rear] = value;

        return true;
    }

    bool deQueue() {
        if (isEmpty()) return false;
        if (front == MAXQUEUE-1) front = 0; else front += 1;
        return true;
    }

    int Front() {
        if (this->isEmpty() == true) return -1; else return queue[(front+1) % MAXQUEUE];
    }

    int Rear() {
        if (this->isEmpty() == true) return -1; else return queue[rear];
    }

    bool isEmpty() {
        if (front == rear) return true; else return false;
    }

    bool isFull() {
        if (front == (rear+1) % MAXQUEUE) return true; else return false;
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