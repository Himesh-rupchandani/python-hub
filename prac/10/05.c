#include <stdio.h>
#define MAX_SIZE 100

struct Queue {
    int queue[MAX_SIZE];
    int front;
    int rear;
};

void initializeQueue(struct Queue *q) {
    q->front = -1;
    q->rear = -1;
}

int isEmpty(struct Queue *q) {
    return (q->front == -1 || q->front > q->rear);
}

int isFull(struct Queue *q) {
    return (q->rear == MAX_SIZE - 1);
}

void enqueue(struct Queue *q, int value) {
    if (isFull(q)) {
        printf("Queue Overflow! Cannot enqueue %d\n", value);
        return;
    }
    if (q->front == -1) {
        q->front = 0;
    }
    q->rear++;
    q->queue[q->rear] = value;
    printf("Enqueued: %d\n", value);
}

int dequeue(struct Queue *q) {
    if (isEmpty(q)) {
        printf("Queue Underflow! Queue is empty\n");
        return -1;
    }
    int value = q->queue[q->front];
    q->front++;
    
    if (q->front > q->rear) {
        q->front = -1;
        q->rear = -1;
    }
    return value;
}

void display(struct Queue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue elements: ");
    for (int i = q->front; i <= q->rear; i++) {
        printf("%d ", q->queue[i]);
    }
    printf("\n");
}

int main() {
    struct Queue q;
    initializeQueue(&q);

    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);

    display(&q);

    printf("Dequeued: %d\n", dequeue(&q));
    printf("Dequeued: %d\n", dequeue(&q));

    display(&q);

    return 0;
}