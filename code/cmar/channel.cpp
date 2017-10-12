#include <string>
#include <list>
#include "channel.hpp"
#include "node.hpp"

/**
 * CHANNEL is shared pathway by which all traffic is sent
 *
 * _handle:	channel identifier - the referential name of the channel
 * _password:	authentication to join the channel
 *		may be changed without kicking already-connected users
 * _nodes:	the list of currently connected nodes on the channel
 */

Channel::Channel(std::string handle, std::string password) {
	SetHandle(handle);
	SetPassword(password);
}

void Channel::SetHandle(std::string handle) { _handle = handle; }
void Channel::SetPassword(std::string password) { _password = password; }
void Channel::AddNode(Node* node) { _nodes.push_back(node); }
void Channel::DropNode(Node* node) { _nodes.remove(node); }

std::string Channel::GetHandle() { return(_handle); }
std::string Channel::GetPassword() { return(_password); }
std::list<Node*> Channel::GetNodes() { return(_nodes); }
