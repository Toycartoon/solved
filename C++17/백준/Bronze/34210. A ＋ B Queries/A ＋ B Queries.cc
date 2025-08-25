#include "aplusb.h"
#include <utility>
#include <vector>

using namespace std;

vector a(200000, 0);
vector b(200000, 0);

void initialize(std::vector<int> A, std::vector<int> B) {
    a = std::move(A);
    b = std::move(B);
}

int answer_question(int i, int j) {
    return a[i] + b[j];
}
