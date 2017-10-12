#include <iostream>
#include <list>
#include "node.hpp"
#include "channel.hpp"
#include "content.hpp"

using namespace std;
int main(int argc, char **argv) {
	Node test_node(0, 8080, "name", "key");
	cout << test_node.GetHandle() << "\n";

	Channel test_channel("", "1337pa55");
	cout << test_channel.GetPassword() << "\n";

	test_channel.AddNode(&test_node);
	test_channel.DropNode(&test_node);
	cout << test_channel.GetNodes().empty() << "\n";

	Content test_content;
	test_content.Load("main.cpp");
	test_content.Dump("new.cpp");
	return(0);
}
