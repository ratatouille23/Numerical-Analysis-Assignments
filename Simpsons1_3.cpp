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

    stepSize = (upper - lower)/(2 * subInterval);


    integration = f(lower) + f(upper);

    for(int i = 1; i < subInterval; i++){
        float k = lower + 2 * i * stepSize;
        integration = integration + 2 * f(k);
    }

    for(int i = 1; i <= subInterval; i++){
        float k = lower + (2 * i - 1) * stepSize;
        integration = integration + 4 * f(k);
    }

    integration = (integration * stepSize) / 3;

    cout << integration << endl;
    return 0;
}