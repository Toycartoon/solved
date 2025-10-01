#include "timecard.h"

static int N;

void init(int n) {
	N = n;
}

std::string convert(std::string s) {
	for(int i=0; i < s.size(); i++)
        s[i] = tolower(s[i]);
	return s;
}
