#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * main - entry poin.
 *
 * Return 0
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else
			return (0);
	}
	while (1)
		sleep(1);
	
	return (0);
}

