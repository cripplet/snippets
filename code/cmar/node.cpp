#include <string>
#include "node.hpp"

/**
 * NODE uniquely identifies the user agent, and is used for addressing purposes
 *
 * _address:	the IP address of the user (has potentially been resolved via DNS)
 * _port:	the port of the user by which to communicate bi-directional traffic
 * _handle:	username of the user
 * _public_key:	the public key of the user
 */

Node::Node(unsigned long address, unsigned short port, std::string handle, std::string public_key) {
	SetAddress(address);
	SetPort(port);
	SetHandle(handle);
	SetPublicKey(public_key);
}

void Node::SetAddress(unsigned long address) { _address = address; }
void Node::SetPort(unsigned short port) { _port = port; }
void Node::SetHandle(std::string handle) { _handle = handle; }
void Node::SetPublicKey(std::string public_key) { _public_key = public_key; }

unsigned long Node::GetAddress() { return(_address); }
unsigned short Node::GetPort() { return(_port); }
std::string Node::GetHandle() { return(_handle); }
std::string Node::GetPublickKey() { return(_public_key); }
