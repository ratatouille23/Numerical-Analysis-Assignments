#include<bits/stdc++.h>
using namespace std;

float f(float x){
    return 1/(1 + pow(x,2));
}

int main()
{
    float lower, upper, integration=0.0, stepSize;
    int subInterval;

    cin >> lower >> upper;
    cin >> subInterval;

    stepSize = (upper - lower)/subInterval;


    integration = (f(lower) + f(upper)) / 2;

    for(int i = 1; i < subInterval; i++){
        float k = lower + i * stepSize;
        integration = integration + f(k);
    }

    integration = integration * stepSize;

    cout << integration << endl;
    return 0;
}