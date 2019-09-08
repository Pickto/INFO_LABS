#include <iostream>
#include <string>
#include <map>

using namespace std;

map<char, int> enum_num = { {0 , '0'}, {1 , '1'}, {2, '2'}, {3, '3'}, {4, '4'}, {5, '5'}, {6, '6'}, {7, '7'},
						{8, '8'}, {9, '9'}, {10, 'A'}, {11, 'B'}, {12, 'C'}, {13, 'D'}, {14, 'E'}, {15, 'F'} };

map<char, int> enum_lit = { {'0' , 0}, {'1' , 1}, {'2', 2}, {'3', 3}, {'4', 4}, {'5', 5}, {'6', 6}, {'7', 7},
						{'8', 8}, {'9', 9}, {'A', 10}, {'B', 11}, {'C', 12}, {'D', 13}, {'E', 14}, {'F', 15} };

double trans_to(double value, int base)
{
	int int_part = int(value);
	double double_part = value - int(value);

	string res = "";
	string revers = "";
	int num;

	while (int_part != 0)
	{
		num = int_part % base;
		revers += enum_num[num];
		int_part /= base;
	}

	for (int i = revers.size() - 1; i >= 0; i--)
		res += revers[i];

	res += ".";
	int e = 0;

	while ((double_part - int(double_part) != 0.0) && e < 10)
	{
		e++;
		double_part *= base;
		res += enum_num[(int(double_part))];
		double_part = double_part - int(double_part);
	}

	if (res[res.size() - 1] == '.')
		res[res.size() - 1] = '\0';

	return atof(res.c_str());
}

double trans_from(string value, int base)
{
	int num_dot = value.find('.');
	string int_part = value.substr(0, num_dot);
	string double_part = value.substr(num_dot + 1, value.size() - 1);

	double res = 0.0;

	int i = 0;

	while (int_part != "")
	{
		res += enum_lit[int_part[int_part.size() - 1]] * pow(base, i);
		int_part.erase(int_part.size() - 1, 1);
		i++;
	}

	i = -1;
	int j = 0;

	while (double_part[j] != '\0' && double_part > "000000000001")
	{
		res += enum_lit[double_part[j]] * pow(base, i);
		i--;
		j++;
	}

	return res;
}

int main()
{
	string x;
	double res;
	int base;

	cin >> x >> base;

	res = trans_from(x, base);

	printf_s("%.10f", res);

	system("pause");
	return 0;
}