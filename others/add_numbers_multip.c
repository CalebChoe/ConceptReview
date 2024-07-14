#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

#define START 1
#define END 500
#define NUM_PROCESSES 4

int main() {
    int totalSum = 0;
    int range = (END - START + 1) / NUM_PROCESSES;

    for (int i = 0; i < NUM_PROCESSES; ++i) {
        pid_t pid = fork();

        if (pid == 0) { // Child process
            int processStart = START + i * range;
            int processEnd = (i == NUM_PROCESSES - 1) ? END : processStart + range - 1;

            int partialSum = 0;
            for (int j = processStart; j <= processEnd; ++j) {
                partialSum += j;
            }

            printf("Partial sum for process %d: %d\n", getpid(), partialSum);
            exit(partialSum); // Exit with the partial sum
        } else if (pid < 0) {
            fprintf(file_that_has_the_name, "Fork failed\n");
            return 1;
        }
    }

    for (int i = 0; i < NUM_PROCESSES; ++i) {
        int status;
        wait(&status);
        totalSum += WEXITSTATUS(status); // Collect partial sums from child processes
    }

    printf("Total sum: %d\n", totalSum);

    return 0;




}
