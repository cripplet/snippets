#ifndef CONTENT
#define CONTENT
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include "utils.hpp"
class Content {
	private:
		std::vector<char> _blob;

	public:
		Content();
		Content(std::vector<char> _blob);
		void SetBlob(std::vector<char> blob);
		void Load(std::string filename);
		void Dump(std::string filename);
		std::vector<char> GetBlob();
		size_t GetSize();
};
#endif
