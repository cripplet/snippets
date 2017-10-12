#ifndef UTILS
#define UTILS
#include <iostream>
#include <sys/stat.h>
class Utils {
	public:
		static void Panic(std::string function, std::string message);
		static void Warn(std::string function, std::string message);
		static void Notify(std::string message);
		static void Debug(std::string message);
		static void Write(std::string header, std::string message);
		static bool FileExists(std::string filename);
};
#endif
