#include <iostream>
#include <vector>
#include <map>

int main()
{
    int N;

    std::cin >> N;
    int useHealth[20];
    int getHappy[20];
    bool dpArray[20];

    for (int i = 0; i < N; i++)
    {
        std::cin >> useHealth[i];
    }
    for (int i = 0; i < N; i++)
    {
        std::cin >> getHappy[i];
    }
}