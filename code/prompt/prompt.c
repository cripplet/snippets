#include <stdio.h>
#include <string.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>

#define MAXLINE		1024

/**
 * function list
 */

void main(int argc, char** argv);
void usage();
void sigint_handler();
void quit();
void process_buf(char* buf);

/**
 * global variables
 */

char prompt[] = "> ";
int verbose = 0;

void main(int argc, char** argv)
{
	// @c the cli options
	char c;
	char buf[MAXLINE];

	/**
	 * signal handlers
	 */

	signal(SIGINT, sigint_handler);

	/**
	 * parses arguments
	 */

	while((c = getopt(argc, argv, "hv")) != EOF)
	{
		switch(c)
		{
			case 'v':
				verbose = 1;
				break;
			case 'h':
			default:
				usage(argv[0]);
		}
	}

	/**
	 * recieves commands
	 */

	while(1)
	{
		printf("%s", prompt);
		fflush(stdout);
		fgets(buf, MAXLINE, stdin);
		if(feof(stdin))
			quit();
		process_buf(buf);
		memset(buf, 0, sizeof(buf));
	}
}

void usage(char* exec_name)
{
	printf("Usage: %s [-hv]\n", exec_name);
	printf("\t-h\tprint this message\n");
	printf("\t-v\tverbose\n");
	exit(0);
}

void sigint_handler ()
{
//	printf("\n");
//	process_buf("");
	printf("\n%s", prompt);
	fflush(stdout);
//	printf("\nsigint has been called (ctrl + c)\n");
}

// ctrl + d
void quit()
{
	printf("exit\n");
	exit(0);
}

void process_buf(char* buf)
{
	printf("buf is %s", buf);
}
