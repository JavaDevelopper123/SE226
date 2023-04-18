#3
#include <iostream>
#include <math.h>
double sum_of_series = 0;

void compute_series(int n) {
    if (n == 1) {
        sum_of_series += pow(-1, n+1) / n;
    }
    else {
        sum_of_series += pow(-1, n+1) / n;
        compute_series(n-1);
    }
}

#include <cmath>

using namespace std;

double recursiveSum(int n) {
    if(n==1) {
        return -1.0;
    }
    else {
        double term = pow(-1.0, n+1) / n;
        return term + recursiveSum(n-1);
    }
}

int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;
    double result = recursiveSum(n);
    cout << "The summation is: " << result << endl;
    return 0;
}


#4
#include <iostream>
#include <cmath>

using namespace std;

double recursiveSum() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;

    if(n==1) {
        return -1.0;
    }
    else {
        double term = pow(-1.0, n+1) / n;
        return term + recursiveSum(n-1);
    }
}

int main() {
    double result = recursiveSum();
    cout << "The summation is: " << result << endl;
    return 0;
}
