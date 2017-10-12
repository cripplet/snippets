#include <iostream>
#include <sys/stat.h>
#include "utils.hpp"
void Utils::Panic(std::string function, std::string message) {
	Write("error", function + " : " + message);
	exit(-1);
}
void Utils::Warn(std::string function, std::string message) { Write("warning", function + " : " + message); }
void Utils::Notify(std::string message) { Write("notice", message); }
void Utils::Debug(std::string message) { Write("debug", message); }
void Utils::Write(std::string header, std::string message) {
	std::cerr << header << " : " << message << std::endl;
}
// check if file exists
//	http://bit.ly/127J21e
bool Utils::FileExists(std::string filename) {
	struct stat buf;
	return(stat(filename.c_str(), &buf) != -1);
}
