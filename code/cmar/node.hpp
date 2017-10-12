#ifndef NODE
#define NODE
#include <string>
class Node {
	private:
		unsigned long _address;
		unsigned short _port;
		std::string _handle, _public_key;
	public:
		Node(unsigned long address, unsigned short port, std::string handle, std::string public_key);
		void SetAddress(unsigned long address);
		void SetPort(unsigned short port);
		void SetHandle(std::string handle);
		void SetPublicKey(std::string public_key);
		unsigned long GetAddress();
		unsigned short GetPort();
		std::string GetHandle();
		std::string GetPublickKey();
};
#endif
