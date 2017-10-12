#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include "content.hpp"
#include "utils.hpp"

// using namespace std;
Content::Content() {}
Content::Content(std::vector<char> blob) { SetBlob(blob); }

void Content::SetBlob(std::vector<char> blob) { _blob = blob; }

void Content::Load(std::string filename) {
	if(!Utils::FileExists(filename)) {
		Utils::Warn("Content::Load(std::string filename)", "file " + filename + " not found");
		return;
	}
	std::ifstream file;
	file.open(filename);
	// read file one character at a time
	//	http://bit.ly/151lOOy
	if(file.is_open()) {
		std::vector<char> blob;
		char buffer;
		while(file.good()) {
			buffer = file.get();
			// additional check for final char corruption
			if(file.good()) { blob.push_back(buffer); }
		}
		SetBlob(blob);
		file.close();
	}
}
void Content::Dump(std::string filename) {
	if(Utils::FileExists(filename)) {
		Utils::Warn("Content::Dump(std::string filename)", "file " + filename + " already exists - aborting");
		return;
	}
	if(GetSize() == 0) {
		Utils::Warn("Content::Dump(std::string filename)", "no data in blob to write - aborting");
	}
	std::ofstream file(filename);
	if(file.is_open()) {
		// convert blob to string
		//	http://bit.ly/1aSJoQ6
		std::string content(_blob.begin(), _blob.end());
		file << content;
		file.close();
	}
}

std::vector<char> Content::GetBlob() { return(_blob); }
size_t Content::GetSize() { return(_blob.size()); }
