#ifndef CHANNEL
#define CHANNEL
#include <string>
#include <list>
#include "node.hpp"
class Channel {
	private:
		std::string _handle, _password;
		std::list<Node*> _nodes;
	public:
		Channel(std::string handle, std::string password);
		void SetHandle(std::string handel);
		void SetPassword(std::string password);
		void AddNode(Node* node);
		void DropNode(Node* node);
		std::string GetHandle();
		std::string GetPassword();
		std::list<Node*> GetNodes();
};
#endif
