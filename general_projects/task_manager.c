#include <stdio.h>
#include <string.h>

// task is in the format "\033[##m{task}\033[0m"
// look at add_task and complete_task to understand

// global variables
int num = 0;
char tasks[100][107];

// utilities
void add_task();
void view_tasks();
void complete_task();
void remove_task();

int main()
{
    printf("\033[2J");
    while (1)
    {
        int option;
        printf("\033[H\
Task Manager\n\
1. Add Task\n\
2. View Tasks\n\
3. Remove Task\n\
4. Mark Task as completed\n\
5. Exit\n\n");
        do
        {
            printf("Select an option: \033[0K");
            scanf("%d", &option);
            printf("\033[0J\n");
        } while (!(option >= 1 && option <= 5));

        switch (option)
        {
        case 1:
            add_task();
            break;
        case 2:
            view_tasks();
            break;
        case 3:
            remove_task();
            break;
        case 4:
            complete_task();
            break;
        case 5:
            return 0;
        }
    }
}

// definitions

/*for making difference between completed and uncompleted tasks
 *completed tasks have green color while uncompleted are red
 *I  used ansi escape codes for coloring
 *4 coloring bytes + 100 task + 3 default color bytes
 *num now represent the index
 * for more info
 * https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
 */
void add_task()
{
    if (num < 100)
    {

        char task[100];
        strcpy(tasks[num], "\033[31m");

        printf("Enter task description: ");
        scanf("%99s", task); // 99 refers to characters except for '\0' so the max input string will take 100 characters with the null character

        strcat(strcat(tasks[num], task), "\033[0m");

        // now it represents the number of strings
        num++;
        printf("Task added successfully!\n\n");
    }
    else
    {
        printf("you exceeded maximum number of tasks\n\n");
    }
}

void view_tasks()
{
    if (num != 0)
    {

        for (int i = 0; i < num; i++)
        {
            // to make a tabular format max number is 100 which requires 3 places
            // you can see the tabular format if you entered more than ten inputs 
            printf("%3d %s\n", i + 1, tasks[i]);
        }
        printf("\n");
    }
    else
    {
        printf("No tasks to read\n\n");
    }
}

void complete_task()
{
    int id;
    printf("Enter task ID to mark as completed: ");
    scanf("%d", &id);
    if (1 <= id && id <= num)
    {
        if (tasks[id - 1][3] != '2')
        {
            // "\033[31m" so '1' has index of 3 -> "\033[32m"
            // which is green color check github link at line 64
            tasks[id - 1][3] = '2';
            printf("Task was completed successfully\n\n");
        }
        else
        {
            printf("Task is completed already\n\n");
        }
    }
    else
    {
        printf("No Tasks to complete or ID (should be from 1 to %d) is not valid\n\n", num);
    }
}

void remove_task()
{
    int id;
    printf("Enter task ID to remove: ");
    scanf("%d", &id);
    if (1 <= id && id <= num)
    {
        for (int i = id - 1; i < num - 1; i++)
        {
            strcpy(tasks[i], tasks[i + 1]);
        }
        printf("Task removed successfully!\n\n");
        num--;
    }
    else
    {
        printf("No Tasks to remove or  ID (should be from 1 to %d) is not valid\n\n", num);
    }
}