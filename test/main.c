#include <stdio.h>
int main(void) {
	char *line = NULL;
	size_t len = 0;
	ssize_t lineSize = 0;
	lineSize = getline(&line, &len, stdin);
	printf("%s\n", line);
	return 0;
}
