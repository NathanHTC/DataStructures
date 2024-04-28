//implement stack using linked list
#include <iostream>
using namespace std;

class StackNode {
    public:
    int data;
    StackNode* next;

    StackNode(int data){
        this->data = data;
        next = nullptr;
    }
};

class Stack {
public:
    StackNode* top;

    Stack(){
        top = nullptr;
    }

    //push data on the top of stack
    void push(int data){
        StackNode* newNode = new StackNode(data);
        if(top == nullptr){
            //stack is empty, set top pointer to newNode pointer
            top = newNode;
        } else {
            newNode->next = top;
            top = newNode;
        }
    }

    bool isEmpty(){
        return top == nullptr;
    }

    //pop the top value
    int pop(){
        if(top == nullptr){
            throw "stack is empty";
        }
        int popData = top->data;
        StackNode* temp = top; 
        top = top->next;
        delete temp; //free memory
        return popData;
    };

    //return the top value
    int peek(){
        if(top == nullptr){
            throw "stack is empty";
        } else {
            int val = top->data;
            return val;
        }
    }

    ~Stack(){
        while(top != nullptr){
            StackNode* temp = top;
            top = top->next;
            delete temp;
        }
    }
};

int main(){
    Stack myStack;
    myStack.push(1);
    myStack.push(2);
    myStack.push(3);
    while(!myStack.isEmpty()){
        cout << myStack.peek() << endl;
        myStack.pop();
    }
    
}