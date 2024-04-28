//stack implemented using vector/array like dynamic list
#include <iostream>
#include <vector>
using namespace std;

class Stack {
private:
    vector<int> elements;

public:
    void push(int data){
        elements.push_back(data);
    }

    bool isEmpty(){
        return elements.empty();
    }

    int pop(){
        if(elements.empty()){
            throw "Stack is empty";
        } else {
            int data = elements.back();
            elements.pop_back();
            return data;
        }
    }

    int peek(){
        if(isEmpty()){
            throw "Stack is empty";
        }
        int val = elements.back();
        return val;
    }

    ~Stack(){
        elements.clear();
    }


};


int main(){
    Stack myStack;
    myStack.push(1);
    myStack.push(2);
    myStack.push(4);
    while(!myStack.isEmpty()){
        cout << myStack.peek() << endl;
        myStack.pop();
    }
}